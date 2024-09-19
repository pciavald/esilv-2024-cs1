#!/bin/bash

# %Y year
YEAR=$(date +%Y)
# year override
# YEAR=1969

# reset previously generated calendar
rm -rf $YEAR
mkdir $YEAR

# iterate on months, padding with 0
for MONTH in $(seq -f %02g 1 12); do
  mkdir $YEAR/$MONTH

  # get month length by adding a month and subtracting a day
  # %d day of month (e.g., 01)
  DAYS=$(date -d "$YEAR-$MONTH-01 + 1 month - 1 day" +%d)

  # iterate on days, padding with 0
  for DAY in $(seq -f %02g 1 $DAYS); do

    # get day of week
    # %A locale's full weekday name (e.g., Sunday)
    DAY_NAME=$(date -d "$YEAR-$MONTH-$DAY" +%A)

    # write day file
    echo "$YEAR/$MONTH/$DAY is a $DAY_NAME" > $YEAR/$MONTH/$DAY.txt
  done

done
