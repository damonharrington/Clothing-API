from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from results.models import Clothing
from .serializers import ClothingSerializer
'''
class ClothingSection(APIView):
    def get(self,request,serial_no, version):
        try:
            Clothing = Clothing.objects.get(serial_no=serial_no, version=version)
            serializer = ClothingSerializer(Clothing)
            return Response(serializer.data)
        except Clothing.DoesNotExist:
            return Response({"message": "Clothes not found"}, status=status.HTTP_404_NOT_FOUND)
'''
class ClothingSection(APIView):
    def get(self, request, *args, **kwargs):
        version = self.kwargs.get('version')
        type = self.kwargs.get('type')
        try:
            Clothing = Clothing.objects.get(version=version, type=type)
            serializer = ClothingSerializer(Clothing)
            return Response(serializer.data)
        except Clothing.DoesNotExist:
            return Response({"message": "Player not found"}, status=status.HTTP_404_NOT_FOUND)