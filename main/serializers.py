from rest_framework import serializers
from datetime import timedelta
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Singer
        fields="__all__"


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields="__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields="__all__"

    def validate_file(self,value):
        if not value.endswith('.mp3'):
            raise serializers.ValidationError(
                "File should have .mp3 extension"
            )
        return value

    def validate_duration(self,value):
        if value > timedelta(minutes=7):
            raise serializers.ValidationError(
                "7 minutdan koproq bolmasin"
            )
        return value
