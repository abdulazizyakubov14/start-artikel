from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    category = Category.objects.all()
    # category = get_object_or_404(Category,
    #     translations__language_code=language,
    #     translations__slug=category_slug)

    return render(request,'index.html',{'cat':category})

def category_detail(request,id):
    category = Category.objects.get(id=id)

    return render(request,'biologiya.html',{'cat':category})


# class DetailPage(DetailView):
#     model = Category
#     fields = ['__all__']
#     template_name = 'biologiya.html'


def about(request):
    return render(request,'about.html')