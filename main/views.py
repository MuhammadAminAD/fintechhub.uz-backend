from rest_framework import viewsets
from .models import (
    Course,
    Teacher,
    Partner,
    BannerImage,
    CourseDescription,
    CourseIcon,
    CourseDescriptionGroup,
)
from .serializers import (
    CourseSerializer,
    TeacherSerializer,
    PartnerSerializer,
    BannerImageSerializer,
    CourseDescriptionSerializer,
    CourseIconSerializer,
    CourseDescriptionGroupSerializer,
    CourseDetailSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer


class CourseDescriptionGroupView(viewsets.ModelViewSet):
    queryset = CourseDescriptionGroup.objects.all()
    serializer_class = CourseDescriptionGroupSerializer


class CourseDescriptionViewSet(viewsets.ModelViewSet):
    queryset = CourseDescription.objects.all()
    serializer_class = CourseDescriptionSerializer


class CourseIconViewSet(viewsets.ModelViewSet):
    queryset = CourseIcon.objects.all()
    serializer_class = CourseIconSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class BannerImageViewSet(viewsets.ModelViewSet):
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer
