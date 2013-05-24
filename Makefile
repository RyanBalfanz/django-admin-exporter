sdist:
	python setup.py sdist

register:
	python setup.py register

upload: sdist
	python setup.py upload

test:
	DJANGO_SETTINGS_MODULE=example_project.settings.local nosetests

clean:
	rm -rf dist/
	rm -rf *.egg-info
