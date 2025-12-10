Linux Security Basics
Description

This project focuses on learning and practicing the fundamentals of Linux security. It covers essential concepts such as user permissions, file security, process management, system monitoring, and securing services. The goal is to understand how to protect a Linux system from unauthorized access and potential threats.

Topics Covered

Linux File System Hierarchy (FHS)

File permissions and ownership (chmod, chown, chgrp)

User and group management (useradd, usermod, groupadd)

Process management (ps, top, kill)

Network security basics (iptables, ufw, netstat)

Package and software updates

Logging and monitoring (journalctl, /var/log)

Basic hardening practices

Prerequisites

Linux operating system (Ubuntu, Debian, Kali Linux, or CentOS recommended)

Basic knowledge of Linux commands and terminal usage

Root or sudo access for executing administrative commands

Installation / Setup

Clone the repository:

git clone https://github.com/jdidi422/linux_security_basics.git


Navigate to the project directory:

cd linux_security_basics


Follow the exercises and scripts in the respective folders.

Usage

Each folder contains exercises or scripts for specific security concepts.

Use the terminal to run scripts or commands as instructed.

Always review scripts before executing to understand their effects.

Example Commands
# Check file permissions
ls -l /etc/passwd

# Change file permissions
chmod 644 file.txt

# Add a new user
sudo useradd newuser

# Monitor processes
top

Resources

Linux Security Basics

Linux Documentation Project

OWASP Linux Security

Author

Your Name – Your GitHub or contact info

License

This project is licensed under the MIT License – see the LICENSE file for details.
