from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from quickstart.serializers import UserSerializer, GroupSerializer,PostSerializer
from .models import *


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""
    queryset = Post.objects.all().order_by('created')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Post.objects.get(id=id)
            serializer = PostSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = Post.objects.all()
        serializer = PostSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Post.objects.get(id=id)
        serializer = PostSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data})
        else:
            return Response({'status':'error', 'data': serializer.errors})
    
    def delete(self, request, id=None):
        item = get_object_or_404(Post, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

def post_view(request):
    qs= Post.objects.all()
    user = request.user

    context = {
        'qs': qs,
        'user' : user,
    }
    return render(request, 'quickstart/main.html', context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else: 
                like.value = 'Like'
        like.save()

    return redirect('quickstart:post_list')
