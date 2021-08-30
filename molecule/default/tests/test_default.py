"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_ssh_directory(host):
    """Validate ~/.ssh directory."""
    ssh = host.file("/root/.ssh")

    assert ssh.exists
    assert ssh.is_directory
    assert ssh.user == "root"
    assert ssh.group == "root"
    assert ssh.mode == 0o700


def test_ssh_private_key(host):
    """Validate SSH private key."""
    key = host.file("/root/.ssh/id_rsa")

    assert key.exists
    assert key.user == "root"
    assert key.group == "root"
    assert key.mode == 0o600
    assert key.content == b"ssh-private-key"


def test_ssh_public_key(host):
    """Validate SSH public key."""
    key = host.file("/root/.ssh/id_rsa.pub")

    assert key.exists
    assert key.user == "root"
    assert key.group == "root"
    assert key.mode == 0o644
    assert key.content == b"ssh-public-key"


def test_ssh_known_hosts(host):
    """Validate SSH known_hosts."""
    known_hosts = host.file("/root/.ssh/known_hosts")

    assert known_hosts.exists
    assert known_hosts.user == "root"
    assert known_hosts.group == "root"
    assert known_hosts.mode == 0o644
    assert known_hosts.content == b"ssh-known-hosts"
