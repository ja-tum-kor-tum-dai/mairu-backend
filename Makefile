default: up

up:
	docker network create -d bridge mairu | true
	docker-compose up -d

down:
	docker-compose down --remove-orphans
	docker network rm mairu | true