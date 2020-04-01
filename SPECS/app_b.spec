Name:           app_b
Version:        1
Release:        0
Summary:        Density On Prem Homework Assignment

Group:          DevOps
BuildArch:      noarch
License:        GPL
URL:            https://github.com/ztuakj/density#density-on-prem-homework-assignment
Source0:        app_b-1.0.tar.gz

%description
Write some description about your package here

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/density
install -m 0755 app_b.py $RPM_BUILD_ROOT/opt/density/app_b.py

%files
/opt/density
/opt/density/app_b.py

%changelog
* Mon Mar 30 2020 Jason Kautz  1.0
  - Initial rpm release
