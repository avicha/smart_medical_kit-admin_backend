# coding=utf-8
APP_NAME = 'smart_medical_kit-admin'
# app的secret key
SECRET_KEY = ''
# 服务器绑定主机和端口
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
SERVER_DEBUG = True
SERVER_USE_RELOADER = True
SERVER_USE_DEBUGGER = True
# 默认缓存失效时间5分钟
CACHE_DEFAULT_TIMEOUT = 300
# 文件缓存条数500条
CACHE_FILE_THRESHOLD = 500
CACHE_FILE_DIR = '../cache'
CACHE_FILE_MODE = 0600
# 缓存Redis配置
CACHE_REDIS_HOST = 'localhost'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_PASSWORD = None
CACHE_REDIS_DB = 0
CACHE_REDIS_KEY_PREFIX = 'cache:'
# 日志文件配置
LOG_FILE_DIR = '../logs'
LOG_FILE_WHEN = 'midnight'
LOG_FILE_BACKUP_COUNT = 30
# 存储配置
STORAGE_FILE_DIR = '../storage'
