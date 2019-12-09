from django.urls import path
  
from . import views

urlpatterns = [
        path('', views.all_squirrels),
        path('add/', views.add_squirrel),
        path('<Unique_Squirrel_ID>/', views.edit_squirrel),
        path('stats',views.stats_squirrel),
]

