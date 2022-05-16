#!/usr/bin/python3
import os;
import sys;
import getpass;
import subprocess;
print('Ansible vault file gen tool');

def usage(toexit):
    print('Usage: ' + sys.argv[0] + ' vault_file.yml')
    if(toexit == True):
        exit();
    return;

def rewrite():
    if os.path.exists(sys.argv[1]):
        delfile = input('Vault file already exists. Replace it?');
        if delfile in ['yes', 'Yes', 'y']:
            os.remove(sys.argv[1]);
        else: exit();
    return;

def save2vault(hostname, adminname, admincomment, adminhash, username, usercomment, userhash, domainpass, domain, domainadmin):
    print('Creating vault file');
    with open(sys.argv[1], 'w+') as vaultfile:
        vaultfile.write("user1: '{0}'\nusername1: '{1}'\npassword1: '{2}'\nuser2: '{3}'\nusername2: '{4}'\npassword2: '{5}'\ndomain_admin: '{6}'\ndomain_password: '{7}'\ndomain: '{8}'\nhostname: '{9}'\n".format(adminname, admincomment, adminhash, username, usercomment, userhash, domainadmin, domainpass, domain, hostname));
    return;

def crypt2vault():
    subprocess.check_output("ansible-vault encrypt " + sys.argv[1], shell=True);
    return;

#main()
if len(sys.argv) < 2:
    usage(True);
if not sys.argv[1].endswith('.yml'):
    usage(True);
rewrite();

try:
    #adminname = sys.stdin.readline().rstrip()
    hostname = input('Hostname: ');
    adminname = input('Admin login: ');
    adminpass = getpass.getpass('Admin password: ');
    admincomm = input('Admin comment: ');

    username = input('User login: ');
    userpass = getpass.getpass('User password: ');
    usercomm = input('User comment: ');

    domain = input('Domain (without first dot): ')
    domainadmin = input('Domain admin: ');
    domainpass = getpass.getpass('Domain password: ');
except Exception as error:
    print('ERROR', error);
    exit();
else:
    adminhash = subprocess.check_output("mkpasswd --method=sha-512 " + adminpass, shell=True);
    userhash = subprocess.check_output("mkpasswd --method=sha-512 " + userpass, shell=True);

    save2vault(hostname, adminname, admincomm, adminhash.decode("utf-8").strip(), username, usercomm, userhash.decode("utf-8").strip(), domainpass, domain, domainadmin);
    crypt2vault();
    print('Complete');
