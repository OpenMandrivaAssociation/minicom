%define name	minicom
%define version	2.1
%define release	%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A text-based modem control and terminal emulation program.
License:	GPL
Group:		Communications
URL:		http://alioth.debian.org/projects/minicom/
Source:		http://alioth.debian.org/download.php/123/%{name}-%{version}.tar.bz2
Source1:    %{name}.bash-completion
patch0:     %{name}-2.1.build.patch
Requires:	lrzsz
Requires:	setserial
BuildRequires:	ncurses-devel
BuildRequires:	libtermcap-devel
Buildroot:	%{_tmppath}/%{name}-%{version}


%description
Minicom is a simple text-based modem control and terminal emulation
program somewhat similar to MSDOS Telix.  Minicom includes a dialing
directory, full ANSI and VT100 emulation, an (external) scripting language,
and other features.

Minicom should be installed  if you need a simple modem control program
or terminal emulator.

%prep
%setup -q
%patch0 -p 0

# minicom used wrong variable to check intl inside glibc
perl -pi -e 's/gt_cv_func_gettext_libc/gt_cv_func_gnugettext1_libc/' configure

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -D -m 644 doc/minicom.users %{buildroot}%{_sysconfdir}/minicom.users

# bash completion
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc doc
%{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/minicom.users
%attr(755,root,uucp) %{_bindir}/minicom
%{_bindir}/runscript
%{_bindir}/xminicom
%{_bindir}/ascii-xfr
%{_mandir}/*/*

