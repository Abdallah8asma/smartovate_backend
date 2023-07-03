#!/bin/bash
#
# Check lint rules on the Python code.
# This code assumes that the caller has installed the testing requirements
# in test_requirements.txt.
#
# Read more here: https://github.com/Tradias-GmbH/tradias.pricesource
# Proprietary and confidential. Copyright Tradias-GmbH 2021

set -o xtrace
mypy --allow-untyped-decorators --ignore-missing-imports --config-file pyproject.toml caustaza/*.py tests/*.py
pre-commit install
git ls-files -- '*.py' | xargs pre-commit run --files
exit_code="$?"
if [ $exit_code -ne 0 ]
then
exit $exit_code
fi
pylint --rcfile=pylintrc --fail-under=0.5 caustaza tests
