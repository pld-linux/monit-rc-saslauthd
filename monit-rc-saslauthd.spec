Summary:	monitrc file for monitoring SASL authentication server
Summary(pl.UTF-8):	Plik monitrc do monitorowania serwera uwierzytelniania SASL
Name:		monit-rc-saslauthd
Version:	1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	saslauthd.monitrc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	monit
Requires:	monit
Requires:	cyrus-sasl-saslauthd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring Cyrus SASL authentication server.

%description -l pl.UTF-8
Plik monitrc do monitorowania serwera uwierzytelniania Cyrus SASL.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/monit

install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monit

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q monit restart

%postun
%service -q monit restart

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/monit/*.monitrc
