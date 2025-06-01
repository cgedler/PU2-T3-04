from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# SQLITE
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# POSTGRESQL
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'libros',
        'USER': 'cge',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# MYSQL
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'libros',
        'USER': 'cge',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}