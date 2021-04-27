from django.views.generic import TemplateView

# Create your views here.
class HomepagePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): # new
    template_name = 'about.html'
