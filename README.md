## Introduction
For GIT (Github) testing only! Tool for generating secret file with credentials for Astra and Ubuntu linux setup via Ansible.
## Current Releases
0.1 - bash script variant added. <br />
0.2 - python script added. <br />
0.3 - new fields in script: _domain_controller_ and _domain_ou_
## Platforms
Any Linux. For python gensecrets.py Python3 required.
## Usage
Typical usage:
> ./gensecrets.sh vars/secrets.yml or ./gensecrets.py vars/secrets.yml
## Result yml file example
user1: `'admin'`<br />
username1: `'Admin'`<br />
password1: `'$6$ThyF71IwgHcNfU.Q$rWNU1QS1I4rNy/MnmvBhjrMg7GbV842y8W4ks5n/RU1dP6rkq6BE.R3mk7HRMEHeXy.lXcggjiqC.yrCEbfnp/'`<br />
user2: `'user'`<br />
username2: `'User'`<br />
password2: `'$6$80fQ07cUePbxOu1t$RonxIz.fD1up1rH65jvwQwGKL5fcP9K3lDKzh9CxU0Cdn9lrRlyImv41L0aEqM58GNFL8JF4pvgLsGp8ni7J2.'`<br />
hostname: `'amb1-10'`<br />
domain_admin: `'superadmin'`<br />
domain_password: `'Quazar'`<br />
domain: `'.domain.com'`<br />
domain_ou: `'OU=OFFICE,DC=domain,DC=ru'`<br />
domain_controller: `'192.168.1.2'`
## Licenses
Use and modify on your own risk.