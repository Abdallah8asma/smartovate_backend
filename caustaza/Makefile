# Makefile: Automation for local building and testing.
#
# Read more here: https://github.com/Tradias-GmbH/tradias.pricesource
# Proprietary and confidential. Copyright Tradias-GmbH 2021


SHELL := /bin/bash
SOURCE_VENV := source venv/bin/activate

# Python definitions. Support Python 3.9 and 3.10 on GH workflow
PYTHON_INTERPRETER := python3.9
PIP := $(PYTHON_INTERPRETER) -m pip
VENV_DIR = venv

DOCKER_SERVER_IMAGE_TAG := caustaza-service
DOCKER_IMAGE_VERSION := latest
DOCKER_EXPOSE_PORT := 8080
PIP := python -m pip

# Env variables for different providers


.PHONY: clean lint unit_tests redis docker_build docker_run serve


# Removes the existing virtual environment, if exists
clean:
	rm -rf venv server/__pycache__ tests/__pycache__


# Create a Python virtual environment
# $(SOURCE_VENV) && $(PIP) install proto/tradias_proto*.whl
# $(SOURCE_VENV) && $(PIP) install -r requirements.txt
# excluded .whl because we dont have it yet, for testing purposes we excluded requirements.txt as well.

# !IMPORTANT, in order to fix psycopg2 error, you need to install gcc and libpq-dev, which already taken care of.
venv:
	sudo apt-get -y install libpq-dev && sudo apt-get -y install gcc
	$(PYTHON_INTERPRETER) -m venv $(VENV_DIR)
	$(SOURCE_VENV) && $(PIP) install --upgrade pip
	$(SOURCE_VENV) && $(PIP) install -r requirements_test.txt

# Lint-check the code in the virtual environment
lint: venv
	$(SOURCE_VENV) && scripts/lint.sh

# Package the code to a docker container image
docker_build:
	docker build -t $(DOCKER_SERVER_IMAGE_TAG):$(DOCKER_IMAGE_VERSION) -f Dockerfile .

docker_clean:
	docker ps -q    | xargs -r docker kill
	docker ps -a -q | xargs -r docker rm
	docker image prune -a --force


# Test the code in the virtual environment
unit_tests: venv
	$(SOURCE_VENV) && python -m pytest

# function for running docker image based on given env variables
define run_provider
	docker run --init -it --rm --name caustaza --network host --env-file .env --env PROVIDER=$(1) --env URI=$(2) --env TOKEN=$(3) -p $(DOCKER_EXPOSE_PORT):8080 $(DOCKER_SERVER_IMAGE_TAG):$(DOCKER_IMAGE_VERSION)
endef
