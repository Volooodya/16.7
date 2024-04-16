from django.urls import path
from .views import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),  # Добавили эту строчку
    path("products/", include("simpleapp.urls")),
]


from rest_framework import routers
from education import views


router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewset)
router.register(r'classes', views.SClassViewset)
router.register(r'students', views.StudentViewest)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]