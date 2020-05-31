from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "Mi super Web Playgound"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"