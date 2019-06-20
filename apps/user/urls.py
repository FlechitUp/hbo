from django.conf.urls import url

from apps.user.views import update_profile

urlpatterns = [
    url(r'^', update_profile, name='register'),
]
