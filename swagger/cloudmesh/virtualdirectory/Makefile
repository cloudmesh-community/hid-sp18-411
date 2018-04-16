all: clean start-docker

start-docker:
	touch .env
	echo "export MONGO_HOST=Mongo_endpoint" >> .env
	docker-compose up -d --build

stop:
	echo "Docker build complete"
	docker-compose stop