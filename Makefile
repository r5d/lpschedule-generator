# -*- coding: utf-8 -*-
#
#    Copyright (C) 2015-2016  lpschedule-generator contributors. See CONTRIBUTORS.
#
#    This file is part of lpschedule-generator.
#
#   lpschedule-generator is free software: you can redistribute it
#   and/or modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.
#
#   lpschedule-generator is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with lpschedule-generator (see COPYING).  If not, see
#   <http://www.gnu.org/licenses/>.
VENV_DIR='.venv'
VENV_DIR3='.venv3'

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
	@$(MAKE) -C docs html

upload-docs: docs
	@rsync -avz --delete docs/_build/html/  $(LPSG_DOCS_HOST)

.PHONY: docs upload-docs

venv:
	rm -rf *.egg-info
	$(shell [[ -d $(VENV_DIR) ]] && mv $(VENV_DIR) $(VENV_DIR).`date +%s`)
	virtualenv --clear --python=python2.7 $(VENV_DIR)
	@echo 'Initialized virtualenv, run' \
		'source '$(VENV_DIR)'/bin/activate' \
		'to activate the virtual environment'
.PHONY: venv

venv3:
	rm -rf *.egg-info
	$(shell [[ -d $(VENV_DIR3) ]] && mv $(VENV_DIR3) $(VENV_DIR3).`date +%s`)
	virtualenv --clear --python=python3 $(VENV_DIR3)
	@echo 'Initialized virtualenv, run' \
		'source '$(VENV_DIR3)'/bin/activate' \
		'to activate the virtual environment'
.PHONY: venv3

clean-build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +

clean-venv:
	@rm -rf .venv*/

clean-docs:
	@$(MAKE) -C docs clean

.PHONY: clean-build clean-pyc clean-venv clean-docs

dev-env:
	pip install -r requirements.txt
	python setup.py develop

.PHONY: dev-env
