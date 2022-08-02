from rest_framework import serializers
from App.models import Word
# You need this serializer to serialize the objects created from models
# Also to create json objects out of python
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'