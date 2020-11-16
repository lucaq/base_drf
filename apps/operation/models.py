from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class Color(models.Model):
    """标签颜色"""
    id = models.AutoField(primary_key=True)
    rgb = models.CharField('颜色rgb值', max_length=7)
    remark = models.CharField(max_length=20)
    admin_name = models.CharField(verbose_name='管理员name',
                                  max_length=32,
                                  default='administrator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'operation_color'
        ordering = ['id']

    def __str__(self):
        return self.rgb


class TagCategory(models.Model):
    """标签分类"""
    # 分类创建后不删除，仅修改和停用/启用
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=10)
    admin_name = models.CharField(verbose_name='管理员name',
                                  max_length=32,
                                  default='administrator')
    dep_name = models.CharField(verbose_name='所属部门',
                                max_length=32,
                                default='admin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(verbose_name='启用状态', default=True)
    remark = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'operation_tag_category'


class Tag(models.Model):
    """标签"""
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(verbose_name='标签名', max_length=20)
    category = models.ForeignKey(TagCategory, on_delete=models.PROTECT)
    admin_name = models.CharField(verbose_name='管理员name',
                                  max_length=32,
                                  default='administrator')
    weight = models.IntegerField(verbose_name='标签值', default=1)  # 默认为1，暂时没用到
    color = models.CharField(verbose_name='标签颜色',
                             default='#808080',
                             max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(verbose_name='启用状态', default=True)
    remark = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = 'operation_tag'


class Group(models.Model):
    """用户分组"""
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(verbose_name='组名', max_length=64)
    GROUP_TYPE_CHOICES = ((1, 'STATIC'), (2, 'DYNAMIC'))
    group_type = models.IntegerField(verbose_name='组类型',
                                     choices=GROUP_TYPE_CHOICES)
    admin_name = models.CharField(verbose_name='管理员name',
                                  max_length=32,
                                  default='administrator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    GENDER_CHOICES = (
        (1, 'MALE'),
        (2, 'FEMALE'),
        (3, 'UNKNOWN'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    region = models.CharField(verbose_name='地区', max_length=128, null=True)
    from_group = models.IntegerField(verbose_name='已存在分组id', null=True)
    tags = ArrayField(models.IntegerField())
    from_tag_value = models.IntegerField(verbose_name='开始标签值', null=True)
    to_tag_value = models.IntegerField(verbose_name='结束标签值', null=True)
    start_tagging_at = models.DateTimeField(verbose_name='起始打标签时间', null=True)
    end_tagging_at = models.DateTimeField(verbose_name='结束打标签时间', null=True)
    life_cycle = models.IntegerField(verbose_name='生命周期', null=True)
    from_active_value = models.IntegerField(verbose_name='开始活跃度', null=True)
    to_active_value = models.IntegerField(verbose_name='结束活跃度', null=True)
    received_count = models.IntegerField(verbose_name='接收条数', null=True)
    remark = models.CharField(max_length=128)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = 'operation_group'


class User(models.Model):
    """用户"""
    id = models.AutoField(primary_key=True)
    nick_name = models.CharField(verbose_name='用户昵称', max_length=100)
    union_id = models.CharField(verbose_name='微信用户union_id', max_length=64)
    avatar = models.CharField(verbose_name='用户头像链接', max_length=36)
    age = models.IntegerField(verbose_name='年龄')
    GENDER_CHOICES = (
        (1, 'MALE'),
        (2, 'FEMALE'),
        (3, 'UNKNOWN'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=3)
    region = models.CharField(verbose_name='地区', max_length=100)
    gzh_follow_count = models.IntegerField(verbose_name='公众号关注数', default=0)
    xcx_authorize_count = models.IntegerField(verbose_name='小程序授权数', default=0)
    is_registed = models.BooleanField(verbose_name='是否提交注册', default=False)
    tag = models.ManyToManyField(Tag, through='UserTags')
    group = models.ManyToManyField(Group, through='UserGroups')
    active_value = models.IntegerField(verbose_name='活跃度', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    interactive_at = models.DateTimeField(verbose_name='最近互动时间', auto_now=True)
    remark = models.CharField(max_length=128)

    def __str__(self):
        return self.nick_name

    class Meta:
        db_table = 'operation_user'


class UserGroups(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    admin_name = models.CharField(verbose_name='管理员name',
                                  max_length=32,
                                  default='auto')
    grouping_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'operation_user_groups'


class UserTags(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    admin_name = models.CharField(verbose_name='管理员name',
                                  max_length=32,
                                  default='auto')
    tagging_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'operation_user_tags'


class UserRegisted(models.Model):
    """用户注册信息"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    corporation = models.CharField(verbose_name='公司', max_length=128)
    position = models.CharField(verbose_name='职位', max_length=64)
    phone = models.CharField(max_length=18)
    email = models.CharField(max_length=64)
    GENDER_CHOICES = (
        (1, 'MALE'),
        (2, 'FEMALE'),
        (3, 'UNKNOWN'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=3)
    region = models.CharField(verbose_name='地区', max_length=100)
    others = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'operation_user_registed'
