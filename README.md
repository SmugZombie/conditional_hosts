# Conditional Hosts - hosts.py

0.0.1 Installation:<br>
Create new directory: /etc/host.s/<br>
Upload these files here:<br>


0.0.1 Use:<br>
/: <strong>python /etc/host.s/hosts.py</strong>
<pre>
root@It-Guy-Nix:/etc/host.s# <strong>python hosts.py</strong> 
Current Hosts File: head
Would you like to update this? (y/n)
<strong>y</strong>
What file would you like to load instead?
head
io
backup
<strong>io</strong>
</pre>

At this point the previous hosts file is backed up to /etc/host.s/hosts.backup, the chosen file is merged with the head file and written to /etc/host.s/tmpfile. Which is then copied to /etc/hosts overwriting the old file.
