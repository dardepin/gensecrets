## Introduction
For GIT (Github) testing only! Tool for generating secret file with credentials for Astra linux setup via Ansible.
## Current Releases
0.1 - bash script variant added.
0.2 - python script added.
## Platforms
Any Linux. For python gensecrets.py Python3 required.
### Usage
Typical usage: ./gensecrets.sh vars/secrets.yml or ./gensecrets.py vars/secrets.yml
## Result yml file example
user1: 'admin'
username1: 'Admin'
password1: '$6$ThyF71IwgHcNfU.Q$rWNU1QS1I4rNy/MnmvBhjrMg7GbV842y8W4ks5n/RU1dP6rkq6BE.R3mk7HRMEHeXy.lXcggjiqC.yrCEbfnp/'
user2: 'user'
username2: 'User'
password2: '$6$80fQ07cUePbxOu1t$RonxIz.fD1up1rH65jvwQwGKL5fcP9K3lDKzh9CxU0Cdn9lrRlyImv41L0aEqM58GNFL8JF4pvgLsGp8ni7J2.'
hostname: 'amb1-10'
domain_admin: 'superadmin'
domain_password: 'Quazar'
domain: '.domain.com'
## Licenses
Use and modify on your own risk.