init:
	docker-compose build
	docker-compose up -d
	docker-compose stop

update_db:
	docker-compose up -d
	docker exec docker_api_1 python manage.py makemigrations accounts monitor
	docker exec docker_api_1 python manage.py migrate
	docker exec docker_api_1 python manage.py collectstatic --noinput
	docker-compose stop

clear:
	docker-compose stop
	docker-compose rm --all -f
	docker-compose ps
	docker ps

clear_all:
	$(MAKE) clear
	docker stop $(docker ps -a -q); true
	docker rm -f $(docker ps -a -q); true
	docker rmi -f `docker images | awk '{ print $3; }'`; true
	docker volume rm $(docker volume ls -qf dangling=true); true

up:
	COMPOSE_HTTP_TIMEOUT=500 docker-compose up

api_run:
	docker-compose run --rm --service-ports api

api_shell:
	docker-compose run --rm api bash

api_shell_cur:
	docker exec -it docker_api_1 bash

front_shell:
	docker-compose run --rm front bash

front_shell_cur:
	docker exec -it docker_front_1 bash

sample_shell:
	docker-compose run --rm sample-server bash

sample_shell_cur:
	docker exec -it docker_sample-server_1 bash
