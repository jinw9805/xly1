from django.shortcuts import render
from apps.users.models import UserProfile
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, QueryDict


# Create your views here.
class UserMangerView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        username = request.GET.get('keyword', '')
        # test = UserProfile.objects.filter(username='liyongli',)
        # filter 结果 < QuerySet[ < UserProfile: liyongli >] >
        # print(test)
        all_user_info = []
        user_group = []
        if username:
            # 搜索用户
            user_info = UserProfile.objects.all().values('username', 'name_cn', 'groups__name', 'phone', 'is_active'). \
                filter(username=username).first()
        else:
            all_user = UserProfile.objects.all().values('username')
            for user in all_user:
                # 获取全部用户信息
                user_info = UserProfile.objects.all().values('username', 'name_cn', 'groups__name', 'phone',
                                                             'is_active').filter(username=user['username'])
                # 如果长度不为1证明用户属于多个组
                if len(user_info) != 1:
                    for users in user_info:
                        # 获取用户所在的全部组
                        user_group.append(users['groups__name'])
                    # 将多用户组数据写入用户信息
                    user_info[0]['groups__name'] = user_group
                # 将用户数据加入列表
                all_user_info.append(user_info[0])
        return render(request, 'user/userlist.html', {'user_info': all_user_info})


class UserUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        user_info = UserProfile.objects.all().values('username', 'name_cn', 'phone').filter(
            username=request.user).first()
        # print(user_info)
        return render(request, 'user/center.html', {'user_info': user_info})

    def put(self, request):
        data = {
            'status': 'fail',
            'msg': '非法请求'
        }
        user = self.request.user
        put = QueryDict(request.body)
        username = put.get('username', '')
        name_cn = put.get('name_cn', '')
        phone = put.get('phone', '')

        # 判断请求是否构造非法请求
        if str(user) == username:
            try:
                UserProfile.objects.filter(username=user).update(name_cn=name_cn, phone=phone)
                data = {
                    'status': 'success',
                    'msg': '更新成功'
                }
            except Exception as e:
                data = {
                    'status': 'fail',
                    'msg': e
                }
        return JsonResponse(data)


class RoleListView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        role_info = UserProfile.objects.all().values('groups__name', 'groups__permissions__name').filter(
            username='liyongli')
        print(role_info)
        return render(request, 'user/rolelist.html')

    def put(self):
        pass

    def delete(self):
        pass
