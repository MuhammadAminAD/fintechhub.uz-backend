from rest_framework import serializers
from .models import (
    Course,
    Teacher,
    Partner,
    BannerImage,
    CourseDescription,
    CourseIcon,
    CourseDescriptionGroup,
)

class CourseDescriptionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDescriptionGroup
        fields = "__all__"

class CourseDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDescription
        fields = "__all__"


class CourseIconSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CourseIcon
        fields = ["id", "icon", "course_id"]


class CourseSerializer(serializers.ModelSerializer):
    icons = CourseIconSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    descriptions = serializers.SerializerMethodField()
    icons = CourseIconSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_descriptions(self, obj):
        description_groups = obj.description_groups.all()
        result = []
        for group in description_groups:
            descriptions = group.descriptions.all()
            description_serializer = CourseDescriptionSerializer(
                descriptions, many=True
            )
            result.append(
                {
                    "group_title": group.title,
                    "descriptions": description_serializer.data,
                }
            )
        return result


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = "__all__"
