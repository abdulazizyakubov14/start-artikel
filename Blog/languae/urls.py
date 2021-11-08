from django.urls import path
from.import views

app_name = 'languae'

urlpatterns = [
    path('',views.index, name='homes'),
    path("<int:pk>", views.CategoryDetailView.as_view(), name="cat_detail"),
    path("detail/<int:pk>", views.ArticelDetailView.as_view(), name="art_detail"),
    # path('<str:cat>',views.category_detail,name='cat_detail'),
    # path('<int:id>/<slug:slug>/',views.articel,name='articel_detail'),
    # path('category/<slug:category_slug>/', views.categoryDetail,name='category_detail'),
    path("about/", views.about, name="abouts"),

]
