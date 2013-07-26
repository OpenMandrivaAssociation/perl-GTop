%define	upstream_name	 GTop
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.18
Release:	1

Summary:	Perl interface to libgtop
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/M/MJ/MJH/GTop-0.18.tar.gz

BuildRequires:	pkgconfig(libgtop-2.0)
Buildrequires:	perl-devel
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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.170.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1
+ Revision: 690262
- update to new version 0.17

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 409301
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.16-2mdv2009.0
+ Revision: 268514
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 30 2008 Olivier Blin <blino@mandriva.org> 0.16-1mdv2009.0
+ Revision: 199735
- initial perl-GTop package
- create perl-GTop


