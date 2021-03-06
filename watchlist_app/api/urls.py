from django.urls import path, include
# from watchlist_app.api.views import movie_detail, movie_list
from watchlist_app.api.views import ReviewList, ReviewDetail, WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
  path('list/', WatchListAV.as_view(), name="watch-list"),
  path('<int:pk>/', WatchDetailAV.as_view(), name="watch-detail"),
  path('stream/', StreamPlatformAV.as_view(), name="stream"),
  path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name="stream-detail"),
  path('review/', ReviewList.as_view(), name="review"),
  path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail")
]
