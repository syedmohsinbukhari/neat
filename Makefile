init:
	pip install -r requirements.txt

test:
	py.test . --cov=.
	coveralls

install:
	python setup.py install

.PHONY: init install test
