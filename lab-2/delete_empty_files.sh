#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: ./delete_empty_files.sh <directory>"
  exit 1
fi

directory=$1

if [ ! -d "$directory" ]; then
  echo "Directory not found: $directory"
  exit 1
fi

empty_files=$(find "$directory" -type f -empty)
if [ -z "$empty_files" ]; then
  echo "No empty files found in directory '$directory'."
else
  echo "Deleting empty files:"
  for file in $empty_files; do
    echo "Deleted: $file"
    rm "$file"
  done
fi
