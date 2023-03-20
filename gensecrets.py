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

def save2vault(hostname, adminname, admincomment, adminhash, username, usercomment, userhash, domainpass, domain, domainadmin, domainou, domaincontroller):
    print('Creating vault file');
    with open(sys.argv[1], 'w+') as vaultfile:
        vaultfile.write("user1: '{0}'\nusername1: '{1}'\npassword1: '{2}'\nuser2: '{3}'\nusername2: '{4}'\npassword2: '{5}'\ndomain_admin: '{6}'\ndomain_password: '{7}'\ndomain: '{8}'\ndomain_ou: '{9}'\ndomain_controller: '{10}'\nhostname: '{11}'\n".format(adminname, admincomment, adminhash, username, usercomment, userhash, domainadmin, domainpass, domain, domainou, domaincontroller, hostname));
    return;

def crypt2vault():
    try:
        subprocess.check_output("ansible-vault encrypt " + sys.argv[1], shell=True);
    except Exception as error:
        print('ERROR: ', error);
        exit();
    return;

#main()
if len(sys.argv) < 2:
    usage(True);
if not sys.argv[1].endswith('.yml'):
    usage(True);
rewrite();

try:
    #adminname = sys.stdin.readline().rstrip()
    hostname = ""; adminname = ""; adminpass = ""; admincomm = "";
    username = ""; userpass = ""; usercomm = "";
    domain = ""; domainadmin = ""; domainpass = "";
    domainou= ""; domaincontroller = "";

    while len(hostname) == 0:
        hostname = input('Hostname: ');
    while len(adminname) == 0:
        adminname = input('Admin login: ');
    while len(adminpass) == 0:
        adminpass = getpass.getpass('Admin password: ');
    while len(admincomm) == 0:
        admincomm = input('Admin comment: ');
    while len(username) == 0:
        username = input('User login: ');
    while len(userpass) == 0:
        userpass = getpass.getpass('User password: ');
    while len(usercomm) == 0:
        usercomm = input('User comment: ');

    while len(domain) == 0:
        domain = input('Domain (without first dot): ')
    while len(domaincontroller) == 0:
        domaincontroller = input('Domain controller address: ');
    while len(domainou) == 0:
        domainou = input('Domain ou: ');
    while len(domainadmin) == 0:
        domainadmin = input('Domain admin: ');
    while len(domainpass) == 0:
        domainpass = getpass.getpass('Domain password: ');
except Exception as error:
    print('ERROR: ', error);
    exit();
else:
    adminhash = subprocess.check_output("mkpasswd --method=sha-512 " + adminpass, shell=True);
    userhash = subprocess.check_output("mkpasswd --method=sha-512 " + userpass, shell=True);

    save2vault(hostname, adminname, admincomm, adminhash.decode("utf-8").strip(), username, usercomm, userhash.decode("utf-8").strip(), domainpass, domain, domainadmin, domainou, domaincontroller);
    crypt2vault();
    print('COMPLETE!');
