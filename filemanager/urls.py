from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('login/', views.loginPage),
    path('register/', views.registration_view),
    path('logout/', views.logoutPage),
    path('', views.load_user_dashboard),
    path('add-file/', views.add_file),
    path('settings/', views.settings),
    path('share-file/', views.share_file),
    path('search/', views.settings),

]

