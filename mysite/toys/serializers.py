from rest_framework import serializers
from toys.models import Toy


class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    release_date = serializers.DateTimeField()
    toy_category = serializers.CharField(max_length=200)
    was_included_in_home = serializers.BooleanField(required=False)
    
    def create(self, validated_data):
        return Toy.objects.create(**validated_data)
    
    def update(self, instance, validated_date):
        instance.name = validated_date.get('name', instance.name)
        instance.description = validated_date.get('description', instance.description)
        instance.release_date = validated_date.get('release_date', instance.release_date)
        instance.toy_category = validated_date.get('toy_category', instance.toy_category)
        instance.was_included_in_home = validated_date.get('was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance