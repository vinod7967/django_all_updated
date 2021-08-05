from django.urls import path
from . import views

urlpatterns = [
    path('',views.first_page, name='first_page'),
    path('signup',views.signup, name='signup'),
    path('login',views.user_login,name='login'),
    path('first_page',views.first_page,name='first_page'),
    path('logout', views.user_logout,name='logout'),
    path('show', views.show, name = 'show'),
    path('edit/<int:id>', views.update_ticket, name = 'update_ticket'),
    path('delete/<int:id>', views.destroy, name = 'destroy'),
    path('get_sess', views.getsession, name = 'get'),
    path('del_sess', views.delsession, name = 'del'),
    path('del_coo', views.delcookie, name = 'del'),
    path('get_coo', views.getcookie, name = 'get'),
]
