#!/bin/bash
#generating secret file via ansible-vault
#req parameter=vault filename

echo 'Ansible vault file geneartion tool'

if [ "$*" == "" ]
then
    echo "Usage: $0 vault_file"
    exit 1
fi

if [ -f "$1" ]
then
    while true; do
    read -p "Vault file already exists. Replace it? " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo "Cancelling"; exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
fi

while [ -z "$HOST" ]; do
    read -p 'Enter hostname: ' HOST
done

while [ -z "$ADMIN" ]; do
    read -p 'Enter admin login: ' ADMIN
done

read -p 'Admin comment, optional: ' COMMENT1

while [ -z "$ADMINPASS" ]; do
    read -sp 'Provide admin password: ' ADMINPASS
done

while [ -z "$DOCTOR" ]; do
    read -p 'Enter user login: ' DOCTOR
done

read -p 'User comment, optional: ' COMMENT2

while [ -z "$USERPASS" ]; do
    read -sp 'Provide user password: ' USERPASS
done

while [ -z "$DOMAINPASS" ]; do
    read -sp 'Provide domain admin password: ' DOMAINPASS
done

HASH1=$(mkpasswd --method=sha-512 $ADMINPASS)
HASH2=$(mkpasswd --method=sha-512 $USERPASS)

#echo "host: $HOST; admin: $ADMIN, user: $USERN;"
echo "Creating vault file..."
printf "user1: '$ADMIN'
username1: '$COMMENT1'
password1: '$HASH1'
user2: '$DOCTOR'
username2: '$COMMENT2'
password2: '$HASH2'
hostname: '$HOST'
domain_password: '$DOMAINPASS'
domain: '.med.cap.ru'\n" > $1

ansible-vault encrypt $1
echo "Complete."