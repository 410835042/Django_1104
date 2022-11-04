from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BrandForm, LoginForm, RegisterForm, UpdateForm, consumer_updateForm, HandSizeForm, CartForm  # RawPartnerForm
from .models import Brand, Account, Cart, HandSize
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def brand_create_view(request):
    if request.method == 'POST':
        form = BrandForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account = request.user
            instance.save()
            # form.save()
            # form = PartnerForm()
        context = {
            'state': "更新品牌",
            'form': form
        }
    else:
        form = BrandForm()
        context = {
            'state': "新增品牌",
            'form': form
        }
    return render(request, "partners/partner_create.html", context)


def brand_delete_view(request, b_id):
    obj = get_object_or_404(Brand, id=b_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "partners/partner_delete.html", context)


def brand_update_view(request, b_id):
    obj = get_object_or_404(Brand, id=b_id)
    form = BrandForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'state': "更新品牌",
        'form': form
    }
    return render(request, "partners/partner_create.html", context)


def brand_list_view(request):
    queryset = Brand.objects.all()  # list of objects
    context = {
        "object_list": queryset,
    }
    return render(request, "partners/partner_list.html", context)


def brand_detail_view(request, b_id):
    obj = Brand.objects.get(id=b_id)
    context = {
        'object': obj
    }
    return render(request, "partners/partner_detail.html", context)


# USER相關
def sign_up_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../index/')
    context = {
        'state': "註冊",
        'form': form
    }
    return render(request, 'partners/partner_signup.html', context)


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 內建的登入
            return redirect('../')  # 重新導向到索引頁
        else:
            messages.warning(request, '登入失敗')

    context = {
        'form': form
    }
    return render(request, 'partners/partner_login.html', context)


def index_view(request):
    return render(request, 'partners/partner_index.html')


def information_view(request):
    user = request.user
    size_list = HandSize.objects.all()
    # size = HandSize.objects.get(account_id=user.id)
    form = RegisterForm(request.POST or None, instance=user)
    queryset = Account.objects.all()
    messages.warning(request, '注意！登出前請先妥善存檔')
    context = {
        'form': form,
        'user_list': queryset,
        'size_list': size_list,
        # 'size': size,
    }
    return render(request, 'partners/partner_information.html', context)


def update(request):
    user = request.user
    if user.identity == 0:
        consumer_form = consumer_updateForm(request.POST or None, instance=user)
        if request.method == "POST":
            if consumer_form.is_valid():
                consumer_form.save()
                return redirect('../')
        context = {
            'state': "更新資料",
            "form": consumer_form
        }
    elif user.identity == 1:
        partner_form = UpdateForm(request.POST or None, instance=user)
        if request.method == "POST":
            if partner_form.is_valid():
                partner_form.save()
                return redirect('../')
        context = {
            'state': "更新資料",
            "form": partner_form
        }
    return render(request, 'partners/partner_update.html', context)


def cart_view(request):
    queryset = Cart.objects.all()
    context = {
        "cart": queryset
    }
    return render(request, 'partners/partner_cart.html', context)


def cart_delete_view(request, c_id):
    obj = Cart.objects.get(id=c_id)
    # if request.method == "POST":
    obj.delete()
    return redirect('../../cart')
    # context = {
    #     "object": obj
    # }
    # return render(request, 'partners/partner_cart_delete.html', context)


def logout_view(request):
    logout(request)  # 內建的登出
    return redirect('../index')


def delete_user(request):
    request.user.delete()
    return redirect('../index')

