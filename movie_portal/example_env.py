SECRET_KEY = 'f6zq+&)v6%w6ik*3v)zp%e=m+c@-9i8yc&vmp1f293@h=+jf+9'
ALLOWED_HOSTS = ['*']
DEBUG = False

DATABASE_ENGINE = 'django.db.backends.mysql'
DATABASE_NAME = 'database_name'
DATABASE_USER = 'db_username'
DATABASE_PASSWORD = 'db_password'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '3302'
CHARTSET = 'utf8mb4'
INIT_COMMAND = "ALTER DATABASE {} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci;".format(DATABASE_NAME)

YOUTUBE_API_KEY = 'your_secret_api_key'

# Data Update Interval In Seconds
DATA_UPDATE_INTERVAL = 1800

