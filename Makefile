#build[6-8] refers to OS version
all: setup build8
setup:
	cd ./SOURCES;tar cfz app_a-1.0.tar.gz app_a-1;tar cfz app_b-1.0.tar.gz app_b-1
build6:
	rpmbuild -bb SPECS/app_a-CentOS6.spec
	rpmbuild -bb SPECS/app_b-CentOS6.spec
build7:
	rpmbuild -bb SPECS/app_a-CentOS7.spec
	rpmbuild -bb SPECS/app_b-CentOS7.spec
build8:
	rpmbuild -bb SPECS/app_a-CentOS8.spec
	rpmbuild -bb SPECS/app_b-CentOS8.spec
clean:
	rm SOURCES/app_*gz
	rm -rf BUILD
	rm -rf BUILDROOT
