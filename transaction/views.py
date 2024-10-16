from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction
from .serializers import TransactionSerializer
import requests
from django.shortcuts import get_object_or_404

class CreateTransactionView(APIView):
    """
    This view handles transaction initialization with Chapa.
    """
    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.id  # Set the user based on the request

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()

            # Chapa API URL
            chapa_url = "https://api.chapa.co/v1/transaction/initialize"

            # Payload for Chapa API
            payload = {
                'amount': str(transaction.amount),
                'currency': 'ETB',
                'email': transaction.user.email,
                'tx_ref': transaction.reference,
                'callback_url': 'http://127.0.0.1:8000/api/transactions/callback/',  # Local callback for development
                'return_url': 'http://127.0.0.1:3000/success',  # Local frontend URL for development success page
            }

            # Headers for Chapa API
            headers = {
                "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
            }

            # Send request to Chapa
            response = requests.post(chapa_url, json=payload, headers=headers)

            # Handle Chapa response
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            else:
                # Update transaction status to failed
                transaction.status = Transaction.FAILED
                transaction.save()
                return Response({"error": "Transaction failed with Chapa", "details": response.json()}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChapaCallbackView(APIView):
    """
    This view handles the callback from Chapa to update the transaction status.
    """
    def post(self, request, *args, **kwargs):
        reference = request.data.get('tx_ref')
        transaction = get_object_or_404(Transaction, reference=reference)

        # Validate Chapa transaction status (from their callback)
        chapa_status = request.data.get('status')

        if chapa_status == 'success':
            transaction.status = Transaction.SUCCESS
        else:
            transaction.status = Transaction.FAILED

        transaction.save()
        return Response({'message': 'Transaction status updated'}, status=status.HTTP_200_OK)


