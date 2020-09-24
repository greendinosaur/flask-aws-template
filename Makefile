
cwd:= $(shell pwd)

MODULE := my_app.py
MY_SECRET := $(shell python -c 'import os; print(os.urandom(16))')

BLUE='\033[0;34m'
NC='\033[0m' # No Color

# This version-strategy uses git tags to set the version string
TAG := $(shell git describe --tags --always --dirty)

run:
	@flask run

test:
# pytest is not generating coverage data files for some reason
# using coverage directly
#	@pytest
	@coverage run -m pytest 
	@coverage xml

lint:
	@echo "\n${BLUE}Running Pylint against source and test files...${NC}\n"
	@pylint --rcfile=setup.cfg app
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8
	@echo "\n${BLUE}Running Bandit against source files...${NC}\n"
	@bandit -r --ini setup.cfg

sonar:
	@sonar-scanner

version:
	@echo $(TAG)

.PHONY: clean test

clean:
	@echo "removing old files"
	@rm -rf .pytest_cache __pycache__ tests/__pycache__ .coverage tests/.pytest_cache
	@rm -f coverage.xml



