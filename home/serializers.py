from rest_framework import serializers
from .models import Person, Color


class ColorSerializer(serializers.ModelSerializer):
    hex = serializers.SerializerMethodField()
    class Meta:
        model = Color
        fields = ['id','color_name', 'hex']

    def get_hex(self, obj):
        return "#000"



class PersonSerializer(serializers.ModelSerializer):
    fav_color = serializers.PrimaryKeyRelatedField(queryset = Color.objects.all())

    class Meta:
        model = Person
        fields = ['id','name', 'age', 'fav_color']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['fav_color'] = ColorSerializer(instance.fav_color).data
        return representation
    

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('age should be greater than 18')
        return age
    
    def validate_name(self, name):
        if not name.isalnum():
            raise serializers.ValidationError('name can not contain special characters')
        return name


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()