from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.createUser,name='createUser'),
    path('logout/', views.logout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('search/', views.search,name='search'),
    path('settings/', views.settings,name='settings'),
    path('account/',views.account,name="account"),
<<<<<<< HEAD
    path('api/',views.api,name="api"),
=======
    path('add_family/',views.add_family,name="add_family"),
>>>>>>> 8df0d68f8e7a417dac06ce485b1ed73ac1f967b4
]
