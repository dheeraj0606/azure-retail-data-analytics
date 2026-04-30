#!/bin/bash

echo "Uploading data to Fabric Lakehouse..."

LAKEHOUSE_PATH="abfss://lakehouse@storageaccount.dfs.core.windows.net/bronze/"
LOCAL_FILE="data/sample_orders.csv"

if [ ! -f "$LOCAL_FILE" ]; then
  echo "File not found!"
  exit 1
fi

echo "Simulating upload..."
echo "File: $LOCAL_FILE → $LAKEHOUSE_PATH"

echo "Upload completed!"
