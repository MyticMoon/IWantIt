# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('iwantit/index.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))

def profile(request):
    template = loader.get_template('iwantit/profile.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template('iwantit/contact.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))