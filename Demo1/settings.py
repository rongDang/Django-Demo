"""
Django settings for Demo1 project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lcf!%-k&5jovihk)cj=hzazri1)f_u2o=l)w4j+astn$$ik9z5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',              # 站点管理系统
    'django.contrib.auth',               # 认证系统
    'django.contrib.contenttypes',      # content types 框架
    'django.contrib.sessions',          # session 框架
    'django.contrib.messages',          # message 框架
    'django.contrib.staticfiles',       # 静态文件管理框架
    'model.apps.ModelConfig',           # Django应用的注册
    'nick.apps.NickConfig',
    'myaccount.apps.MyaccountConfig',
    'markdown_deux',        # 前端渲染markdown
    'mdeditor',                          # 富文本编辑器
    'pure_pagination',                  # 分页
    'widget_tweaks',                    # 自定义渲染forms表单工具
    # sites一个让你可以在同一个数据库与 Django 安装中管理多个网站的框架,comments,allauth对它有依赖
    'django.contrib.sites',
    'django_comments',  # 评论插件
    'allauth',  # 管理用户注册登录的第三方包
    'allauth.account',
    'allauth.socialaccount',
    # 第三方账号关联，测试使用GitHub
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.baidu',
]
SITE_ID = 1     # 站点设置？

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 3,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Demo1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',

                # 将新建的两个 上下文渲染器 加入到 settings.py 中：
                'Demo1.context_processor.ip_address',
                'Demo1.context_processor.work_data',
            ],
            # 加了下面这段，则不需要在html上写{% load  myFilter%} 和 {% load static%} ，Django的内置变量
            # 'builtins':['nick.templatetags.myFilter', 'django.templatetags.static'],
        },
    },
]

WSGI_APPLICATION = 'Demo1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test1',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '3306',
        'HOST': '127.0.0.1'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
# Django 后台admin页面语言设置
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 下面的静态目录用来存放app中使用的共同的静态文件
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 配置媒体文件，
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 关于allauth的基本设定
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # 当用户登录时，既可以使用用户名也可以使用email
ACCOUNT_EMAIL_REQUIRED = True       # 注册时必须填写email
LOGIN_REDIRECT_URL = '/accounts/profile/'    # 设置登录后跳转链接

# 告诉django-allauth使用我们自定义的注册表单
ACCOUNT_SIGNUP_FORM_CLASS = 'myaccount.forms.SignupForm'

# django-allauth相关设置
AUTHENTICATION_BACKENDS = (
    # django admin使用的用户登录于django-allauth无关
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# django的邮箱设定，使用allauth的话，注册后它会给邮箱发送一条注册信息给注册邮箱验证
EMAIL_HOST = 'smtp.qq.com'  # 这里使用QQ的smtp服务
EMAIL_PORT = 25
EMAIL_HOST_USER = '2801293031@qq.com'   # 你的 QQ 账号和授权码
EMAIL_HOST_PASSWORD = 'vdltztnwuggbddei'
EMAIL_USE_TLS = True  # 这里必须是 True，否则发送不成功
EMAIL_FROM = '2801293031@qq.com'  # 发件人邮箱
DEFAULT_FROM_EMAIL = '2801293031@qq.com'    # 默认发件人邮箱

# mdeditor markdown编辑器配置
MDEDITOR_CONFIGS = {
    'default': {
        'width': '100%',  # 自定义编辑框宽度
        'heigth': 500,  # 自定义编辑框高度
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
        'image_floder': 'editor',  # 图片保存文件夹名称
        'theme': 'default',  # 编辑框主题 ，dark / default
        'preview_theme': 'default',  # 预览区域主题， dark / default
        'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,  # 是否开启查找替换
        'emoji': True,  # 是否开启表情功能
        'tex': True,  # 是否开启 tex 图表功能
        'flow_chart': True,  # 是否开启流程图功能
        'sequence': True  # 是否开启序列图功能
    },

    'form_config': {
        'width': '100%',  # 自定义编辑框宽度
        'heigth': 300,  # 自定义编辑框高度
        'toolbar': ["undo", "redo", "|", "link", "image", "code", "code-block",
                    "table",
                    "emoji", "|",
                    "help", "info", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
        'image_floder': 'editor',  # 图片保存文件夹名称
        'theme': 'default',  # 编辑框主题 ，dark / default
        'preview_theme': 'default',  # 预览区域主题， dark / default
        'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,  # 是否开启查找替换
        'emoji': True,  # 是否开启表情功能
        'tex': True,  # 是否开启 tex 图表功能
        'flow_chart': True,  # 是否开启流程图功能
        'sequence': True,  # 是否开启序列图功能
    },
}

# 使用rabbitMQ做MQ配置
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672'

# from celery.schedules import crontab  定时任务调用crontab
CELERYD_MAX_TASKS_PER_CHILD = 5
CELERY_BEAT_SCHEDULE = {
    # 周期性任务
    'task-one': {
        'task': 'model.tasks.test_celery',
        'schedule': 5.0,  # 每5秒执行一次
    },
    # 定时任务
    # 'task-two': {
    #     'task': 'app.tasks.print_hello',
    #     'schedule': crontab(minute=0, hour='*/3,10-19'),
    # }
}
