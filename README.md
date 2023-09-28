# pyuyuni

Python library for controlling Uyuni / SUSE Manager.

## Requirements

This library uses the [JSON over HTTP API](https://www.uyuni-project.org/uyuni-docs-api/uyuni/api/scripts/json-http-login.html) that was introduced with Uyuni 2022.05 and is supported beginning with SUMA 4.3. The older XMLRPC API is **not** supported.

## Usage

Installation:

```command
$ python3 setup.py --user
```

Install for development purposes:

```command
$ python3 setup.py develop --user
```
