#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Multiplex
Summary:	IO::Multiplex - manage IO on many file handles
Summary(pl.UTF-8):	IO::Multiplex - zarządzanie operacjami we/wy na wielu uchwytach plików
Name:		perl-IO-Multiplex
Version:	1.13
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a74f4c07a543cbf06ba3b24fe1be94e9
URL:		http://search.cpan.org/dist/IO-Multiplex/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Multiplex is designed to take the effort out of managing multiple
file handles. It is essentially a really fancy front end to the select
system call. In addition to maintaining the select loop, it buffers
all input and output to/from the file handles. It can also accept
incoming connections on one or more listen sockets.

%description -l pl.UTF-8
Moduł IO::Multiplex został zaprojektowany jako próba zarządzania
wieloma uchwytami plików. Jest przede wszystkim naprawdę fantazyjnym
frontendem do wywołania systemowego select. Oprócz zarządzania pętlą
wywołań select, buforuje całe wejście i wyjście do/z uchwytów plików.
Może także akceptować przychodzące połączenia z jednego lub więcej
nasłuchujących gniazd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/IO/Multiplex.pm
%{_mandir}/man3/*
