#Comando para dar formato y ejecutar codigo
.PHONY: format run tests mutants

format:
	black --check --line-length 100 src
	black --check --line-length 100 tests
	flake8 --max-line-length 100 src
	flake8 --max-line-length 100 tests

run:
	python src/kata.py
#Comando para iniciar las prueba
tests:
	pytest tests
#Comando para iniciar las mutaciones
#Las mutaciones deben ser al codigo no a las pruebas
mutants:
	mutmut run --paths-to-mutate src
	