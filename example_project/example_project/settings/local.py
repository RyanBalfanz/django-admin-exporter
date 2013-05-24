from .base import *


ADMINS = (
	('Ryan Balfanz', 'ryan@ryanbalanz.net'),
)

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'admin_exporter_example_project.db',
	}
}

INSTALLED_APPS += (
	'django.contrib.admin',
)

INSTALLED_APPS += (
	'example_project.core',
	'admin_exporter',
)
