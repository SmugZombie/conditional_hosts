#!/usr/bin/python
# hosts.py - Changes /etc/host based on preferences
# Smugzombie - github.com/smugzombie
version='0.0.1'

## Imports ##
import os
from shutil import copyfile

## Definitions ##
current_file='/etc/host.s/current'
active_hosts='/etc/hosts'
backup_hosts='/etc/host.s/hosts.backup'

## Functions ##
def build_hosts(hostsfile):
	base_file = '/etc/host.s/hosts.head'
	tmp_file = '/etc/host.s/tmphosts'
	with open(base_file, 'r') as f:
        	base_contents = f.read()

	if hostsfile != "head":
		with open("hosts."+hostsfile, 'r') as f:
			extra_contents = f.read()

		with open(tmp_file, 'w') as f:
			f.write(base_contents+extra_contents)
	else:
		with open(tmp_file, 'w') as f:
                        f.write(base_contents)

	copyfile(tmp_file,active_hosts)
	with open(current_file, 'w') as f:
		f.write(hostsfile)

with open(current_file, 'r') as f:
    current = str(f.readline().rstrip())

if current == "":
	print "No Current Configuration"
else:
	print "Current Hosts File: " + current

answered=False
while answered is False:
	print "Would you like to update this? (y/n)"
	answer = raw_input()
	if answer == 'y' or answer == 'n': answered = True;

if answer == 'y':
	copyfile(active_hosts, backup_hosts)

answered=False
while answered is False:
	print "What file would you like to load instead?"
#import os  
	valid_files = []
	for fn in os.listdir('.'):
		if "hosts." in fn and ".py" not in fn and ".bak" not in fn:
     			if os.path.isfile(fn):
	        		try:
					filename = (fn).split(".",1)[1]
				except:
					filename = ""
				if filename != "": print filename; valid_files.append(filename)  
	choice = raw_input()
	if choice in valid_files:
		answered = True
	else:
		answered = False
		
# Build and save the new hosts file
build_hosts(choice)
