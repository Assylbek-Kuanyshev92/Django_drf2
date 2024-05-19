from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lookup_field = 'pk'


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=1)


class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save()

class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


# class PostCreateView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def perform_create(self, serializer):
#         # title = serializer.validated_data.get('title')
#         # content = serializer.validated_data.get('content', None)
#         # if content == "":
#         #     content = title
#         serializer.save(author_id=1)



# class PostListlView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
















#
#
# @api_view(['POST'])
# # @api_view(['GET', 'POST'])
# def index(request):
#
#     if request.method == 'POST':
#         # print(request.POST)
#         print(request.data)
#         instance = PostSerializer(data=request.data)
#
#         if instance.is_valid(raise_exception=True):
#             instance.save()
#             # post.author_id = 1
#             # post.save()
#             return Response(instance.data, status=status.HTTP_201_CREATED)
#         # return Response({"detail": "Error Creating", "status": status.HTTP_400_BAD_REQUEST})
#
#     elif request.method == 'GET':
#         post_id = request.GET.get('post_id')
#         if post_id is not None:
#             post = Post.objects.get(pk=post_id)
#             if post:
#                 instance = PostSerializer(post)
#                 return Response(instance.data)
#
#             return Response({"detail": "Post does not exist", "status": status.HTTP_404_NOT_FOUND})
#         else:
#             posts = Post.objects.all()
#             if posts:
#                 instance = PostSerializer(posts, many=True)
#                 return Response(instance.data)

# @api_view(['GET', 'POST'])
# def comment_list(request):
#     if request.method == 'GET':
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#



# if post:
#     data['id'] = post.id
#     data['title'] = post.title
#     data['content'] = post.content
#
# return JsonResponse(data)






