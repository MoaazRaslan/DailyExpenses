from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from .models import Order
from django.urls import reverse_lazy
from customer.models import Customer
from .form import OrderUpdateForm

class all_order_view(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'order/all_orders.html'
    context_object_name = 'orders'
    def get_queryset(self):
        orders = Order.objects.filter(customer__user = self.request.user)
        order_by = 'date'
        if self.request.GET.get('order_by'):
            order_by = self.request.GET.get('order_by')
        if self.request.GET.get('asc') == 'false':
            order_by = '-'+order_by
        orders =  orders.order_by(order_by)
        print(order_by)
        return orders


class order_customer_view(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'order/all_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        cus = self.kwargs.get('cus')
        orders = Order.objects.filter(customer__user = self.request.user,customer = cus)
        print(cus)
        order_by = 'date'
        if self.request.GET.get('order_by'):
            order_by = self.request.GET.get('order_by')
        if self.request.GET.get('asc') == 'false':
            order_by = '-'+order_by
        orders =  orders.order_by(order_by)
        print(order_by)
        return orders
    

class order_view(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Order
    template_name = 'order/detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'ord'
    def test_func(self):
        ord_id = self.kwargs.get('ord')
        ord = Order.objects.filter(id=ord_id).first()
        print(ord)
        if ord and ord.customer.user == self.request.user:
            return True
        return False
    
    def get_queryset(self):
        ord_id = self.kwargs.get('ord')
        order = Order.objects.filter(id=ord_id)
        return order
    
class order_create_view(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Order
    template_name = 'order/create.html'
    fields = ['name','date','amount','price','description','payed']
    context_object_name = 'order'

    def get_success_url(self):
        success_url = reverse_lazy('show-order-customer-pk' ,kwargs ={'cus':self.kwargs.get('cus')})
        return success_url
        
    def test_func(self):
        cus_id = self.kwargs.get('cus')
        cus = Customer.objects.filter(id = cus_id).first()
        if cus and cus.user == self.request.user:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.customer = Customer.objects.filter(id = self.kwargs.get('cus')).first()
        return super().form_valid(form)


class order_delete_view(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Order
    template_name = 'order/delete.html'
    pk_url_kwarg = 'ord'
    def test_func(self):
        ord_id = self.kwargs.get('ord')
        cus_id = Order.objects.filter(id = ord_id).first().customer.id
        print(cus_id)
        print(cus_id)
        cus = Customer.objects.filter(id = cus_id).first()
        if cus and cus.user == self.request.user:
            return True
        return False
    
    def get_success_url(self):
        cus_id = Order.objects.filter(id = int(self.kwargs.get('ord'))).first().customer.id
        print('id = ',cus_id)
        successful_url = reverse_lazy('show-order-customer-pk',kwargs = {'cus':cus_id})
        print(successful_url)
        return successful_url
    

class order_update_view(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Order
    template_name ='order/update.html'
    context_object_name = 'order'
    pk_url_kwarg = 'ord'
    fields = ['name','date','amount','price','description','payed']

    def test_func(self):
        ord_id = self.kwargs.get('ord')
        cus_id = Order.objects.filter(id = ord_id).first().customer.id
        cus = Customer.objects.filter(id = cus_id).first()
        if cus and cus.user == self.request.user:
            return True
        return False

    def get_success_url(self):
        success_url = reverse_lazy('detail-order',kwargs = {'ord':self.kwargs.get('ord')})
        return success_url