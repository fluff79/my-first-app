from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item


# Create your views here.

def post_list(request):
    posts = Item.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request,'freezer/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Item, pk = pk)
    return render(request,'freezer/post_detail.html', {'post' : post})