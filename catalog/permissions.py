from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions
from datetime import datetime, timezone
from rest_framework import permissions
import jwt
from rest_framework.exceptions import PermissionDenied
class AnonReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow full access to authenticated users,
    and read-only access to unauthenticated users. 
    Additionally, flag if the JWT has expired.
    """

    def has_permission(self, request, view):
        # If the method is safe (GET, HEAD, OPTIONS), allow read-only access
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the user is authenticated
        if request.user and request.user.is_authenticated:
            # If the user is authenticated, check if the access token has expired
            token = request.headers.get('Authorization', '').split(' ')[-1]
            if token:
                try:
                    # Decode the JWT token to get the expiration time
                    decoded_token = jwt.decode(token, options={"verify_signature": False})
                    expiration_time = decoded_token.get('exp')
                    if expiration_time:
                        # Convert expiration time from UTC to local time
                        expiration_time = datetime.fromtimestamp(expiration_time, timezone.utc)
                        current_time = datetime.now(timezone.utc)
                        
                        # If the token is expired, raise PermissionDenied
                        if current_time > expiration_time:
                            raise PermissionDenied("Token has expired. Please authenticate again.")
                        
                        return True
                except jwt.ExpiredSignatureError:
                    raise PermissionDenied("Token has expired. Please authenticate again.")
                except jwt.JWTError:
                    raise PermissionDenied("Invalid token.")
        # Default case: Deny if user is not authenticated
        return False