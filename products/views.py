from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils.timezone import now

from .forms import VacancyForm, CommentForm
from .models import Comment
from .models import Product, Category


def leave_request(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = VacancyForm()

    return render(request, 'ecommerce/vacancy_form.html', {'form': form})


def product_search(request):
    search_text = request.GET.get('search', '').strip()
    products = Product.objects.all()
    categories = Category.objects.all()
    prdctlst = []
    if search_text:
        for i in products:
            if i.name.lower().startswith(search_text.lower()):
                prdctlst.append(i)
    else:
        prdctlst.extend(products)

    return render(request, 'ecommerce/products_list.html', {
        'products': prdctlst,
        'categories': categories,
        'search_text': search_text,
        'search': True
    })



def products_list(request):
    category_filter = request.GET.get('category', '')
    products = Product.objects.all()

    if category_filter:
        products = products.filter(category__category=category_filter)

    categories = Category.objects.all()

    return render(request, 'ecommerce/products_list.html', {
        'products': products,
        'categories': categories,
        'category_filter': category_filter,
        'search': True
    })



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.comments.all()
    context = {
        "product": product,
        "reviews": reviews,
    }

    return render(request, "ecommerce/product_detail.html", context)


@login_required
def review_edit(request, pk, review_pk=None):
    product = get_object_or_404(Product, pk=pk)

    if review_pk:
        comment = get_object_or_404(Comment, pk=review_pk, product=product)
    else:
        comment = None

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.product = product
            new_comment.user_name = request.user.username
            new_comment.user_id = request.user.id
            new_comment.created_date = now()
            new_comment.save()
            return redirect('product_detail', pk=pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'ecommerce/review_form.html', {'form': form, 'product': product})
