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
REDIS_URL := redis://172.18.0.2
BINANCE_PROVIDER=binance
BINANCE_URI=wss://stream.binance.com:9443/stream
BITSTAMP_PROVIDER=bitstamp
BITSTAMP_URI=wss://ws.bitstamp.net
KRAKEN_PROVIDER=kraken
KRAKEN_URI=wss://ws.kraken.com
COINBASE_PROVIDER=coinbase
COINBASE_URI=wss://ws-feed.exchange.coinbase.com
B2C2_PROVIDER=b2c2
B2C2_URI=wss://socket.uat.b2c2.net/quotes
B2C2_TOKEN=c9e56959414344c15b0039b5f835cab595746b63

.PHONY: clean lint unit_tests redis docker_build docker_run serve


# Removes the existing virtual environment, if exists
clean:
	rm -rf venv server/__pycache__ tests/__pycache__


# Create a Python virtual environment
# $(SOURCE_VENV) && $(PIP) install proto/tradias_proto*.whl
# $(SOURCE_VENV) && $(PIP) install -r requirements.txt
# excluded those because we dont have them yet, i guess.
venv:
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

# Run redis
redis:
		docker-compose up -d redis

# function for running docker image based on given env variables
define run_provider
	docker run --init -it --rm --name caustaza --network host --env-file .env --env PROVIDER=$(1) --env URI=$(2) --env TOKEN=$(3) -p $(DOCKER_EXPOSE_PORT):8080 $(DOCKER_SERVER_IMAGE_TAG):$(DOCKER_IMAGE_VERSION)
endef

# Call run_provider for kraken
run_kraken:
		$(call run_provider,$(KRAKEN_PROVIDER),$(KRAKEN_URI))

# Call run_provider for bitstamp
run_bitstamp:
		$(call run_provider,$(BITSTAMP_PROVIDER),$(BITSTAMP_URI))

# Call run_provider for binance
run_binance:
		$(call run_provider,$(BINANCE_PROVIDER),$(BINANCE_URI))

# Call run_provider for coinbase
run_coinbase:
		$(call run_provider,$(COINBASE_PROVIDER),$(COINBASE_URI))

# Call run_provider for b2c2
run_b2c2:
		$(call run_provider,$(B2C2_PROVIDER),$(B2C2_URI),$(B2C2_TOKEN))
