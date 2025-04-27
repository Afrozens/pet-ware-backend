#!/bin/bash

# Let the DB start
python /app/app/pre_start.py
# Create initial data in DB
python /app/app/initial_data.py