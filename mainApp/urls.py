from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('main', views.model_form_upload, name='upload')
]
