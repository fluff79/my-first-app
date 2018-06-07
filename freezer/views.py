from datetime import date
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import ItemForm, ShoppinglistForm
from .models import Item, Shopping_list

three_months = date.today() + relativedelta(months =+3)
# Create your views here.

def index(request):
    return render(request, 'freezer/index.html')

def post_list(request):
    posts = Item.objects.exclude(where = 10).order_by('expires_date')
    return render(request,'freezer/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Item, pk = pk)
    return render(request,'freezer/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.added_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ItemForm(initial = {'expires_date': three_months })
    return render(request, 'freezer/post_new.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ItemForm(instance=post)
    return render(request, 'freezer/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Item, pk=pk)
    post.delete()
    return redirect('post_list')

def shopping_list(request):
    shopping_list_items = Item.objects.filter(on_shopping_list=True).order_by('added_date')
    return render(request,'freezer/shopping_list.html', {'shopping_list_items' : shopping_list_items})

def shopping_list_detail(request, pk):
    shopping_list_item = get_object_or_404(Item, pk = pk)
    return render(request,'freezer/shopping_list_detail.html', {'shopping_list_item' : shopping_list_item})

def shopping_list_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.added_date = timezone.now()
            post.save()
            return redirect('shopping_list') 
    else:
        form = ItemForm(initial = {'on_shopping_list': True, 'where': 10 })
    return render(request, 'freezer/shopping_list_new.html', {'form' : form})

def shopping_list_edit(request, pk):
    shopping_list_item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=shopping_list_item)
        if form.is_valid():
            shopping_list_item = form.save(commit=False)
            shopping_list_item.author = request.user
            shopping_list_item.save()
            return redirect('shopping_list_detail', pk=shopping_list_item.pk)
    else:
        form = ItemForm(instance=shopping_list_item)
    return render(request, 'freezer/shopping_list_edit.html', {'form': form})

def shopping_list_remove(request, pk):
    shopping_list_item = get_object_or_404(Item, pk=pk)
    shopping_list_item.delete()
    return redirect('shopping_list')

# def post_add_to_shopping_list(request, pk):
#     post = get_object_or_404(Item, pk=pk)
#     Shopping_list(title = post.title)
#     return redirect('shopping_list')
