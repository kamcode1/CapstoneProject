from django.http import JsonResponse

# Create your views here.
def api_overview(request):
    return JsonResponse({
        'message': 'Welcome to the E-commerce API!',
        'endpoints':{
            'users': '/api/users/',
            'products': '/api/products/',
            'token_obtain': '/api/token',
            'token_refresh': '/api/token/refresh/',
        },
        'description': 'This API allows you to manage users, products, and handle authentication via JWT tokens.',
    })