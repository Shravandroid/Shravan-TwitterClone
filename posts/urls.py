from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('edit/<int:post_id>/cancel', views.cancel, name='cancel'),
    path('like/<int:post_id>/', views.like, name='like')

]