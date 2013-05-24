sdist:
	python setup.py sdist

register:
	python setup.py register

upload: sdist
	python setup.py upload

test:
	# cd example_project && python manage.py test

clean:
	rm -rf dist/
	rm -rf *.egg-info
