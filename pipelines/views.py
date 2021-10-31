from django.shortcuts import render

from .tasks import go_to_sleep

def index(request):
	go_to_sleep.delay(5)
	return render(request, 'index.html')