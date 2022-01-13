%define _disable_rebuild_configure 1

Summary:	A text-based modem control and terminal emulation program
Name:		minicom
Version:	2.8
Release:	1
License:	GPLv2+
Group:		Communications
Url:		https://salsa.debian.org/minicom-team/minicom
Source0:	https://salsa.debian.org/minicom-team/minicom/-/archive/v%{version}.x/minicom-v%{version}.x.tar.bz2
BuildRequires:	pkgconfig(ncurses)
Requires:	lrzsz
Requires:	setserial

%description
Minicom is a simple text-based modem control and terminal emulation program
somewhat similar to MSDOS Telix. Minicom includes a dialing directory, full
ANSI and VT100 emulation, an (external) scripting language, and other features.

Minicom should be installed if you need a simple modem control program or
terminal emulator.

Run 'minicom -s' as root to create a system wide configuration. Users need
read/write permissions on the serial port devices in order to use minicom.

%prep
%autosetup -p1 -n minicom-v%{version}.x
./autogen.sh

%build
%configure --enable-music
# Switch to more reasonable defaults... "Real" serial ports are virtually dead
sed -i -e 's,ttyS1,ttyUSB0,g' config.h
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
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
%{_mandir}/man1/*
