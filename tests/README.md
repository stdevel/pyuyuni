# tests

## Running tests using Vagrantboxes

The `Vagrant` directory contains a [`Vagrantfile`](Vagrant/Vagrantfile) for creating your own testing environment. Simply start it using:

```shell
$ vagrant up
```

After having the machines up and running you can link your tests again the Vagrant test configurations:

```shell
$ ln -s uyuni_config.yml.vagrant uyuni_config.yml
```

Now you can run `pytest` against the APIs running in VMs - e.g.:

```shell
$ pytest test_login.py
```
