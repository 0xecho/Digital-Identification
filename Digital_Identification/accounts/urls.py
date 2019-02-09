from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.createUser,name='createUser'),
    path('logout/', views.logout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('search/', views.search,name='search'),
    path('settings/', views.settings,name='settings'),
    path('search/',views.search,name="search"),
]
