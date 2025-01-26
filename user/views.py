from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from order.models import Order
from django.db.models import Sum
from datetime import datetime

def home_view(request):
    orders = Order.objects.filter(customer__user = request.user,date = datetime.today())
    filter_date = request.GET.get('filter_date')
    print(filter_date)

    if filter_date:
        try:
            filter_date = datetime.strptime(filter_date,'%Y-%m-%d').date()
            print(filter_date)
            orders = Order.objects.filter(customer__user = request.user,date = filter_date)
        except ValueError:
            return render(request,'home/home.htm',{'orders':orders})
    spent = sum(order.price for order in orders)
    print(orders)
    return render(request,'home/home.html',{'orders':orders,'spent':spent})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = UserRegisterForm()
        return render(request,'user/register.html',{'form':form})
