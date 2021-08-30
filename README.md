# ansible-ssh-config

Configure a single user for SSH client.

## Variables

Name | Description | Required?
---- | ----------- | ---------
ssh_user | Username to configure | Y
ssh_home_dir | Home directory of the user | Y
ssh_private_key | File content of your private key | Y
ssh_public_key | File content of your public key | Y
ssh_known_hosts | File content of your SSH known_hosts | N
