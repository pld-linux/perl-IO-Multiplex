#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Multiplex
Summary:	IO::Multiplex - Manage IO on many file handles
Summary(pl):	IO::Multiplex - zarz±dzanie operacjami we/wy na wielu uchwytach plików
Name:		perl-IO-Multiplex
Version:	1.04
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Multiplex is designed to take the effort out of managing multiple
file handles. It is essentially a really fancy front end to the select
system call. In addition to maintaining the select loop, it buffers
all input and output to/from the file handles. It can also accept
incoming connections on one or more listen sockets.

%description -l pl
Modu³ IO::Multiplex zosta³ zaprojektowany jako próba zarz±dzania
wieloma uchwytami plików. Jest przede wszystkim naprawdê fantazyjnym
frontendem do wywo³ania systemowego select. Oprócz zarz±dzania pêtl±
wywo³añ select, buforuje ca³e wej¶cie i wyj¶cie do/z uchwytów plików.
Mo¿e tak¿e akceptowaæ przychodz±ce po³±czenia z jednego lub wiêcej
nas³uchuj±cych gniazd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_sitelib}/IO/Multiplex.pm
%{_mandir}/man3/*
