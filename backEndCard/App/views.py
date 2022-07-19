import pdb
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .utils import showWordsList, updateWord, showWordDetail, deleteWord, createWord
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
# how to customize your token claims
# use jwt.io to view json data about from the access token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/token',
        'token/refresh'
    ]
    return Response(routes)

# adding permissions for Authenticating
@api_view(['GET','POST'])   
@permission_classes([IsAuthenticated])
def wordRequest(request):
    # grabbing the user's input
    if(request.method == 'GET'):
     return showWordsList(request)
    # Post Request
    if(request.method == 'POST'):
     return createWord(request)

@api_view(['POST'])
def creatingUser(request):
    if(request.method == "POST"):
        return createUser(request)

   
@api_view(['GET','PATCH','DELETE'])
def wordChangeRequest(request, pk):
    # Show Word Details
     if(request.method == 'GET'):
        return showWordDetail(request, pk)
    # Update Request
     if(request.method == 'PATCH'):
       return updateWord(request, pk)
    # Delete request
     if(request.method == 'DELETE'):
        return deleteWord(request, pk)
