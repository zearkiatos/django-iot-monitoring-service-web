activate:
	if [ -d "venv" ]; then \
		echo "Python 🐍 environment was activated"; \
		source venv/bin/activate; \
	else \
		 echo "The folder environment doesn't exist"; \
        python -m venv venv; \
        source venv/bin/activate; \
		 echo "The environment folder was created and the python 🐍 environment was activated"; \
	fi
install:
	pip install -r requirements.txt --break-system-packages

migrate:
	python3 manage.py migrate

start_mqtt:
	 nohup python3 IOTMonitoringServer/manage.py start_mqtt &