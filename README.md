# Density On Prem Homework Assignment

- Documentation on how you would:
  * Deliver the final packages to a client
  * Document a strategy for building update packages (e.g., how would you specify code versions, especially across repos)
  * What tools or methods you would lean on for remote support of these applications once installed

Create a new repo using your Github account with a unique name and send us the final product!


## Build
This directory must be symlinked to a rpmbuild:
ln -s ~/density ~/rpmbuild

Edit OS version in Dockerfile and Makefile

make all
vagrant up

Making a request
```
curl -X POST -H 'Authorization: mytoken' http://127.0.0.1:5000/jobs
```
