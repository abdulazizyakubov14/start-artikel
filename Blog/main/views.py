from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    category = Category.objects.all()
    return render(request,'index.html',{'cat':category})

# def categoryDetail(request,category_slug):
# 	category = get_object_or_404(Category,slug=category_slug)
# 	articels = Article.objects.filter(category=category)
# 	context = {
# 		'articels':articels
# 	}
# 	return render(request, 'biologiya.html', context)

class CategoryDetailView(DetailView):
	model = Category
	template_name = 'biologiya.html'


class ArticelDetailView(DetailView):
	model = Article
	template_name = 'detail.html'

def img(request):
	img = Category.objects.all()
	return render(request,'biologiya.html',{'imgs':img})


def about(request):
    return render(request,'about.html')

# class DetailPageView(DetailView):
#     model = Article
#     template_name = 'detail.html'
def articel(request,id,slug):
	language = request.LANGUAGE_CODE
	product = get_object_or_404(Article,
 		id=id,
 		translations__language_code=language,
 		translations__slug=slug,
 	)
	return render(request,'detail.html',{'object':product})