#!/bin/bash
last -n 6 | grep -v "reboot" | head -n 5
