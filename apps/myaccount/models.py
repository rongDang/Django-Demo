from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

"""
    由于Django自带的User模型字段邮箱，所以我们需要对其扩展，最便捷的方式就是创建UserProfile的模型，
    如下所示,我们添加了org和telephone两个字段。
"""


class UserProfile(models.Model):
    # 和Django自带的User模型是一对一关系，其实就相当于是一个表
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    org = models.CharField('Organization', max_length=128, blank=True)
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    mod_date = models.DateTimeField('last modified', auto_now=True)

    class Meta:
        verbose_name = 'user Profile'

    def __str__(self):
        return "{}'s profile".format(self.user.__str__())

    def account_verified(self):
        # is_authenticated是判断当前用户是否已通过身份验证(是否登录)
        if self.user.is_authenticated:
            # 查询登录用户的邮箱，verified默认为False，认证后为True
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False




