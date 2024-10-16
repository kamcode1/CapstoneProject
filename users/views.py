from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer

# User Registration View
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Use the serializer to validate and create the user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user and hash the password
            user = serializer.save()

            # Debugging Step: Check if user is created
            print("User created:", user)

            # Generate JWT token for the new user
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            # Debugging Step: Check tokens
            print("Refresh Token:", refresh)
            print("Access Token:", access)

            return Response({
                'user': UserSerializer(user).data,  # Return user data
                'refresh': str(refresh),  # Return refresh token
                'access': str(access),  # Return access token
            }, status=status.HTTP_201_CREATED)
        
        # If serializer is invalid, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User ViewSet for managing user profiles
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]  # Allow anyone to register
        else:
            self.permission_classes = [IsAuthenticated]  # Authenticated users for other actions
        return super().get_permissions()
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Buyers should only see their own profile
            if self.request.user.role == 'buyer':
                return User.objects.filter(id=self.request.user.id)
        return super().get_queryset()
