from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView
#from django.template import RequestContext, loader

from tasks.models import Assignment

class HomeView(TemplateView):
	template_name = 'tasks/home.html'

class IndexView(generic.ListView):
	template_name = 'tasks/index.html'
	context_object_name = 'todo_list'

	def get_queryset(self):
		return Assignment.objects.order_by('dueDate')
#def index(request):
#	todo_list = Assignment.objects.order_by('dueDate')
#	context = {'todo_list': todo_list}
#	return render(request, 'tasks/index.html', context)
	
	#context = RequestContext(request, {
	#	'todo_list': todo_list,
	#})
	#template = loader.get_template('tasks/index.html')
	#return HttpResponse(template.render(context))
	
#def detail(request):
