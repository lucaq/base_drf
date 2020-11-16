#!/bin/bash
NAME='blueadmin_operation' #应用的名称
DJANGODIR=$(pwd) #django项目的目录
SOCKFILE=$DJANGODIR/gunicorn.sock #使用这个sock来通信
USER=$(whoami) #运行此应用的用户
GROUP=$(whoami) #运行此应用的组
NUM_WORKERS=1 #gunicorn使用的工作进程数
DJANGO_SETTINGS_MODULE=blueadmin_operation.settings #django的配置文件
DJANGO_WSGI_MODULE=blueadmin_operation.wsgi #wsgi模块
LOG_DIR=$DJANGODIR/logs #日志目录

echo "starting $NAME as `whoami`"

# #激活python虚拟运行环境 #部署时容器不需要虚拟环境，本地手动激活虚拟环境再执行脚本
# cd $DJANGODIR
# source bg_env/bin/activate
# export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
# export PYTHONPATH=$DJANGODIR:$PYTHONPATH

#如果gunicorn.sock所在目录不存在则创建
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR


echo ${DJANGO_WSGI_MODULE}
echo $NAME
echo $NUM_WORKERS
echo unix:$SOCKFILE


#启动Django
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --bind=0.0.0.0:8003 \
    --bind=unix:$SOCKFILE \
    --access-logfile=${LOG_DIR}/gunicorn_access.log \
    --reload # 代码修改自动重启
