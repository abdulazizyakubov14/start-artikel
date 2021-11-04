from django.urls import path
from.import views

app_name = 'main'

urlpatterns = [
    path('',views.index, name='home'),
    # path('<str:cat>',views.category_detail,name='cat_detail'),
    path('detail/<pk>',views.DetailPageView.as_view(),name='articel_detail'),
    path('category/<slug:category_slug>/', views.categoryDetail,name='category_detail'),
    path("about/", views.about, name="about"),

]
