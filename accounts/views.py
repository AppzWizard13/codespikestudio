from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView( TemplateView):
    template_name = "landing/home.html"


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        return context

