from django.urls import path
from .views import all_customer_view,create_customer_view,delete_customer_view,detail_customer_view,update_customer_view

urlpatterns = [
    path('',all_customer_view.as_view(),name='customer-home'),
    path('profile/<pk>/',detail_customer_view.as_view(),name='detail-view'),
    path('create/',create_customer_view.as_view(),name='create-customer'),
    path('<pk>/delete/',delete_customer_view.as_view(),name='delete-customer'),
    path('<pk>/update/',update_customer_view.as_view(),name='update-customer'),
]
