# base_drf

正式部署时，debug=False，需要单独配置图片目录，配置 nginx
测试 debug=True，可直接使用 django 的 media_root 进行配置测试

#### 介绍

base_drf 做成一个基础框架，整合了一个 common_lib，对 drf 做了部分封装
settings 拆分
swagger 集成
cors 跨域
后续要集成权限/认证等

#### 安装教程

psycopg2 包需要依赖 zlibc、zlib1g-dev、libffi-dev
sudo apt install zlibc zlib1g-dev libffi-dev

#### 使用说明

clone 后在此基础上继续开发

后续完善更多功能，更多实用组件和模块
