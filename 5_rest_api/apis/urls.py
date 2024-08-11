from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import v1 as api

router = DefaultRouter()

api_v1_urls = (router.urls, 'apis.views.v1.urls')

urlpatterns = [
    path('v1/', include('apis.views.v1.urls'))

]
