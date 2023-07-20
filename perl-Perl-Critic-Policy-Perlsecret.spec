#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Perl
%define		pnam	Critic-Policy-Perlsecret
Summary:	Perl::Critic::Policy::Perlsecret - Prevent perlsecrets entering your codebase
Name:		perl-Perl-Critic-Policy-Perlsecret
Version:	0.0.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8e5084afd573db4624bc5ff3a7960829
URL:		https://metacpan.org/release/Perl-Critic-Policy-Perlsecret
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Perl::Critic::Policy)
BuildRequires:	perl(Perl::Critic::TestUtils)
BuildRequires:	perl(Perl::Critic::Utils)
BuildRequires:	perl(Test::FailWarnings)
BuildRequires:	perl-Test-Fatal
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This policy checks for perlsecret operators in your code and warns you
about them.

You can override the secrets that are allowed or disallowed using the
parameters allow_secrets and disallow_secrets. The default is to
simply disallow everything.

Notice the secrets are capitalized correctly ("Ornate Double-Bladed
Sword", not "Ornate double-bladed sword").

[Perlsecret] disallow_secrets = Flathead, Phillips, Pozidriv, Torx,
Enterprise

This provides the list to disallow.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Perl/Critic/Policy/Perlsecret.pm
%{_mandir}/man3/Perl::Critic::Policy::Perlsecret.3*
%{_examplesdir}/%{name}-%{version}
