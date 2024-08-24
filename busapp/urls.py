from django.urls import path
from busapp import views

urlpatterns = [
    path('<int:id>',views.index),
    path('savefile',views.save_file),
]