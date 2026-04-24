#!/bin/bash
cat dmesg | grep -m1 "Linux version" | cut -d' ' -f3
