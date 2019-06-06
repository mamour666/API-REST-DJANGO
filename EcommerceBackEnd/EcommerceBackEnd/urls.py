
from django.contrib import admin
from django.urls import path, include
from api.resources import ProductResource
from api.resources import CategoryResource
from api.resources import OrderResource
from django.conf.urls.static import static
from django.conf import settings


product_resource = ProductResource()
category_resource = CategoryResource()
order_resource = OrderResource()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(product_resource.urls)),
    path('api/',include(category_resource.urls)),
    path('api/',include(order_resource.urls)),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
