Summary:	A text-based modem control and terminal emulation program
Name:		minicom
Version:	2.4
Release:	%mkrel 1
License:	GPL
Group:		Communications
URL:		http://alioth.debian.org/projects/minicom/
Source:		http://alioth.debian.org/frs/download.php/3195/minicom-%{version}.tar.gz
Patch1:		minicom-2.4-ncurses.patch
Patch4:     minicom-2.4-umask.patch
Patch6:     minicom-2.2-spaces.patch
Patch7:     minicom-2.3-gotodir.patch
Patch9:     minicom-2.4-esc.patch
Patch10:    minicom-2.4-staticbuf.patch
Patch12:    minicom-2.4-fix-format-error.patch
Requires:	lrzsz
Requires:	setserial
Requires:	lockdev-baudboy
BuildRequires:	ncurses-devel
BuildConflicts:	libtermcap-devel
BuildRequires:	liblockdev-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

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
%patch4 -p1 -b .umask
%patch6 -p1 -b .spaces
%patch7 -p1 -b .gotodir
%patch9 -p1 -b .esc
%patch10 -p1 -b .staticbuf
%patch12 -p1 -b .format

# minicom used wrong variable to check intl inside glibc
#perl -pi -e 's/gt_cv_func_gettext_libc/gt_cv_func_gnugettext1_libc/' configure

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS AUTHORS INSTALL README TODO
%doc doc/Announce* doc/COMPATABILITY.lrzsz doc/HistSearch
%doc doc/Locales doc/Macros doc/QuickStart.modemu doc/README.lrzsz
%doc doc/TODO.lrzsz doc/Todo* doc/copyright.modemu doc/fselector.txt
%doc doc/japanese doc/minicom.FAQ doc/modemu.README doc/pl-translation.txt 
%doc doc/portugues-brasil doc/suomeksi doc/ChangeLog.old
%attr(755,root,dialout) %{_bindir}/minicom
%{_bindir}/runscript
%{_bindir}/xminicom
%{_bindir}/ascii-xfr
%{_mandir}/*/*
