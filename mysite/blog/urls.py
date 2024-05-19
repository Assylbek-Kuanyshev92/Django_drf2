from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    # path('create/', views.PostCreateView.as_view()),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    ]

#
# urlpatterns = [
#     path('<int:post_id>/', views.index, name='index')
# ]

