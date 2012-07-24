Summary:	A text-based modem control and terminal emulation program
Name:		minicom
Version:	2.6.1
Release:	1
License:	GPLv2+
Group:		Communications
URL:		http://alioth.debian.org/projects/minicom/
Source:		http://alioth.debian.org/frs/download.php/3700/%{name}-%{version}.tar.gz
Requires:	lrzsz
Requires:	setserial
Requires:	lockdev-baudboy
BuildRequires:	ncurses-devel

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

%build
%configure2_5x --disable-rpath
%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc NEWS AUTHORS README TODO
%doc doc/Announce* doc/COMPATABILITY.lrzsz doc/HistSearch
%doc doc/Locales doc/Macros doc/QuickStart.modemu doc/README.lrzsz
%doc doc/TODO.lrzsz doc/Todo* doc/copyright.modemu doc/fselector.txt
%doc doc/japanese doc/minicom.FAQ doc/modemu.README doc/pl-translation.txt 
%doc doc/portugues-brasil doc/suomeksi doc/ChangeLog.old
%attr(755,root,dialout) %{_bindir}/minicom
%{_bindir}/runscript
%{_bindir}/xminicom
%{_bindir}/ascii-xfr
%{_mandir}/man1/*.1*
