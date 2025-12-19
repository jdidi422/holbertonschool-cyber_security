#!/bin/bash
# 2-mx_record.sh
# Usage: ./2-mx_record.sh domain

domain="$1"

# nslookup command to get MX records and filter the output
nslookup -type=mx "$domain" 2>/dev/null | awk -F'= ' '/mail exchanger/ {print $2}'

