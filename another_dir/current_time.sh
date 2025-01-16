#!/bin/bash
end_hour=20
end_minute=0

current_time=$(date +"%H:%M")
current_hour=$(date +"%H")
current_minute=$(date +"%M")

remaining_hours=$((end_hour - current_hour))
remaining_minutes=$((end_minute - current_minute))
if [ $remaining_minutes -lt 0 ]; then
  remaining_minutes=$((remaining_minutes + 60))
  remaining_hours=$((remaining_hours - 1))
fi

echo "Current time: $current_time"
if [ $remaining_hours -ge 0 ]; then
  echo "Work day ends after $remaining_hours hours and $remaining_minutes minutes."
else
  echo "Work day has already ended!"
fi
