from django.conf.urls import url, include
from .views import AnimateView, animateChapter, getAllanimates
urlpatterns = [
    url(r'^chapter/$', animateChapter),
    url(r'^getAllanimates/$', getAllanimates),
    url(r'^$', AnimateView.as_view()),
]
