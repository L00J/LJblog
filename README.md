##  LJblog - 个人博客


### 环境
![Python](https://img.shields.io/badge/python-3.7.0-blue.svg?style=plastic)
![django](https://img.shields.io/badge/django-2.1.7-blue.svg?style=plastic)
![bootstrap](https://img.shields.io/badge/bootstrap-3.3.7-brightgreen.svg?style=plastic)
![markdown](https://img.shields.io/badge/markdown-3.0.1-brightgreen.svg?style=plastic)
![django-mdeditor](https://img.shields.io/badge/mdeditor-0.1.13-brightgreen.svg?style=plastic)





### 初始化环境
```
cd LJblog
python3 -m venv env_django (或: virtualenv -p `which  python3` env_django)
source  env_django/bin/activate
#载入py环境

pip  install -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com  -r requirements.txt
#安装pip包(阿里源)

python manage.py makemigrations 
#为改动models创建迁移记录
python manage.py migrate 
#同步数据库
python manage.py  createsuperuser
#建立后台管理员帐号

python manage.py runserver
#启动服务
```

### 维护调试
**数据导入和导出**
```
python manage.py dumpdata >  dump_blog.json 
#导出文章内容
python manage.py loaddata  dump_blog.json
#导入内容
```


### 效果预览

首页:
![首页](doc/index.jpg)

文章发布图：
![后台](doc/article1.jpg)
![后台](doc/article2.jpg)



### demo:
[https://attacker.club/](https://attacker.club/ "https://attacker.club/")