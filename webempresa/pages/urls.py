from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:slug>/', views.page, name="page"),
]