from django.conf.urls import url, include
from colleges import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'colleges', views.CollegeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'attributes', views.AttributeViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]