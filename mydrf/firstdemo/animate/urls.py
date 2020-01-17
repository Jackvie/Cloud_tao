from django.conf.urls import url, include
from .views import AnimateView
urlpatterns = [
    url(r'^$', AnimateView.as_view()),
]