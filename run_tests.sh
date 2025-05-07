#!/bin/bash
# run_tests.sh

echo "Executando testes com cobertura..."

pytest --rootdir=. \
  --cov=. \
  --cov-report=term \
  -v \
  -q
