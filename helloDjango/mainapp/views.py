from django.http import HttpResponse
from django.shortcuts import render, redirect
from mainapp.models import UserEntity

# Create your views here.
# 用户列表
def user_list1(request):
    users = UserEntity.objects.all()
    msg = '最好的学员'
    return render(request, 'user/list.html',{"users":users,"msg":msg})

# 添加用户
def add_user(request):
    user = UserEntity()
    # request.GET是一个字典类型,保存的是查询参数
    name = request.GET.get("name",None)
    age = request.GET.get("age", 0)
    phone = request.GET.get("phone", None)
    # 验证数据是否完整
    if not all((name,age,phone)):
        return HttpResponse('<h3 style="color:red>请求参数不完整</h3>', status=400)
    user.name = name
    user.age = age
    user.phone = phone
    user.save()
    return redirect('/user/1')


# 删除用户
def del_user(request):
    user = UserEntity.objects.get(pk=2)
    user.delete()
    return redirect('/user/1')


# 更新用户
def update_user(request):
    # 查询参数有id，name，phone
    # 通过模型查询id用户是不是存在  model.objects.get可能会报异常
    id = request.GET.get("id", None)
    if not id:
        return HttpResponse('<h3 style="color:red>id必须要提供</h3>', status=400)
    try:
        user = UserEntity.objects.get(pk=int(id))
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        if any((name, phone)):
            if name:
                user.name = name
            if phone:
                user.phone = phone
            user.save()
            return redirect('/user/1')
    except:
        return HttpResponse('<h3 style="color:red>id用户不存在</h3>', status=400)


def update_post(request):
    # TODO
    pass


def qas(request):
    pass


def sdawd(request):
    pass