from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomeWeatherView(TemplateView):

    template_name = 'weather/index.html'
    extra_context = {
        'title' : 'Weather'
    }