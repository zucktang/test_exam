from rest_framework import viewsets, status
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response

from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


class APIMixin:
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    
    def get_serializer_class(self):
        return self.ACTION_SERIALIZERS.get(self.action)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        read_serializer = self.serializer_class(instance)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        message = {"message": f"{instance.__class__.__name__} deleted successfully"}
        return Response(message, status=status.HTTP_204_NO_CONTENT)


    
    
    