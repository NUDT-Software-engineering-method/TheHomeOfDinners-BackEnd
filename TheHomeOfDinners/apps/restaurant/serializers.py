import re

from rest_framework import serializers

from restaurant.models import Restaurant, Tag, Collection, Menu, Review


class RestaurantSerializer(serializers.ModelSerializer):
    # 餐馆序列化器

    # 添加收藏数字段
    collection_count = serializers.SerializerMethodField(label='收藏数')

    # picture = serializers.ImageField(
    #     max_length=None, use_url=True, allow_null=True, required=False)

    # foods = serializers.CharField(label='菜品', read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'

    def get_collection_count(self, obj):
        """获取餐馆的收藏数"""
        count = obj.restaurant_collection.count()
        return count

    def validate_mobile(self, value):
        """单独校验手机号"""
        if not re.match(r'1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式有误')
        return value

    def create(self, validated_data):
        # 设置默认审核状态为未审核
        validated_data['verify'] = '0'
        restaurant = Restaurant(**validated_data)
        restaurant.save()
        return restaurant


class TagSerializer(serializers.ModelSerializer):
    # 标签序列化器
    class Meta:
        model = Tag
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    # 收藏序列化器
    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ['datetime']


class MenuSerializer(serializers.ModelSerializer):
    # 菜单序列化器
    class Meta:
        model = Menu
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    # 评论序列化器
    class Meta:
        model = Review
        fields = '__all__'
