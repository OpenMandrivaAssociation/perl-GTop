%define	upstream_name	 GTop
%define	upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl interface to libgtop
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MJ/MJH/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	libgtop2.0-devel
Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl 

%description
GTop is a Perl interface to libgtop.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
