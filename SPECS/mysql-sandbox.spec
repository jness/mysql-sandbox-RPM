Name: mysql-sandbox
Version: 3.0.17
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Libraries
Summary: Quick painless install of side MySQL server in isolation 
URL: https://launchpad.net/mysql-sandbox 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source0: http://launchpad.net/mysql-sandbox/mysql-sandbox-3/mysql-sandbox-3/+download/MySQL-Sandbox-%{version}.tar.gz 
BuildArch: noarch

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::More)


%description
Quick painless install of side MySQL server in isolation. MySQL Sandbox is a 
tool for installing one or more MySQL servers in isolation, without 
affecting other servers.

%prep
%setup -q -n MySQL-Sandbox-3.0.17

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
rm -rf %{buildroot}
%{__make} install PERL_INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files

%{_bindir}/low_level_make_sandbox
%{_bindir}/make_multiple_custom_sandbox
%{_bindir}/make_multiple_sandbox
%{_bindir}/make_replication_sandbox
%{_bindir}/make_sandbox
%{_bindir}/make_sandbox_from_installed
%{_bindir}/make_sandbox_from_source
%{_bindir}/msandbox
%{_bindir}/sb
%{_bindir}/sbtool
%{_bindir}/test_sandbox

%{perl_vendorlib}/MySQL/Sandbox.pm
%{perl_vendorlib}/MySQL/Sandbox/Recipes.pm
%{perl_vendorlib}/MySQL/Sandbox/Scripts.pm
%{perl_vendorlib}/i386-linux-thread-multi/auto/MySQL/Sandbox/.packlist

%{_mandir}/man3/MySQL::Sandbox.3pm.gz
%{_mandir}/man3/MySQL::Sandbox::Recipes.3pm.gz
%{_mandir}/man3/MySQL::Sandbox::Scripts.3pm.gz

%changelog
* Mon Mar 07 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 3.0.17-1
- Initial Build
