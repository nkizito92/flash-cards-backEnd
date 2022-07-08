from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer

def showWordsList(request):
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)

def showWordDetail(request, pk):
    thisWord = Word.objects.get(id=pk)
    serializer = WordSerializer(thisWord, many=False)
    return Response(serializer.data)

def createWord(request):
    newWord = request.data
    # To create word type Word.objects.create()
    word = Word.objects.create(
        name=newWord['word']['name'], definition=newWord['word']['definition']
    )
    serializer = WordSerializer(word, many=False)
    # To debug first import pdb then from desired line type pdb.set_trace()
    return Response(serializer.data)

def updateWord(request, pk):
    data = request.data['word']
    # To get the specific object use objects.get(id=pk) "pk is Primary Key"
    word = Word.objects.get(id=pk)
    serializer = WordSerializer(instance=word, data=data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)

def deleteWord(request, pk): 
    word = Word.objects.get(id=pk)
    word.delete()
    return Response("Word Delete!!")