# uyuni

This folder contains a Vagrant configuration and Ansible playbook for installing Uyuni 2023.04 on openSUSE Leap 15.4.

## Requirements

For this demo, you'll need:

- Oracle VirtualBox
- HashiCorp Vagrant
- Ansible

## Usage

Install Ansible requirements:

```shell
$ ansible-galaxy install -r requirements.yml
```

Run `vagrant` in order to create the VM and configure Uyuni. This can take up to 40 minutes:

```shell
$ vagrant up
```

Access the web interface via [https://localhost:8443](https://localhost:8443) (VirtualBox) or [https://192.168.56.10](https://192.168.56.10) (libvirt) afterwards.
