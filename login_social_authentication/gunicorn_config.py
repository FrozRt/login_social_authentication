command = '/home/frozrt/login_social_authentication/task_env/bin/gunicorn'
pythonpath = '/home/frozrt/login_social_authentication'
bind = '127.0.0.1:8001'
workers = 3
user = 'frozrt'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=login_social_authentication.settings'
