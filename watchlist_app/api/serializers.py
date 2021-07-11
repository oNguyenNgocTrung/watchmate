from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
  class Meta:
    model = WatchList
    fields = "__all__"

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(
    view_name='stream-detail',
    lookup_field='pk'
  )

  watchlist = WatchListSerializer(many=True, read_only=True)
  class Meta:
    model = StreamPlatform
    fields = "__all__"


# class MovieSerializer(serializers.ModelSerializer):
#   len_name = serializers.SerializerMethodField()
#   class Meta:
#     model = Movie
#     fields = "__all__"
#     # fields = ['id', 'name', 'description']

#   def get_len_name(self, obj):
#     return len(obj.name)

#   def validation_data(self, data):
#     if len(data["name"]) == len(data["description"]):
#       raise serializers.ValidationError("Name and descriptions should be different!")
#     else:
#       return data

#   def validate_name(self, value):
#     if len(value) <= 2:
#       raise serializers.ValidationError("Name is too short")
#     else:
#       return value

# def name_length(value):
#   if len(value) <= 2:
#     raise serializers.ValidationError("Name is too short")

# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators=[name_length])
#   description = serializers.CharField()
#   active = serializers.BooleanField()

#   def create(self, validated_data):
#     return Movie.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.description = validated_data.get('description', instance.description)
#     instance.active = validated_data.get('active', instance.active)
#     instance.save()
#     return instance


#   def validation_data(self, data):
#     if len(data["name"]) == len(data["description"]):
#       raise serializers.ValidationError("Name and descriptions should be different!")
#     else:
#       return data

  # def validate_name(self, value):
  #   if len(value) <= 2:
  #     raise serializers.ValidationError("Name is too short")
  #   else:
  #     return value
