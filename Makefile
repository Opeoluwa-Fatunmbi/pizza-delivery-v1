ifneq (,$(wildcard ./.env))
include .env
export 
ENV_FILE_PARAM = --env-file .env

endif

act:
	source env/Scripts/activate

build:
	docker-compose up --build -d --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down

show-logs:
	docker-compose logs

serv:
	uvicorn main:app --reload

alembic_init:
	alembic init app/db/migrations

mmig: # run with "make mmig" or "make mmig message='migration message'"
	if [ -z "$(message)" ]; then \
		alembic revision --autogenerate; \
	else \
		alembic revision --autogenerate -m "$(message)"; \
	fi
	
mig:
	alembic upgrade heads

initial_data:
	python initials/initial_data.py

tests:
	pytest --disable-warnings -vv -x

reqm:
	pip install -r requirements.txt

ureqm:
	pip freeze > requirements.txt