from django.urls import path, re_path
# from django.views.decorators.cache import cache_page
from django.views.generic import *
from . import views
from .views import *
# app_name = 'poll'


urlpatterns = [
    # path('', index, name='home'),
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('post/<slug:slug>/', ProductDetailView.as_view(), name = 'product-detail'),
    path('catalog/post/new/', ProductCreateView.as_view(), name = 'product-create'),
    path('post/<int:pk>/update/', ProductUpdateView.as_view(), name = 'product-update'),
    path('post/<int:pk>/delete/', ProductDeleteView.as_view(), name = 'product-delete'),
    
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/',  TechCategory.as_view(), name='category'),
    
    path('share/<int:product_id>', post_share, name='post_share'),

    path('search/', post_search, name='post_search'),
    
    
    
    path('add-to-cart/<slug:slug>/',views.add_to_cart, name='add-to-cart'),
     path('remove-from-cart/<slug:slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('cart-summary/', ShoppingCartSummaryView.as_view(), name='cart-summary'),
    

    
    # Wish List
    path("wishlist", views.wishlist, name="wishlist"),
    path("wishlist/add_to_wishlist/<int:id>", views.add_to_wishlist, name="user_wishlist"),


    path('shsup/', shsup, name='shsup'),
    path('acceptorder/', views.acceptorder, name='acceptorder'),
    
]
