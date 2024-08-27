from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.book.models import Tag 
from apps.book.serializers import TagSerializer


@api_view() # Define our http methods
def list_tags(request):
    # ORM
    tags = Tag.objects.all() # Complex Data type

    # DeSerialization
    data = TagSerializer(tags, many=True) # Convert complex data type to primitive Python types

    # Return JSOn
    return Response(data.data, status=status.HTTP_200_OK)