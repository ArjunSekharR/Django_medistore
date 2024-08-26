from django.urls import path
from . import views

urlpatterns = [
    path('med/', views.medicine_list, name='medicine_list'),
    path('add/',views.add_medicine,name='add_medicine'),
    path('update/<int:id>/',views.medicine_update,name='update_med'),
    path('delete/<int:id>/', views.medicine_delete, name='delete_med'),
    path('search/', views.search_medicines, name='search_medicines'),
]
