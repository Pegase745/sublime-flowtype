check:
	flake8 --max-complexity 7 flowtype/**/*.py

	pylint --rcfile .pylintrc -E flowtype

lint:
	pylint --rcfile .pylintrc flowtype

test:
	pytest tests/**/*.py