%define	module	GTop
%define	name	perl-%{module}
%define	version	0.16
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to libgtop
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MJ/MJH/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}
Buildrequires:	perl-devel
BuildRequires:	libgtop2.0-devel
Requires:	perl 

%description
GTop is a Perl interface to libgtop.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{perl_vendorarch}/config.pl
%{perl_vendorarch}/GTop*
%{perl_vendorarch}/auto/GTop
%{_mandir}/*/*
