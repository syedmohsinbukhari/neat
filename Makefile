# Need .PHONY in the beginning sp that it doesn't run files
.PHONY: init install test clean-pyc

# To remove pyc files
clean-pyc:
    find . -name '*.pyc' -exec rm --force {} +
    find . -name '*.pyo' -exec rm --force {} +
    name '*~' -exec rm --force  {} 

init:
	pip install -r requirements.txt
   
test:
	clean-pyc
	py.test . --cov=.
	coveralls

install:
	python setup.py install

