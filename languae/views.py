from django.shortcuts import render,get_object_or_404
from languae.models import *
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    category = Categorys.objects.all()
    return render(request,'russian/index.html',{'cat':category})



class CategoryDetailView(DetailView):
	model = Categorys
	template_name = 'russian/biologiya.html'


class ArticelDetailView(DetailView):
	model = Articles
	template_name = 'russian/detail.html'


def about(request):
    return render(request,'russian/about.html')

