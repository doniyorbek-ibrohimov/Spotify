from argparse import Action

from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class SingersAPIView(APIView):
    def get(self,request):
        singers=Singer.objects.all()
        serializer=SingerSerializer(singers,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=SingerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

class SingerRetrieveAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Singer,pk=pk)

    def get(self,request,pk):
        singer=self.get_object(pk)
        serializer=SingerSerializer(singer)
        return Response(serializer.data)

    def put(self,request,pk):
        singer=self.get_object(pk)
        serializer=SingerSerializer(singer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    def delete(self,request,pk):
        singer=self.get_object(pk)
        singer.delete()
        return Response(status=204)



