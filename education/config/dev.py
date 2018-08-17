# coding:utf-8
'''
@summary: 全局常量设置
用于本地开发环境
'''
import os

# ===============================================================================
# 数据库设置, 本地开发数据库设置
# ===============================================================================

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '3306')
DB_NAME = os.environ.get('DB_NAME', 'education')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PWD = os.environ.get('DB_PWD', '123456')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PWD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'options': {
            'MAX_ENTRIES': 10240,
        },
    }
}
