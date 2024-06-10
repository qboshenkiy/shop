from django.shortcuts import render
from .models import products
# Create your views here.
def index(request):
    return render(request, 'index.html', context={'product': products.objects.all()})