from django.urls import path
from.import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.index, name='home'),
    # path('<str:cat>',views.category_detail,name='cat_detail'),
    path("<int:id>", views.category_detail, name="detail"),
    path("about/", views.about, name="about")
]
