from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('view_ticket/',views.view_ticket,name='view_ticket'),
    path('edit_ticket/<int:id>/',views.edit_ticket,name='edit_ticket'),
    path('delete_ticket/<int:id>/',views.delete_ticket,name='delete_ticket'),
]
