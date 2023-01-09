from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import MyTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user/', include('apps.user.api.urls'), name='user_principal_routes'),

    path('api/', include('apps.category.api.urls'), name='category_routes'),
    path('api/', include('apps.product.api.urls'), name='product_routes'),

    path('', TemplateView.as_view(template_name='index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]