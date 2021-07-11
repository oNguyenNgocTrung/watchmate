from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer

class StreamPlatformAV(APIView):
  def get(self, request):
    stream_platforms = StreamPlatform.objects.all()
    serializers = StreamPlatformSerializer(stream_platforms, many=True)
    return Response(serializers.data)

  def post(self, request):
    serializer = StreamPlatformSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
  def get(self, request, pk):
    try:
      stream_platform = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
      return Response({"error": "StreamPlatform not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StreamPlatformSerializer(stream_platform)
    return Response(serializer.data)

  def put(self, request, pk):
    try:
      stream_platform = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
      return Response({"error": "StreamPlatform not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StreamPlatformSerializer(stream_platform, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    try:
      stream_platform = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
      return Response({"error": "StreamPlatform not found"}, status=status.HTTP_404_NOT_FOUND)

    stream_platform.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):
  def get(self, request):
    watch_lists = WatchList.objects.all()
    serializers = WatchListSerializer(watch_lists, many=True)
    return Response(serializers.data)

  def post(self, request):
    serializer = WatchListSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

class WatchDetailAV(APIView):
  def get(self, request, pk):
    try:
      watch_list = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
      return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = WatchListSerializer(watch_list)
    return Response(serializer.data)

  def put(self, request, pk):
    try:
      watch_list = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
      return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = WatchListSerializer(watch_list, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    try:
      watch_list = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
      return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    watch_list.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):
#   if request.method == 'GET':
#     movies = Movie.objects.all()
#     serializers = MovieSerializer(movies, many=True)
#     return Response(serializers.data)
#   elif request.method == 'POST':
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#   try:
#     movie = Movie.objects.get(pk=pk)
#   except Movie.DoesNotExist:
#     return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

#   if request.method == 'GET':
#     serializer = MovieSerializer(movie)

#     return Response(serializer.data)
#   elif request.method == 'PUT':
#     serializer = MovieSerializer(movie, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#   elif request.method == 'DELETE':
#     movie.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
