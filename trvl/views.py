from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    return render(request,'index.html',{'price':700,})