sdist:
	python setup.py sdist

register:
	python setup.py register

upload: sdist
	python setup.py upload

clean:
	rm -rf dist/
	rm -rf *.egg-info
