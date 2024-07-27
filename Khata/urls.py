
from django.urls import path
from Khata import views

urlpatterns = [
    path('',views.index,name='index'),
    path('show_khata/<str:entry_type>/',views.show_khata,name='show_khata'),
    path('new_entry/<str:entry_type>/',views.new_entry,name='new_entry'),
]