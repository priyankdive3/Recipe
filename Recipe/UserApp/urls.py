from django.urls import path
from . import views

urlpatterns =[
    # path('',views.ok),
    path('',views.homepage),
    path('signup',views.signup),
    path('login',views.login),
    path('signout',views.signout),
    path('products',views.products),
    path('cart',views.cart),
    path('ok/<did>',views.ok),
    path('explore/<did>',views.viewdetails),
    path('showrecipe/<did>',views.showrecipe),

] 