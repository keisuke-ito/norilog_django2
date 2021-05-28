from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='update'),
]
