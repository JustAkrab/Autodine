from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt decorator
from .models import Inventory, MenuItem
import json

@csrf_exempt  # Disable CSRF protection for this view
@require_POST
def check_feasible_items(request):
    """
    View to check the feasibility of menu items based on the current inventory.
    It expects a JSON payload with a dictionary where the keys are menu item names and the values are 
    dictionaries of additional ingredients (or empty if none).
    
    Example input:
    {
        "Burger": {"Cheese": 1, "Tomato": "-4-"},   # Extra 1 cheese on a burger, Exactly 4 Tomatoes
        "Fries": {}                # Standard fries
        "Biryani":{"Rice": 3, "Chicken": 2} # Extra 3 bowls of rice, Extra 2 chickens
    }
    
    Example output:
    {
        "Burger": {"feasible": False, "missing_ingredients": [{"ingredient": "Cheese", "required": 2, "available": 1}]},
        "Fries": {"feasible": True}
        "Biryani":{"feasible": True} 
    }
    """
    # Ensure the data is in JSON format
    try:
        json_req = json.loads(request.body)
        items = json_req['items']
        if not items:
            return JsonResponse({'error': 'Invalid data format or missing items key.'}, status=400)

        # Initialize response dictionary
        feasibility = {}

        # Get the current inventory instance (assuming you have only one inventory object)
        inventory = Inventory.objects.first()

        # Loop through each menu item in the input dictionary
        for item_name, additional_ingredients in items.items():
            # Check if the item is feasible in the inventory
            feasibility[item_name] = inventory.is_feasible(item_name, additional_ingredients)

        # Return the feasibility result as JSON
        return JsonResponse(feasibility, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
