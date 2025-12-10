# 0x00 Linux Security Basics

This project introduces fundamental Linux security concepts and essential command-line skills used to analyze, protect, and monitor Linux systems.

## Learning Objectives

By the end of this project, you should be able to explain:

- What Linux is  
- What a Linux command is  
- The structure of the Linux operating system  
- The purpose and benefits of the Filesystem Hierarchy Standard (FHS)  
- The different directories in the Linux file system and their purposes  
- How to protect files and directories  
- How to monitor and investigate system activity  
- How to securely transfer files and data  
- How to configure and manage a firewall  
- How to identify and terminate malicious processes  

### Working with Commands

You should also be able to use:

- `ps` and `kill` to identify and terminate malicious processes  
- `netstat` and `ss` to monitor suspicious network activity  
- `nmap`, `lynis`, and `tcpdump` to analyze network traffic  
- `iptables` and `ufw` to manage firewall rules on Linux systems  

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`  
- All scripts tested on **Kali Linux**  
- All scripts must be exactly **2 lines long**  
- You must substitute the IP range using `$1`  
- All files must end with a new line  
- First line of all scripts: `#!/bin/bash`  
- You must follow **Betty style** (checked with `betty-style.pl` and `betty-doc.pl`)  
- Backticks, `&&`, `||`, and `;` are **not allowed**  
- All files must be executable  
- A `README.md` is mandatory

## Tasks

### 0. What secrets hold

Write a Bash script that displays the last **5 login sessions** for all users, including their dates and times.

**Usage:**


