
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from school import views

urlpatterns = [
    path('home/', views.home),
    path('mylist/', views.MyList.as_view()),
    path('notice/', views.NoticeListView.as_view()),
    path('question/create/', views.QuestionCreate.as_view(success_url="/school/home"), name=''),
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/school/home/")),
    path('notice/<int:pk>/', views.NoticeDetailView.as_view()),
    path('', RedirectView.as_view(url='home/')),
]
