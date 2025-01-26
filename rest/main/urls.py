from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, OrderAdd, ProductEdit
from django.urls import path, include

router = SimpleRouter()
router.register('api/product', ProductViewSet)

urlpatterns = [
    path('api/order-add', OrderAdd.as_view(), name='order-add'),
    path('api/product/<slug:slug>', ProductEdit.as_view(), name='product-edit'),
]

urlpatterns += router.urls
