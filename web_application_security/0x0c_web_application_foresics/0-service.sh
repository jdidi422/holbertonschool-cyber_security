#!/bin/bash

grep -oE 'sshd|ftp|apache|nginx' *.log | sort | uniq -c | sort -nr
