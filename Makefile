deps:
	@pip install -r requirements.txt

dev-deps:
	@pip install -r dev_requirements.txt

flake8:
	@flake8 .

isort:
	@isort -rc .

run:
	@python dawer
