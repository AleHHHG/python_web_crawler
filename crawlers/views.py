from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from .models import CrawlerInstruction, Product, Solution, Service, Log

from django.views import generic

from DefaultCrawler import DefaultCrawler
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'crawlers/index.html'
    context_object_name = 'list_instructions'
    def get_queryset(self):
        return CrawlerInstruction.objects.all()

def generic_list(request, model_name):
	generic_objects = eval(model_name.capitalize()+".objects.all()")
	return render(request, 'crawlers/list.html', {'items': generic_objects, 'model_name': model_name })

def generic_detail(request, model_name, id):
	generic_object = get_object_or_404(eval(model_name.capitalize()), pk=id)
	return render(request, 'crawlers/detail.html', { 'item': generic_object })

def process(request, instruction_id):
	instruction = CrawlerInstruction.objects.get(pk=instruction_id)
	model_name = instruction.get_kind_display()
	crawler = DefaultCrawler(instruction).execute()
	for name, description in zip(crawler['products'],crawler['descriptions']):
		obj, created = eval(model_name+'.objects.get_or_create(name={}, description = {})'.format(repr(name), repr(description)))
	return HttpResponseRedirect(reverse('crawlers:list', kwargs={'model_name': model_name.lower()}))
	
