from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index, name="index"),
		url(r'^join/$', views.signup, name="join"),
		url(r'^login/$', views.signin, name="login"),
]