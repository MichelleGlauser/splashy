web: gunicorn splashy_project.wsgi --log-file -
web: python splashy_project/manage.py collectstatic --noinput; gunicorn splashy_project/settings.py