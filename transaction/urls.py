from django.urls import path
from .views import CreateTransactionView, ChapaCallbackView

urlpatterns = [
    path('create/', CreateTransactionView.as_view(), name='create_transaction'),
    path('callback/', ChapaCallbackView.as_view(), name='chapa_callback'),  # Chapa callback endpoint
    path('webhook/', ChapaCallbackView.as_view(), name='chapa_webhook'),  # Chapa webhook endpoint
]
