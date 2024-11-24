# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
<<<<<<< HEAD
]
=======
]
>>>>>>> parent of 2308a95 (a ver si va la politica de privacidad)
