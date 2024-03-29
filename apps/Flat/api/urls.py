from rest_framework import routers
from .views import FlatsAPIViewSet

router = routers.DefaultRouter()

router.register(
    "flats",
    FlatsAPIViewSet
)

urlpatterns = router.urls
