#!/bin/bash
	source /home/frozrt/login_social_authentication/task_env/bin/activate
	exec gunicorn -c "/home/frozrt/login_social_authentication/login_social_authentication/gunicorn_config.py" login_social_authentication.wsgi
