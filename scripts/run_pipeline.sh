#!/bin/bash

echo "Starting pipeline execution..."

python3 synapse/spark/pipeline_runner.py

if [ $? -ne 0 ]; then
  echo "Pipeline failed!"
  exit 1
fi

echo "Pipeline executed successfully!"
