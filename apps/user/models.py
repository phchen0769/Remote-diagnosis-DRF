from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Menu(models.Model):
    """
    菜单
    """

    menu_id = models.IntegerField(
        default=0,
        primary_key=True,
        verbose_name="菜单ID",
        help_text="菜单ID",
    )
    sub_menu = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="上级菜单",
        help_text="上级菜单",
        # related_name="children_menu",
    )
    path = models.CharField(
        null=True, max_length=50, verbose_name="路径", help_text="路径"
    )

    component = models.CharField(
        null=True, max_length=50, verbose_name="组件名称", help_text="组件名称"
    )
    redirect = models.CharField(
        null=True, max_length=30, verbose_name="重定向", help_text="重定向"
    )
    hidden = models.BooleanField(
        default=False, verbose_name="是否隐藏", help_text="是否隐藏"
    )
    name = models.CharField(
        null=True, max_length=30, verbose_name="路由名", help_text="路由名"
    )
    title = models.CharField(
        null=True, max_length=30, verbose_name="菜单名", help_text="菜单名"
    )
    icon = models.CharField(
        null=True, max_length=50, verbose_name="图标", help_text="图标"
    )

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限
    """

    METHOD_TYPE = (
        (1, "GET"),
        (2, "POST"),
        (3, "DELETE"),
        (4, "PUT"),
        (5, "PATCH"),
        (6, "OPTIONS"),
    )
    # URL别名
    name = models.CharField(
        null=True, max_length=30, verbose_name="权限名称", help_text="权限名称"
    )
    method_type = models.IntegerField(
        choices=METHOD_TYPE, verbose_name="方法类型", help_text="方法类型"
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name="菜单",
        help_text="菜单",
    )

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    角色
    """

    name = models.CharField(
        null=True, max_length=30, verbose_name="角色名称", help_text="角色名称"
    )
    permission = models.ManyToManyField(
        Permission,
        verbose_name="权限",
        help_text="权限",
    )

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    """
    用户
    """

    username = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        unique=True,
        verbose_name="姓名",
        help_text="姓名",
    )
    avatar = models.CharField(
        max_length=50,
        verbose_name="用户头像",
        help_text="用户头像",
        default="default.jpg",
    )
    birthday = models.DateField(
        null=True, blank=True, verbose_name="生日", help_text="生日"
    )
    mobile = models.CharField(max_length=11, verbose_name="手机", help_text="手机")
    gender = models.CharField(
        max_length=6,
        choices=(("male", "男"), ("female", "女")),
        default="female",
        verbose_name="性别",
        help_text="性别",
    )
    email = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="邮箱", help_text="邮箱"
    )

    role = models.ManyToManyField(
        Role,
        verbose_name="角色",
        help_text="角色",
    )

    def get_menus(self):
        if self.is_anonymous:
            menus = []
            return menus
        else:
            # 获取该用户所有角色
            roles = self.role.all()
            # 获取所有角色的权限
            permissions = Permission.objects.filter(role__in=roles)
            # 获取所有权限的子菜单
            child_menus = Menu.objects.filter(permission__in=permissions)
            # 获取所有的上级菜单
            sub_menus = Menu.objects.filter(sub_menu__isnull=True)
            # 获取所有权限的上级菜单
            menus = sub_menus.filter(menu_id__in=child_menus.values("sub_menu_id"))
            # 合并上级菜单和子菜单
            all_menus = menus | child_menus
            return all_menus

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class SmsVerifyCode(models.Model):
    """
    短信验证码
    """

    code = models.CharField(
        null=True, max_length=10, verbose_name="验证码", help_text="验证码"
    )
    mobile = models.CharField(
        null=True, max_length=11, verbose_name="手机", help_text="手机"
    )
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name="添加时间", help_text="添加时间"
    )

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class EmailVerifyCode(models.Model):
    """
    邮箱验证码
    """

    code = models.CharField(
        null=True, max_length=10, verbose_name="验证码", help_text="验证码"
    )
    email = models.EmailField(
        null=True, unique=True, max_length=100, verbose_name="邮箱", help_text="邮箱"
    )
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name="添加时间", help_text="添加时间"
    )

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
