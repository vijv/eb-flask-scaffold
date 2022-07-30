install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

init:
	eb init -p python-3.8 eb-flask-scaffold --region us-east-1

deploy:
	eb deploy eb-flask-scaffold-dev
