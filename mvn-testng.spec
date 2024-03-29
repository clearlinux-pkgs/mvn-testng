#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-testng
Version  : 6.3.1
Release  : 1
URL      : https://github.com/cbeust/testng/archive/testng-6.3.1.tar.gz
Source0  : https://github.com/cbeust/testng/archive/testng-6.3.1.tar.gz
Source1  : https://repo1.maven.org/maven2/org/testng/testng/6.3.1/testng-6.3.1.jar
Source2  : https://repo1.maven.org/maven2/org/testng/testng/6.3.1/testng-6.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-testng-data = %{version}-%{release}
Requires: mvn-testng-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
Welcome to TestNG
Please note that even though the .zip distribution contains the TestNG sources,
you will not be able to build the software with them because we decided
not to include the external jar files in order to keep the size down.

%package data
Summary: data components for the mvn-testng package.
Group: Data

%description data
data components for the mvn-testng package.


%package license
Summary: license components for the mvn-testng package.
Group: Default

%description license
license components for the mvn-testng package.


%prep
%setup -q -n testng-testng-6.3.1

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-testng
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-testng/LICENSE.txt
cp spring/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-testng/spring_LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/testng/testng/6.3.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/testng/testng/6.3.1/testng-6.3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/testng/testng/6.3.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/testng/testng/6.3.1/testng-6.3.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/testng/testng/6.3.1/testng-6.3.1.jar
/usr/share/java/.m2/repository/org/testng/testng/6.3.1/testng-6.3.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-testng/LICENSE.txt
/usr/share/package-licenses/mvn-testng/spring_LICENSE.txt
