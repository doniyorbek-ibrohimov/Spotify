#
#
# from rest_framework.response import Response
# from .serializers import *
# from rest_framework.views import APIView
# from rest_framework.generics import get_object_or_404
#
# class SingersAPIView(APIView):
#     def get(self,request):
#         singers=Singer.objects.all()
#         serializer=SingerSerializer(singers,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer=SingerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=400)
#
# class SingerRetrieveAPIView(APIView):
#     def get_object(self,pk):
#         return get_object_or_404(Singer,pk=pk)
#
#     def get(self,request,pk):
#         singer=self.get_object(pk)
#         serializer=SingerSerializer(singer)
#         return Response(serializer.data)
#
#     def put(self,request,pk):
#         singer=self.get_object(pk)
#         serializer=SingerSerializer(singer,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=400)
#
#     def delete(self,request,pk):
#         singer=self.get_object(pk)
#         singer.delete()
#         return Response(status=204)
#
#
#
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from .serializers import *


class AlbumModelViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


    @action(detail=True,methods=['get'],url_path='songs')
    def get_songs(self,request,pk):
        album=get_object_or_404(Album,pk=pk)
        songs=Song.objects.filter(album=album)
        serializer=SongSerializer(songs,many=True)
        return Response(serializer.data)


class SingerModelViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

    @action(detail=True, methods=['get'], url_path='albums')
    def get_album(self, request, pk):
        singer = get_object_or_404(Singer, pk=pk)
        albums = Album.objects.filter(singer=singer)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)


class SongModelViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer





