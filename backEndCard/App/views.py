import pdb
from django.shortcuts import render
from rest_framework.decorators import api_view
from .utils import showWordsList, updateWord, showWordDetail, deleteWord, createWord

# Create your views here.

@api_view(['GET','POST'])    
def wordRequest(request):
    if(request.method == 'GET'):
     return showWordsList(request)
    # Post Request
    if(request.method == 'POST'):
     return createWord(request)
   
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
