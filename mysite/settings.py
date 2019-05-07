"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+a(-p_2i%)vh*d4sxc9m)x)qvgzn60v%@6gz_35+@45(+*wry*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'mdeditor',
    'comments', # 注册新创建的 comments 应用
    'haystack',
    'topic',
]

# 更改分词引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        #使用whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        #索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10 # 指定如何对搜索结果分页，这里设置为每 10 项结果为一页

# 当添加、修改、删除数据时，自动生成索引；博客文章更新不会太频繁实时更新没有问题
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_TZ = False

USE_I18N = True

USE_L10N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


#静态资源
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"/data/LJblog/static/",),
    os.path.join(BASE_DIR,"static",)
)






# 媒体文件的路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}
#
#
# MDEDITOR_CONFIGS = {
#     'default': {
#         'width': '90% ',  # Custom edit box width
#         'heigth': 500,  # Custom edit box height
#         'toolbar': ["undo", "redo", "|",
#                     "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
#                     "h1", "h2", "h3", "h5", "h6", "|",
#                     "list-ul", "list-ol", "hr", "|",
#                     "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime"
#                                                                                                            "emoji",
#                     "html-entities", "pagebreak", "goto-line", "|",
#                     "help", "info",
#                     "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar
#         'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type
#         'image_floder': 'editor',  # image save the folder name
#         'theme': 'default',  # edit box theme, dark / default
#         'preview_theme': 'default',  # Preview area theme, dark / default
#         'editor_theme': 'default',  # edit area theme, pastel-on-dark / default
#         'toolbar_autofixed': True,  # Whether the toolbar capitals
#         'search_replace': True,  # Whether to open the search for replacement
#         'emoji': True,  # whether to open the expression function
#         'tex': True,  # whether to open the tex chart function
#         'flow_chart': True,  # whether to open the flow chart function
#         'sequence': True  # Whether to open the sequence diagram function
#     }
#
# }
# https://segmentfault.com/a/1190000013671248

LOGIN_URL = '/admin'
LOGIN_REDIRECT_URL= '/topic/'