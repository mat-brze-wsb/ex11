.PHONY: deps test

deps:
		pip install -r requirements.txt; \
					pip install -r test_requirements.txt

lint:
	flake8 --exit-zero hello_world test

test:
		PYTHONPATH=. py.test

docker_build:
		docker image build -t hello-world-printer .

run:
		PYTHONPATH=. FLASK_APP=hello_world flask run

docker_run: docker_build
	docker run \
		--name hello-world-printer-dev \
		-p 5000:5000 \
		-d hello-world-printer
