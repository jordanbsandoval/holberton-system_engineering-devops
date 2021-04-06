# Make changes to ssh configuration file using Puppet
file_line {'Declare identity file':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/holberton',
}
file_line {'Refuse password authorization':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}