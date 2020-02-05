from django.conf.urls import url, include
from .views import AnimateView, animateChapter
urlpatterns = [
    url(r'^chapter/$', animateChapter),
    url(r'^$', AnimateView.as_view()),
]
