Name:           app_a
Version:        1
Release:        0
Summary:        Density On Prem Homework Assignment

Group:          DevOps
BuildArch:      noarch
License:        GPL
URL:            https://github.com/ztuakj/density#density-on-prem-homework-assignment
Source0:        app_a-1.0.tar.gz

Requires: python3 python3-flask python3-requests sqlite

%description
Write some description about your package here

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/density
install -m 0755 -d $RPM_BUILD_ROOT/opt/density/etc/init.d
install -m 0755 app_a.py $RPM_BUILD_ROOT/opt/density/app_a.py
install -m 0755 app_a.init $RPM_BUILD_ROOT/opt/density/etc/init.d/app_a.init

%files
/opt/density
/opt/density/app_a.py
/opt/density/etc/init.d/app_a.init

%changelog
* Mon Mar 30 2020 Jason Kautz  1.0
  - Initial rpm release
