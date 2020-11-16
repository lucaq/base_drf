
from rest_framework import serializers
from operation.models import (
    Color,
    TagCategory,
    Tag,
    Group,
    User,
    UserRegisted,
)


class ColorSerializer(serializers.ModelSerializer):

    updated_at = serializers.SerializerMethodField()

    def get_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Color
        fields = ['id', 'rgb', 'remark', 'updated_at']


class TagCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TagCategory
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    updated_at = serializers.SerializerMethodField()

    def get_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        
    class Meta:
        model = Tag
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegistedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegisted
        fields = '__all__'
