#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: ./count_word.sh <file_name> <word>"
  exit 1
fi

file=$1
word=$2

if [ ! -f "$file" ]; then
  echo "File not found: $file"
  exit 1
fi

count=$(grep -o -w "$word" "$file" | wc -l)
echo "The word '$word' appears $count times in the file '$file'."
