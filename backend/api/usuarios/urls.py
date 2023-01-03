from rest_framework.routers import DefaultRouter

from .views import UsuariosViewSet

router = DefaultRouter()
router.register(r"", UsuariosViewSet, basename="usuarios")

usuarios_urls = router.urls
