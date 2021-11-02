from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

def index(request):
    category = get_object_or_404(Category, slug=category_slug)
    language = request.LANGUAGE_CODE
    category = get_object_or_404(Category,
        translations__language_code=language,
        translations__slug=category_slug)
    return render(request,'index.html',{'cat':category})