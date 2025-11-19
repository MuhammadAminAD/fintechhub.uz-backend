from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    CourseDescriptionViewSet,
    CourseIconViewSet,
    TeacherViewSet,
    PartnerViewSet,
    BannerImageViewSet,
    CourseDescriptionGroupView
)

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r"course-descriptions", CourseDescriptionViewSet)
router.register(r"course-icons", CourseIconViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"partners", PartnerViewSet)
router.register(r"banners", BannerImageViewSet)
router.register(r"course-description-group", CourseDescriptionGroupView)

urlpatterns = [
    path("", include(router.urls)),
]
