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
VENV_DIR3=${VENV_PREFIX}/.venv3-lpschedule-generator

test:
	@nosetests

.PHONY: test

build-dist:
	@python setup.py sdist bdist_wheel

egg:
	@python setup.py egg_info

upload:
	@twine upload -r pypi -s -i '1534 126D 8C8E AD29 EDD9  1396 6BE9 3D8B F866 4377' dist/*.tar.gz
	@twine upload -r pypi -s -i '1534 126D 8C8E AD29 EDD9  1396 6BE9 3D8B F866 4377' dist/*.whl

.PHONY: build-dist egg upload

docs:
	${GNU_MAKE} -C docs html

upload-docs: docs
	@rsync -avz --delete docs/_build/html/  $(LPSG_DOCS_HOST)

.PHONY: docs upload-docs


venv3:
	rm -rf *.egg-info
	${SHELL} -c 'if [[ -d $(VENV_DIR3) ]] then mv $(VENV_DIR3) $(VENV_DIR3).`date +%s`; fi'
	${VENV_CMD} --clear --python=python3 $(VENV_DIR3)
	@echo 'Initialized virtualenv, run' \
		'source '$(VENV_DIR3)'/bin/activate' \
		'to activate the virtual environment'
.PHONY: venv3

clean: clean-build clean-pyc clean-docs
.PHONY: clean

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +

clean-venv:
	rm -rf ${VENV_DIR3}*/

clean-docs:
	${GNU_MAKE} -C docs clean

.PHONY: clean-build clean-pyc clean-venv clean-docs

dev-env:
	pip install -r requirements.txt
	python setup.py develop
.PHONY: dev-env
