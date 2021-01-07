from .models import Post
from .Serializer import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_posts=Post.objects.all()
    data=PostSerializer(all_posts ,many=True).data
    return Response({'data':data})




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail_api(request,pk):
    post=Post.objects.get(id=pk)
    data=PostSerializer(post).data 
    return Response({'data':data})



@api_view(['GET'])
def post_search_api(request,q):
    posts=Post.objects.filter(
        Q(title__icontains=q)|
        Q(description__icontains=q)
    )
    data=PostSerializer(posts ,many=True).data
    return Response({'data':data})
