Name:           app_b
Version:        1
Release:        0
Summary:        Density On Prem Homework Assignment

Group:          DevOps
BuildArch:      noarch
License:        GPL
URL:            https://github.com/ztuakj/density#density-on-prem-homework-assignment
Source0:        app_b-1.0.tar.gz

Requires: python python-flask python-requests sqlite

%description
Write some description about your package here

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/density
install -m 0755 -d $RPM_BUILD_ROOT/opt/density/etc/init.d
install -m 0755 app_b.py $RPM_BUILD_ROOT/opt/density/app_b.py
install -m 0755 schema.sql $RPM_BUILD_ROOT/opt/density/schema.sql
install -m 0755 app_b.init $RPM_BUILD_ROOT/opt/density/etc/init.d/app_b.init

%files
/opt/density
/opt/density/app_b.py
/opt/density/schema.sql
/opt/density/etc/init.d/app_b.init

%changelog
* Mon Mar 30 2020 Jason Kautz  1.0
  - Initial rpm release
