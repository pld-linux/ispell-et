Summary:	Estonian dictionary for ispell
Name:		ispell-et
Version:	20030606
Release:	1
License:	LGPL
Group:		Applications/Text
Source0:	http://www.meso.ee/~jjpp/speller/%{name}_%{version}.tar.gz
# Source0-md5:	00c2351eed7a54c1fb2e3a529a960121
URL:		http://www.meso.ee/~jjpp/speller/
BuildRequires:	ispell
Requires:	ispell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Estonian dictionary (i.e. word list) for ispell.

%prep
%setup -q

%build
cd latin-1
buildhash estonian.dict estonian.aff estonian.hash

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ispell
install latin-1/estonian.aff $RPM_BUILD_ROOT%{_libdir}/ispell
install latin-1/estonian.hash $RPM_BUILD_ROOT%{_libdir}/ispell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog COPYRIGHT
%{_libdir}/ispell/*
