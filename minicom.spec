Summary:	A text-based modem control and terminal emulation program
Name:		minicom
Version:	2.2
Release:	%mkrel 1
License:	GPL
Group:		Communications
URL:		http://alioth.debian.org/projects/minicom/
Source:		http://alioth.debian.org/frs/download.php/1806/minicom-%{version}.tar.gz
Source1:	%{name}.bash-completion
Patch1:		minicom-2.2-ncurses.patch
Patch2:		minicom-2.2-drop-privs.patch
Patch3:		minicom-2.2-wchar.patch
Patch4:		minicom-2.2-umask.patch
Patch5:		minicom-2.2-setlocale.patch
Patch6:		minicom-2.2-spaces.patch
Patch7:		minicom-2.2-gotodir.patch
Patch8:		minicom-2.2-rh.patch
Patch9:		minicom-2.2-esc.patch
Patch10:	minicom-2.2-staticbuf.patch
Requires:	lrzsz
Requires:	setserial
BuildRequires:	ncurses-devel
BuildRequires:	libtermcap-devel
#BuildRequires:	liblockdev-devel

%description
Minicom is a simple text-based modem control and terminal emulation program
somewhat similar to MSDOS Telix. Minicom includes a dialing directory, full
ANSI and VT100 emulation, an (external) scripting language, and other features.

Minicom should be installed if you need a simple modem control program or
terminal emulator.

Run 'minicom -s' as root to create a system wide configuration. Users need
read/write permissions on the serial port devices in order to use minicom.

%prep

%setup -q
%patch1 -p1 -b .ncurses
%patch2 -p1 -b .privs
%patch3 -p1 -b .wchar
%patch4 -p1 -b .umask
%patch5 -p1 -b .setlocale
%patch6 -p1 -b .spaces
%patch7 -p1 -b .gotodir
##%patch8 -p1 -b .rh
%patch9 -p1 -b .esc
#%patch10 -p1 -b .staticbuf

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
