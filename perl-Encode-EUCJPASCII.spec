%define upstream_name    Encode-EUCJPASCII
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    EucJP-ascii - An eucJP-open mapping
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Encode/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides eucJP-ascii, one of eucJP-open mappings, and its
derivative. Following encodings are supported.

  Canonical    Alias                           Description
  --------------------------------------------------------------
  eucJP-ascii                                  eucJP-ascii
               qr/\beuc-?jp(-?open)?(-?19970715)?-?ascii$/i
  x-iso2022jp-ascii                            7-bit counterpart
               qr/\b(x-)?iso-?2022-?jp-?ascii$/i
  --------------------------------------------------------------

*Note*: 'x-iso2022jp-ascii' is unofficial encoding name: It had never been
registered by any standards bodies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std DESTDIR=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%perl_vendorlib/*
