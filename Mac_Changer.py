#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--Interface", dest="interface", help="Interface to Change MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please Specify Interface")
    elif not options.new_mac:
        parser.error("Please specify New MAC")
    return options

def change_mac(interface, new_mac):
    print("Changing MAC for "+ interface +" to "+new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
options = get_arguments()
change_mac(options.interface, options.new_mac)
