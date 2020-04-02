all: setup build
	echo "setup and build..."
setup:
	cd ./SOURCES;tar cfz app_a-1.0.tar.gz app_a-1;tar cfz app_b-1.0.tar.gz app_b-1
build:
	rpmbuild -bb SPECS/app_a.spec
	rpmbuild -bb SPECS/app_b.spec
clean:
	rm SOURCES/app_*gz
	rm -rf BUILD
	rm -rf BUILDROOT
