from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    # 因为django-allauth默认会在templates/account/文件夹下寻找模板文件，为了方便后续集中美化模板也将模板文件放到该文件夹下
    return render(request, 'account/profile.html', {'user': user})


@login_required
def profile_update(request):
    user = request.user
    # get_object_or_404用特定查询条件获取某个对象，成功则返回该对象，否则引发一个Http404
    # 在这里只有新注册的用户才会显示该视图函数渲染的内容，之前命令创建的超级管理员不在UserProfile中，所以查询不到
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        # form 包含提交的数据
        form = ProfileForm(request.POST)
        #  is_valid() 方法来运行验证并返回一个指定数据是否有效的布尔值，也就是判断值是否都正确
        if form.is_valid():
            # form.cleaned_data[]来获取vaild验证后的值，
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.save()
            # 重定向到信息展示页面
            return HttpResponseRedirect(reverse('myaccount:profile'))
    else:
        # 如果没有更新数据的话，则显示原来的数据
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,
                        'org': user_profile.org, 'telephone': user_profile.telephone, }
        form = ProfileForm(default_data)

    return render(request, 'account/profile_update.html', {'form': form, 'user': user})



