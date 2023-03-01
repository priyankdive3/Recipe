from django.urls import path
from . import views

urlpatterns =[
    # path('',views.ok),
    path('',views.homepage),
    path('signup',views.signup),
    path('login',views.login),
    path('signout',views.signout),
    # path('explore',views.explore),
    path('test',views.test),
    path('explore/<did>',views.viewdetails),
    path('showrecipe/<did>',views.showrecipe),

] 