from rest_framework import serializers
from .models import Clothing

class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['version', 'type', 'serial_no', 'rating', 'quantity']
