from django.urls import path
from .views import all_order_view,order_customer_view,order_view,order_create_view,order_delete_view,order_update_view

urlpatterns = [
    path('',all_order_view.as_view(),name='show-orders'),
    path('<cus>/',order_customer_view.as_view(),name='show-order-customer-pk'),
    path('order/<ord>/',order_view.as_view(),name='detail-order'),
    path('create/<cus>/',order_create_view.as_view(),name='create-order'),
    path('order/<ord>/delete/',order_delete_view.as_view(),name='delete-order'),
    path('order/<ord>/update/',order_update_view.as_view(),name = 'update-order'),
]
 