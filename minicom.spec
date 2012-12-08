Summary:	A text-based modem control and terminal emulation program
Name:		minicom
Version:	2.5
Release:	%mkrel 3
License:	GPLv2+
Group:		Communications
URL:		http://alioth.debian.org/projects/minicom/
Source:		http://alioth.debian.org/frs/download.php/3195/minicom-%{version}.tar.gz
Requires:	lrzsz
Requires:	setserial
Requires:	lockdev-baudboy
BuildRequires:	ncurses-devel
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

%build
%configure2_5x --disable-rpath
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5-2mdv2011.0
+ Revision: 666429
- mass rebuild

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 2.5-1
+ Revision: 634147
- New version 2.5

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-3mdv2011.0
+ Revision: 606646
- rebuild

* Wed May 12 2010 Emmanuel Andry <eandry@mandriva.org> 2.4-2mdv2010.1
+ Revision: 544579
- add P13 and p14 from fedora to allow configuration with minicom -s

* Fri Jan 01 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.4-1mdv2010.1
+ Revision: 484677
- new version
- drop getline patch, useless now
- drop unappliable rh and drop-privs patches
- rediff all other patches
- cleanup documentation files

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3-7mdv2010.0
+ Revision: 453434
- added P12 to fix build (gentoo)

* Tue Feb 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.3-6mdv2009.1
+ Revision: 337201
- keep bash completion in its own package

* Fri Jan 09 2009 Frederic Crozat <fcrozat@mandriva.com> 2.3-5mdv2009.1
+ Revision: 327559
- minicom is now setgid dialout and not uucp

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3-4mdv2009.1
+ Revision: 317108
- rediffed some fuzzy patches
- fix build with -Werror=format-security (P11)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.3-3mdv2009.0
+ Revision: 223263
- rebuild

* Mon Mar 03 2008 Olivier Blin <oblin@mandriva.com> 2.3-2mdv2008.1
+ Revision: 177827
- use lockdev to allow users to create lock files (#16739)

* Sun Mar 02 2008 Olivier Blin <oblin@mandriva.com> 2.3-1mdv2008.1
+ Revision: 177629
- buildconflicts with termcap-devel instead of buildrequiring it
  (or else it get preferred over ncurses)
- 2.3
- sync with RH patches

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.2-2mdv2008.1
+ Revision: 153090
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Apr 18 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2-1mdv2008.0
+ Revision: 14790
- 2.2
- sync patches with fedora


* Fri Dec 22 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-12-22 17:13:12 (101546)
- add BuildRequires: libtermcap-devel

* Fri Dec 22 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-12-22 17:07:58 (101545)
Import minicom

* Tue Sep 19 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.1-6mdv2007.0
- Rebuild

* Tue Sep 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-5mdv2007.0
- %%mkrel
- bash completion
- fix build

* Tue May 02 2006 Stefan van der Eijk <stefan@eijk.nu> 2.1-4mdk
- rebuild for sparc

* Mon Jan 24 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.1-3mdk 
- Add requires on setserial package

* Mon May 31 2004 Abel Cheung <deaddog@deaddog.org> 2.1-2mdk
- Drop antique po files
- Fix gettext check, minicom doesn't need to link with -lintl

