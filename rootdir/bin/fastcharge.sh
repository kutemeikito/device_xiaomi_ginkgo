#! /vendor/bin/sh

# Change permission for power_supply
chmod 777 /sys/class/power_supply/*/*

# Enable fast charging
echo '1' > /sys/kernel/fast_charge/force_fast_charge

# Disable input current limit
echo '0' > /sys/class/power_supply/battery/input_current_limited

# Set USB current max
echo '3000000' > /sys/class/power_supply/usb/current_max
echo '3000000' > /sys/class/power_supply/usb/hw_current_max
echo '3000000' > /sys/class/power_supply/usb/pd_current_max
echo '3000000' > /sys/class/power_supply/usb/ctm_current_max

# Set main current max
echo '3000000' > /sys/class/power_supply/main/current_max
echo '3000000' > /sys/class/power_supply/main/constant_charge_current_max
