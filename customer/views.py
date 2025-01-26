from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
from .models import Customer
from .form import CustomerCreateForm,CustomerUpdateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import Http404

class all_customer_view(LoginRequiredMixin,ListView):
    model = Customer
    template_name = 'customer/home.html'
    context_object_name = 'customers'
    login_url = 'login'
    def get_queryset(self):
        user = self.request.user
        queryset = Customer.objects.filter(user = user)
        print(queryset)
        return queryset
    
class update_customer_view(LoginRequiredMixin,UpdateView):
    model = Customer
    form_class = CustomerUpdateForm
    template_name = 'customer/update.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer-home')
    

class delete_customer_view(LoginRequiredMixin,DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-home')
    template_name = 'customer/delete.html'

class detail_customer_view(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Customer
    template_name = 'customer/detail.html'
    context_object_name = 'customer'

    def test_func(self):
        cus = self.get_object()
        if cus.user == self.request.user:
            return True
        return False

    # def get_queryset(self,queryset = None):
    #     cus =self.request.POST
    #     print(cus)
    #     # customer = super().get_object(queryset)
    #     # print(customer)
    #     # if customer.user != self.request.user:
    #     #     raise Http404('customer not found!')
    #     return "customer"


# @login_required
# def all_customer_view(request):
#     user = request.user
#     customers = Customer.objects.filter(user = user)
#     return render(request,'customer/home.html',{'customers':customers})
    

class create_customer_view(LoginRequiredMixin,CreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'customer/create.html'
    success_url = reverse_lazy('customer-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    



def test(request):
    if request.method == 'POST':
        customer = CustomerCreateForm(request.POST)
        print('here')
        print(request.POST)
        if customer.is_valid():
            print('valid')
            customer.save()
            redirect('customer-home')
    else:
        customer = CustomerCreateForm()
    return render(request,'customer/create.html',{'customer':customer})