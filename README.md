# Density On Prem Homework Assignment

## Build
make all
## Test
You'll need to install: docker, vagrant (optional), rpmbuild

This directory must be symlinked to a rpmbuild:
ln -s ~/density ~/rpmbuild

Edit OS version in Dockerfile and Makefile


make all

vagrant up (or docker build)

You can log into the docker container and make a request:
```
curl -X POST -H 'Authorization: mytoken' http://127.0.0.1:5000/jobs
```
## Updates
major.minor[.maintenance[.build]]

## Client Delivery
The rpm can be installed via a repository hosted remotely by us or installed locally with provided checksum.

