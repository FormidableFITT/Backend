from django.urls import path
from . import views

urlpatterns = [
    # path('', views.comment, name='comment'),
		path('', views.CommentView.as_view(), name='comment'),
]
