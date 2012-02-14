%define _prefix /usr/bin

Name:		pwauth
Version:	%{ver}
Release:	2%{?dist}
Summary:	Pwauth
License:	GPL
URL:		http://lucene.apache.org/solr/
Source: 	http://pwauth.googlecode.com/files/pwauth-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: 	pam-devel
BuildRequires: 	gcc
BuildArch:	x86_64

%description
%{summary}
%
%prep
%setup -q -n pwauth-%{version}


%build

%install
rm -rf $RPM_BUILD_ROOT
sed -i "s/\/\* #define PAM\t/#define PAM/g" config.h
sed -i "s/#define SHADOW_SUN/\/\* #define SHADOW_SUN/g" config.h
sed -i "s/#define SERVER_UIDS 30/#define SERVER_UIDS 302,510/g" config.h
sed -i "s/#define MIN_UNIX_UID 500/#define MIN_UNIX_UID 300/g" config.h
sed -i "s/LIB= -lcrypt/LIB= -lpam/g" Makefile
make
mkdir -p %{buildroot}%{_prefix}
%__install -D -m6755 pwauth "%{buildroot}%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,root,root,-)
%attr(6755,root,root) %{_prefix}/pwauth

%changelog
* Tue Feb 14 2012 Jean-Francois Roche <jfroche@affinitic.be>
- Initial implementation
