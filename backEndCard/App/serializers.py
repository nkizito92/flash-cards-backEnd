from rest_framework import serializers
from App.models import Word
# You need this serializer to serialize the objects created from models
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'