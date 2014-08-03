from django.shortcuts import render
from lifx_management.forms import ScheduleCycleForm
from django.views.generic.edit import FormView
import threading
# Create your views here.
class ScheduleCycleView(FormView):
    template_name = 'schedule_cycle.html'
    form_class = ScheduleCycleForm
    success_url = '/'
    def form_valid(self, form):
        timer = threading.Timer(5, form.startCycle, args=[form.cleaned_data['bulbs'], form.cleaned_data['time'], form.cleaned_data['speed']])
        timer.start()
        return super(ScheduleCycleView, self).form_valid(form)

