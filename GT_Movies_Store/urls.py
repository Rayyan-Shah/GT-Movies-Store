from . import views
from django.urls import path
app_name = 'GT_Movies_Store'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),


]