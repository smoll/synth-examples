all: env test

env: env/bin/activate
env/bin/activate: requirements.txt
	test -d env || virtualenv env
	env/bin/pip install -U pip setuptools
	env/bin/pip install -Ur requirements.txt
	touch env/bin/activate

test:
	# Activate virtualenv in the make shell
	( \
		. env/bin/activate; \
		python geo.py; \
	)
