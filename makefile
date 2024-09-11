activate:
	if [ -d "venv" ]; then \
		echo "Python 🐍 environment was activated"; \
		source venv/bin/activate; \
	else \
		 echo "The folder environment doesn't exist"; \
        python3 -m venv venv; \
        source venv/bin/activate; \
		 echo "The environment folder was created and the python 🐍 environment was activated"; \
	fi
install:
	pip install -r requirements.txt --break-system-packages

migrate:
	python3 manage.py migrate

start_mqtt:
	 nohup python3 manage.py start_mqtt &

start_control:
	python3 manage.py start_control &

run_server:
	nohup python3 manage.py runserver 0.0.0.0:80 &

run_create_user:
	python3 manage.py createsuperuser