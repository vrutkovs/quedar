check:
	pipenv check

test:
	pipenv install --system -d
	python3 -m pytest
