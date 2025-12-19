#!/bin/bash

whois "$1" | awk -F': ' '
BEGIN {
    order[1]="Name"
    order[2]="Organization"
    order[3]="Street"
    order[4]="City"
    order[5]="State/Province"
    order[6]="Postal Code"
    order[7]="Country"
    order[8]="Phone"
    order[9]="Phone Ext:"
    order[10]="Fax"
    order[11]="Fax Ext:"
    order[12]="Email"

    sections[1]="Registrant"
    sections[2]="Admin"
    sections[3]="Tech"
}

{
    if ($1 ~ /^(Registrant|Admin|Tech) /) {
        split($1, a, " ")
        sec = a[1]
        field = substr($1, length(sec) + 2)
        data = $2
        values[sec, field] = data
    }
}

END {
    for (s = 1; s <= 3; s++) {
        sec = sections[s]
        for (i = 1; i <= 12; i++) {
            field = order[i]
            val = values[sec, field]

            if (field == "Street")
                printf "%s %s,%s \n", sec, field, val
            else
                printf "%s %s,%s\n", sec, field, val
        }
    }
}
' > "$1.csv"

# remove last newline
truncate -s -1 "$1.csv"

