install:
	poetry install

gendiff:
	poetry run gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

make lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest 
	poetry run coverage xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: gendiff