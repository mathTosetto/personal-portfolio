.PHONY: install activate

install:
	echo "Definining the poetry configs..."
	poetry config virtualenvs.in-project true

	echo "Installing the dependencies..."
	poetry install --quiet

	echo "Installing pre-commit..."
	pre-commit install

activate:
	eval $(poetry env activate)
