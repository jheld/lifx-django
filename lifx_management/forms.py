from django import forms

import sys
from os.path import pardir, join, abspath, dirname

bulbLabels = []
fullpathToLIFXPython = join(join(pardir,dirname(dirname(dirname(abspath(__file__))))),'lifx-python/')
if not fullpathToLIFXPython in sys.path:
    sys.path.append(fullpathToLIFXPython)

import lifx

import imp
imp.load_source('schedule_cycle','{0}{1}'.format(fullpathToLIFXPython,'schedule-cycle.py'))

from schedule_cycle import ScheduleCycle
class ScheduleCycleForm(forms.Form):
    for light in lifx.get_lights():
        bulbLabels.append((light.bulb_label,light.bulb_label))
    bulbs = forms.MultipleChoiceField(choices=bulbLabels)
    time = forms.FloatField()
    speed = forms.FloatField()
    def startCycle(self,bulbs,time,speed):
        lights = lifx.get_lights()
        lightsCycle = []
        for light in lights:
            for bulb in bulbs:
                if bulb in light.bulb_label:
                    lightsCycle.append(light)
        scheduleCycle = ScheduleCycle()
        scheduleCycle.driver(lightsCycle,time,speed)
