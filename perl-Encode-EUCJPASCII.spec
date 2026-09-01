%define	upstream_name	Encode-EUCJPASCII

Name:		perl-Encode-EUCJPASCII
Version:	0.03
Release:	1
Summary:	EucJP-ascii - An eucJP-open mapping
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Group:		Development/Perl
URL:		https://metacpan.org/dist/Encode-EUCJPASCII
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/Encode-EUCJPASCII-0.03.tar.gz
Source1:	enc2xs
Source2:	encode.h

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Encode)
BuildRequires:	perl-Encode
BuildRequires:	gcc

%description
EucJP-ascii - An eucJP-open mapping.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
install -m755 %{SOURCE1} enc2xs
mkdir -p Encode
install -m644 %{SOURCE2} Encode/encode.h
export PATH="$PWD:$PATH"
export PERL5LIB="$PWD${PERL5LIB:+:$PERL5LIB}"
perl Makefile.PL INSTALLDIRS=vendor
%make_build OPTIMIZE="%{optflags}"

%install
%make_install
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
find %{buildroot} -type d -empty -delete

%files
%{perl_vendorarch}/*
%{_mandir}/man3/*
