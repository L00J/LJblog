# LJblog

#### 项目介绍
个人博客
django2.0 + bootstrap + markdown




#### 初始化环境
```
cd LJblog
source  env/bin/activate 
#载入py环境

python manage.py makemigrations 
#为改动models创建迁移记录
python manage.py migrate 
#同步数据库
python manage.py  createsuperuser
#建立后台管理员帐号

python manage.py runserver
#启动服务
```

### 导入数据
```
python manage.py loaddata blog_dump.json
#导入文章内容（测试）
```