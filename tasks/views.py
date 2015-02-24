from django.shortcuts import render
from django.http import HttpResponse
#from django.template import RequestContext, loader

from tasks.models import Assignment

def index(request):
	todo_list = Assignment.objects.order_by('dueDate')
	context = {'todo_list': todo_list}
	return render(request, 'tasks/index.html', context)
	
	#context = RequestContext(request, {
	#	'todo_list': todo_list,
	#})
	#template = loader.get_template('tasks/index.html')
	#return HttpResponse(template.render(context))
	
#def detail(request):
