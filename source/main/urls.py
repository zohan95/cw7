"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollView.as_view(), name='poll_url'),
    path('poll/<int:pk>/', PollDetails.as_view(), name='poll_details_url'),
    path('poll/edit/<int:pk>/', PollEdit.as_view(), name='poll_edit_url'),
    path('poll/delete/<int:pk>/', PollDelete.as_view(), name='poll_delete_url'),
    path('poll/create/', PollCreate.as_view(), name='poll_create_url'),
    path('poll/<int:pk>/create/', ChoiceCreate.as_view(), name='choice_create_url'),
    path('choice/edit/<int:pk>/', ChoiceEdit.as_view(), name='choice_edit_url'),
    path('choice/delete/<int:pk>/', ChoiceDelete.as_view(), name='choice_delete_url'),
    path('answer/<int:pk>/', AnswerView.as_view(), name='answer_view'),
    path('stat/<int:pk>/', StatView.as_view(), name='stat_url')
]
