from django.urls import path

from . import views

app_name = 'norilog'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('<int:pk>/update/', views.NorioriUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.NorioriDeleteView.as_view(), name='delete'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('save/', views.save, name='save'),
    path('guest/', views.guestlogin, name='guest'),
]
