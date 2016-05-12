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
test:
	@nosetests

build-dist:
	@python setup.py sdist bdist_wheel

egg:
	@python setup.py egg_info

upload:
	@twine upload -r pypi -s -i rsd@gnu.org dist/*.tar.gz
	@twine upload -r pypi -s -i rsd@gnu.org dist/*.whl

docs:
	@$(MAKE) -C docs html

clean-build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +

clean-venv:
	@rm -rf bin/
	@rm -rf include/
	@rm -rf lib/
	@rm -rf local/
	@rm -rf man/

dev-packages:
	@pip install -U nose mock restructuredtext_lint
	@pip install -U wheel twine
	@pip install -U Sphinx

.PHONY: dist clean-build upload build-dist egg clean-pyc clean-venv
.PHONY: dev-packages docs
