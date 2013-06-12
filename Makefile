sdist:
	python setup.py sdist

register:
	python setup.py register

upload: sdist
	python setup.py upload

test:
	PYTHONPATH=`pwd`/example_project/ DJANGO_SETTINGS_MODULE=example_project.settings.local nosetests --with-doctest

clean:
	find ./ -name "*.pyc" -delete
	rm -rf dist/
	rm -rf *.egg-info
