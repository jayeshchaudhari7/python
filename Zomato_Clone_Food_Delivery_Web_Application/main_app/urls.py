from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    path('review/<int:restaurant_id>/', views.submit_review, name='submit_review'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
]
