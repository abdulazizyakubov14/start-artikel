from django.urls import path
from.import views

app_name = 'languae'

urlpatterns = [
    path('',views.index, name='homes'),
    path("<int:pk>", views.CategoryDetailView.as_view(), name="cat_detail"),
    path("detail/<int:pk>", views.ArticelDetailView.as_view(), name="art_detail"),
    path("about/", views.about, name="abouts"),

]
