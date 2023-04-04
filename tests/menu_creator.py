import os
import django
from django.conf import settings
from django.core.management import call_command


db_path = '../db.sqlite3'
migrations_path = '../tree_menu/migrations'


if os.path.exists(db_path):
    os.remove(db_path)

for file in os.listdir(migrations_path):
    file_path = os.path.join(migrations_path, file)
    if os.path.isfile(file_path) and not '__init__' in file:
        os.remove(file_path)

DJANGO_SETTINGS = {
        'INSTALLED_APPS': ('tree_menu',)
    }
settings.configure(**DJANGO_SETTINGS)
django.setup()
call_command('makemigrations')



# makemigrations('tree_menu')


from django.core.management.commands import makemigrations, migrate
migrate



# from django.db.migrations.operations import
#
# call_command('makemigrations', app_label='dynamics', database=db_path)
# status = check_output('python manage.py makemigrations')
# check_output('python manage.py migrate', shell=True)
