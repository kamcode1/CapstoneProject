from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer
    

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny] # Allow anyone to register
        else:
            self.permission_classes = [IsAuthenticated] # Authenticated users for other actions
        return super().get_permissions()
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
        # Buyers should only see their own profile
            if self.request.user.role == 'buyer':
                return User.objects.filter(id=self.request.user.id)
        return super().get_queryset()
        