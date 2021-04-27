from django.urls import path
from .views import HomepagePageView, AboutPageView # new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomepagePageView.as_view(), name='home'),
]
