# Generated by Django 2.2.8 on 2020-06-15 18:35

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rgb', models.CharField(max_length=7, verbose_name='颜色rgb值')),
                ('remark', models.CharField(max_length=20)),
                ('admin_name', models.CharField(default='administrator', max_length=32, verbose_name='管理员name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'operation_color',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=64, verbose_name='组名')),
                ('group_type', models.IntegerField(choices=[(1, 'STATIC'), (2, 'DYNAMIC')], verbose_name='组类型')),
                ('admin_name', models.CharField(default='administrator', max_length=32, verbose_name='管理员name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'UNKNOWN')], null=True)),
                ('region', models.CharField(max_length=128, null=True, verbose_name='地区')),
                ('from_group', models.IntegerField(null=True, verbose_name='已存在分组id')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('from_tag_value', models.IntegerField(null=True, verbose_name='开始标签值')),
                ('to_tag_value', models.IntegerField(null=True, verbose_name='结束标签值')),
                ('start_tagging_at', models.DateTimeField(null=True, verbose_name='起始打标签时间')),
                ('end_tagging_at', models.DateTimeField(null=True, verbose_name='结束打标签时间')),
                ('life_cycle', models.IntegerField(null=True, verbose_name='生命周期')),
                ('from_active_value', models.IntegerField(null=True, verbose_name='开始活跃度')),
                ('to_active_value', models.IntegerField(null=True, verbose_name='结束活跃度')),
                ('received_count', models.IntegerField(null=True, verbose_name='接收条数')),
                ('remark', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'operation_group',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=20, verbose_name='标签名')),
                ('admin_name', models.CharField(default='administrator', max_length=32, verbose_name='管理员name')),
                ('weight', models.IntegerField(default=1, verbose_name='标签值')),
                ('color', models.CharField(default='#808080', max_length=7, verbose_name='标签颜色')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True, verbose_name='启用状态')),
                ('remark', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'operation_tag',
            },
        ),
        migrations.CreateModel(
            name='TagCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10, verbose_name='分类标题')),
                ('admin_name', models.CharField(default='administrator', max_length=32, verbose_name='管理员name')),
                ('dep_name', models.CharField(default='admin', max_length=32, verbose_name='所属部门')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True, verbose_name='启用状态')),
                ('remark', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'operation_tag_category',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nick_name', models.CharField(max_length=100, verbose_name='用户昵称')),
                ('union_id', models.CharField(max_length=64, verbose_name='微信用户union_id')),
                ('avatar', models.CharField(max_length=36, verbose_name='用户头像链接')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'UNKNOWN')], default=3)),
                ('region', models.CharField(max_length=100, verbose_name='地区')),
                ('gzh_follow_count', models.IntegerField(default=0, verbose_name='公众号关注数')),
                ('xcx_authorize_count', models.IntegerField(default=0, verbose_name='小程序授权数')),
                ('is_registed', models.BooleanField(default=False, verbose_name='是否提交注册')),
                ('active_value', models.IntegerField(default=0, verbose_name='活跃度')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('interactive_at', models.DateTimeField(auto_now=True, verbose_name='最近互动时间')),
                ('remark', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'operation_user',
            },
        ),
        migrations.CreateModel(
            name='UserTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(default='auto', max_length=32, verbose_name='管理员name')),
                ('tagging_at', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operation.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operation.User')),
            ],
            options={
                'db_table': 'operation_user_tags',
            },
        ),
        migrations.CreateModel(
            name='UserRegisted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corporation', models.CharField(max_length=128, verbose_name='公司')),
                ('position', models.CharField(max_length=64, verbose_name='职位')),
                ('phone', models.CharField(max_length=18)),
                ('email', models.CharField(max_length=64)),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'UNKNOWN')], default=3)),
                ('region', models.CharField(max_length=100, verbose_name='地区')),
                ('others', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation.User')),
            ],
            options={
                'db_table': 'operation_user_registed',
            },
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(default='auto', max_length=32, verbose_name='管理员name')),
                ('grouping_at', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operation.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operation.User')),
            ],
            options={
                'db_table': 'operation_user_groups',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(through='operation.UserGroups', to='operation.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='tag',
            field=models.ManyToManyField(through='operation.UserTags', to='operation.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operation.TagCategory'),
        ),
    ]
