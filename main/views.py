from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    category = Category.objects.all()
    return render(request,'index.html',{'cat':category})



class CategoryDetailView(DetailView):
	model = Category
	template_name = 'biologiya.html'


class ArticelDetailView(DetailView):
	model = Article
	template_name = 'detail.html'




def about(request):
    return render(request,'about.html')




