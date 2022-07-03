import pdb
from telnetlib import WONT
import weakref
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from .serializers import WordSerializer
from django.conf import settings
from .models import Word
import json

# Create your views here.
@api_view(['GET'])
def getData(request):
    peps = Word.objects.all()
    serializer = WordSerializer(peps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWord(request, primaryKey):
    
    thisWord = Word.objects.get(id=primaryKey)
    serializer = WordSerializer(thisWord, many=False)
    return Response(serializer.data)
# Create a Word
@api_view(['POST'])
def addWord(request):
    newWord = request.data
    word = Word.objects.create(
        name=newWord['word']['name'], definition=newWord['word']['definition']
    )
    serializer = WordSerializer(word, many=False)
    # To debug first import pdb then from desired line type pdb.set_trace()
    return Response(serializer.data)
#Update View
@api_view(['PATCH'])
def updateWord(request, pk):
    data = request.data['word']
    # To get the specific object use objects.get(id=pk) "pk is Primary Key"
    word = Word.objects.get(id=pk)
    serializer = WordSerializer(instance=word, data=data)
    if serializer.is_valid():
      serializer.save() 
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteWord(request, pk):
    word = Word.objects.get(id=pk)
    word.delete()
    return Response("Delete {word.name}")
