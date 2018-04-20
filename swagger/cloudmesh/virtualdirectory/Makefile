SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=swagger.yaml
DIR=NoSQL/
STUB_PATH=NoSQL/server/flaskConnexion	

all: clean build start-docker

start-service:
	cd $(STUB_PATH)
	
	pip install -r requirements.txt

	python setup.py install
		
	python -m swagger_server

build:
	wget https://www.dropbox.com/s/0730xoz8rboes7b/swagger-codegen-cli-2.3.1.jar
	
	mkdir $(DIR)
	
	$(SWAGGERCODEGEN) generate\
 	-i $(YAML)
 	-l python-flask\
 	-o $(STUB_PATH)
 	-D supportPython2=true
	
	cp default_controller.py $(STUB_PATH)/swagger_server/controllers
	
	cd $(STUB_PATH)
	
	pip install -r requirements.txt

	python setup.py install
		
	python -m swagger_server

clean:
	sudo rm -rf $(DIR)
	sudo rm *.jar

start-docker:
	touch .env
	echo "export MONGO_HOST=Mongo_endpoint" >> .env
	docker-compose up -d --build

stop-docker:
	echo "Docker build complete"
	docker-compose stop
