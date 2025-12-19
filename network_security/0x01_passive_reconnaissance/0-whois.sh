#!/bin/bash

domain="$1"

whois "$domain" | awk -F: '
BEGIN { sec="" }

/^Registrant / { sec="Registrant" }
/^Admin /      { sec="Admin" }
/^Tech /       { sec="Tech" }

sec != "" {
    if ($1 ~ /Name$/ && !name[sec])              name[sec]=$2
    else if ($1 ~ /Organization$/ && !org[sec]) org[sec]=$2
    else if ($1 ~ /Street$/ && !street[sec])    street[sec]=$2 " "
    else if ($1 ~ /City$/ && !city[sec])        city[sec]=$2
    else if ($1 ~ /State\/Province$/ && !state[sec]) state[sec]=$2
    else if ($1 ~ /Postal Code$/ && !zip[sec])  zip[sec]=$2
    else if ($1 ~ /Country$/ && !country[sec])  country[sec]=$2
    else if ($1 ~ /^Phone$/ && !phone[sec])     phone[sec]=$2
    else if ($1 ~ /^Fax$/ && !fax[sec])         fax[sec]=$2
    else if ($1 ~ /Email$/ && !email[sec])      email[sec]=$2
}

END {
    split("Registrant Admin Tech", order, " ")
    for (i = 1; i <= 3; i++) {
        s = order[i]
        print s " Name," name[s]
        print s " Organization," org[s]
        print s " Street," street[s]
        print s " City," city[s]
        print s " State/Province," state[s]
        print s " Postal Code," zip[s]
        print s " Country," country[s]
        print s " Phone," phone[s]
        print s " Phone Ext:,";
        print s " Fax," fax[s]
        print s " Fax Ext:,";
        print s " Email," email[s] # هذا يضمن Email Tech موجود
    }
}
' > "$domain.csv"

