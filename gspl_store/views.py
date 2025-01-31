from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Call the default implementation of the token view
        response = super().post(request, *args, **kwargs)
        
        # Get the access token from the response data
        access_token = response.data.get("access")
        
        # Customize the response format
        custom_response = {
            "access_token": access_token,
            "expires_in": 3600,  # You can customize this as needed
            "token_type": "Bearer",
        }

        return Response(custom_response, status=status.HTTP_200_OK)
