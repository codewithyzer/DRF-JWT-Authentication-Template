from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenRefreshSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            json =  super().post(request, *args, **kwargs)
            
            access_token = json.data['access']
            refresh_token = json.data['refresh']
            
            response = Response()
            response.data = {'success': True}
            
            response.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            
            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            
            return response
        except:
            return Response({'success': False})
    
class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({'refreshed': False}, status=400)
            
            serializer = TokenRefreshSerializer(data={'refresh': refresh_token})
            serializer.is_valid(raise_exception=True)
            
            access_token = serializer.validated_data['access']
            
            response = Response()
            response.data = {'refreshed': True}
            
            response.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            
            return response
        except Exception as e:
            print("Refresh error:", e)
            return Response({'refresh': False}, status=400)
            
    
