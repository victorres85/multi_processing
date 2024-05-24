#!/bin/bash

# Get the current date and time in the format Y-m-d-H-M
current_date=$(date +"%Y-%m-%d-%H-%M")

# Define the report file name with the current date and time
report_file="test_reports/${current_date}-report.html"

# Run pytest with the specified HTML report file name
pytest --html="$report_file"