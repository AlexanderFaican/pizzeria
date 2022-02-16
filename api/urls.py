from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
##from api.core.legal import views
from api import views
router = DefaultRouter()

router.register('allHorario', views.HorarioSet)
urlpatterns = [
    path(r'^', include(router.urls)),
    ##url(r'^API/', views.MovieDocumentViewSet.as_view()),
    ##url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
