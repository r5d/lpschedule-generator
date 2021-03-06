# -*- coding: utf-8 -*-
#
#   SPDX-License-Identifier: CC0-1.0
#
#   This file is part of lpschedule-generator.
#

GNU_MAKE=gmake

VENV_DIR='.venv'
VENV_CMD=virtualenv
VENV_PREFIX=.
VENV_DIR=${VENV_PREFIX}/.lpschedule-generator

test:
	@nosetests
.PHONY: test

fmt:
	black --include 'lps_gen.py|setup.py|tests/*.py|lpschedule_generator/*.py' .
.PHONY: fmt

build:
	@python setup.py sdist bdist_wheel
.PHONY: build

upload:
	@twine upload -r pypi -s --sign-with 'gpg2' \
		-i '1534 126D 8C8E AD29 EDD9  1396 6BE9 3D8B F866 4377' \
		dist/*.tar.gz
	@twine upload -r pypi -s --sign-with 'gpg2' \
		-i '1534 126D 8C8E AD29 EDD9  1396 6BE9 3D8B F866 4377' \
		dist/*.whl
.PHONY: upload

docs:
	${GNU_MAKE} -C docs html
.PHONY: docs

upload-docs: docs
	@rsync -avz --delete docs/_build/html/  $(LPSG_DOCS_HOST)
.PHONY: upload-docs


venv:
	rm -rf *.egg-info .eggs
	${SHELL} -c 'if [[ -d $(VENV_DIR) ]] then mv $(VENV_DIR) $(VENV_DIR).`date +%s`; fi'
	${VENV_CMD} --clear --python=python3 $(VENV_DIR)
	@echo 'Initialized virtualenv, run' \
		'source '$(VENV_DIR)'/bin/activate' \
		'to activate the virtual environment'
.PHONY: venv

clean: clean-build clean-pyc clean-docs
.PHONY: clean

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
.PHONY: clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
.PHONY: clean-pyc

clean-venv:
	rm -rf ${VENV_DIR}*/
.PHONY: clean-venv

clean-docs:
	${GNU_MAKE} -C docs clean
.PHONY: clean-docs

dev:
	python setup.py develop
	pip install -r requirements.txt
.PHONY: dev
