from rest_framework.authentication import TokenAuthentication

class TokenAuthenticationCustom(TokenAuthentication):
    keyword = 'Bearer'