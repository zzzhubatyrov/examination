# Main commands
init: docker-down-clear docker-pull docker-build docker-up
full-init: docker-down-clear docker-pull docker-build docker-up makemigrate migrate fill-table
migrate-data: makemigrate migrate 
down: docker-down-clear
restart: down init

# For frontend

front-restart: docker-down-clear docker-rmi docker-pull docker-build docker-up

docker-rmi:
	docker rmi $(docker image ls)

# Init python virtual environment

python-init: create-venv activate-venv install-requirements

# Docker run container

docker-up:
	docker-compose up

docker-down:
	docker-compose down --remove-orphans

docker-down-clear:
	docker-compose down -v --remove-orphans

docker-pull:
	docker-compose pull

docker-build:
	docker-compose build

# Django run project

makemigrate:                                          
	python $(PWD)/backend/manage.py makemigrations

migrate:                                              
	python $(PWD)/backend/manage.py migrate

createsuperuser:                                      
	python $(PWD)/backend/manage.py createsuperuser

# Create and Activate python venv

create-venv:
	python -m venv venv

activate-venv:
	source $(PWD)/venv/bin/activate

# Install requirements

install-requirements:
	pip install -r backend/requirements.txt
