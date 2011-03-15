Name: mysql-sandbox
Version: 3.0.17
Release: 2%{?dist}
License: GPLv2
Group: Development/Libraries
Summary: Quick painless install of side by side MySQL server in isolation 
URL: https://launchpad.net/mysql-sandbox 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source0: http://launchpad.net/mysql-sandbox/mysql-sandbox-3/mysql-sandbox-3/+download/MySQL-Sandbox-%{version}.tar.gz 
BuildArch: noarch

Patch0: MySQL-Sandbox-3.0.17_perl_mysql_required.patch

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::More)

%description
Quick painless install of side by side MySQL server in isolation. 
MySQL Sandbox is a tool for installing one or more MySQL servers 
in isolation, without affecting other servers.

%prep
%setup -q -n MySQL-Sandbox-%{version}
%patch0 -p1

%build
# avoid CPAN entirely
# http://fedoraproject.org/wiki/Packaging/Perl#Useful_tips
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
%defattr(644, root, root)
%attr(755, root, root) %{_bindir}/low_level_make_sandbox
%attr(755, root, root) %{_bindir}/make_multiple_custom_sandbox
%attr(755, root, root) %{_bindir}/make_multiple_sandbox
%attr(755, root, root) %{_bindir}/make_replication_sandbox
%attr(755, root, root) %{_bindir}/make_sandbox
%attr(755, root, root) %{_bindir}/make_sandbox_from_installed
%attr(755, root, root) %{_bindir}/make_sandbox_from_source
%attr(755, root, root) %{_bindir}/msandbox
%attr(755, root, root) %{_bindir}/sb
%attr(755, root, root) %{_bindir}/sbtool
%attr(755, root, root) %{_bindir}/test_sandbox

%attr(644, root, root) %{perl_vendorlib}/MySQL/Sandbox/Recipes.pm
%attr(644, root, root) %{perl_vendorlib}/MySQL/Sandbox/Scripts.pm
%attr(644, root, root) %{perl_vendorlib}/MySQL/Sandbox.pm


# http://fedoraproject.org/wiki/Packaging/Perl#Directory_Ownership
%exclude %{perl_vendorarch}/auto/

%{_mandir}/man3/MySQL::Sandbox.3pm.gz
%{_mandir}/man3/MySQL::Sandbox::Recipes.3pm.gz
%{_mandir}/man3/MySQL::Sandbox::Scripts.3pm.gz

%changelog
* Tue Mar 15 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 3.0.17-2
- Added: Patch0: MySQL-Sandbox-3.0.17_perl_mysql_required.patch
  This resolves spurious dependency on perl(mysql)

* Mon Mar 07 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 3.0.17-1
- Initial Build
- Not every binry/script has a man page, I'm checking with upstream:
  https://answers.launchpad.net/mysql-sandbox/+question/148179
