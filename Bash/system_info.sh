#!/bin/bash
# Script to display system information

echo "=== System Information ==="
echo "Hostname: $(hostname)"
echo "Uptime: $(uptime -p)"
echo "Logged in users:"
who
echo "Disk Usage:"
df -h
