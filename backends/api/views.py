from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product

@csrf_exempt
def home(request):
    headers = request.headers
    params = request.GET.get('q')

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            price = data.get('price')
            description = data.get('description')
            if not all([name, price, description]):
                return JsonResponse({'error': 'Missing fields'}, status=400)
            product = Product.objects.create(name=name, price=price, description=description)
            return JsonResponse({'message': 'Product created successfully', 'product_id': product.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    elif request.method == 'GET':  # ✅ Gérer le GET séparément
        products = Product.objects.all().values('id', 'name', 'price', 'description', 'created_at', 'update_at')
        return JsonResponse(list(products), safe=False)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)