#!/bin/bash
grep -m1 "Linux version" dmesg | awk '{print $3}'
