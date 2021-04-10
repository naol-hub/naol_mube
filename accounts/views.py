from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.

def home(request):
	orders = Order.objects.all()
	customer = Customer.objects.all()
	total_customers = customer.count()
	total_order = orders.count()
	deliver = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	dictionary ={'total_order':total_order, 'orders':orders, 'customer':customer, 'deliver':deliver,'pending':pending ,'total_customers': total_customers}

	return render(request,'accounts/dashboard.html', dictionary)

def products(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request,'accounts/products.html', context)

def customer(request,pk_test):
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()
	order_count = orders.count()

	dictionary ={'customer': customer,'orders': orders,'order_count':order_count}
	return render(request,'accounts/customer.html', dictionary)
def createOrder(request):
	form= OrderForm()
	if request.method=='POST':
		#print("print Post:",request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context= {'form': form}
	return render(request,'accounts/order_form.html', context)
def createupdate(request,pk):
	order = Order.object.get(id = pk)
	form= OrderForm(instance=order)
	if request.method=='POST':
		#print("print Post:",request.POST)
		form = OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
