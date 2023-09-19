install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py
	python -m pytest --nbval src/*.ipynb

format:	
	black *.py 

lint:
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py 
	ruff check *.py lib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy: 
#goes here

all: install lint format test
