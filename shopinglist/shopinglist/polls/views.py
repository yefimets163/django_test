from django.shortcuts import render
from django.http import HttpResponse
from polls.models import ShoppingList, UserList, MallList, Item

def index(request):
    user_list = UserList.objects.filter(user_id=1).first()
    result = ShoppingList.objects.filter(list_id=user_list.list_id)

    new_result = [itm.__dict__ for itm in result]
    return HttpResponse(str(new_result))

def add_item(request):
    return HttpResponse("Add Item")

def buy_item(request, item_id):
    return HttpResponse("Buy Item")

def remove_item(request, item_id):
    return HttpResponse("Remove Item")
