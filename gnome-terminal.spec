%define gettext_package gnome-terminal

%define glib2_version 2.40.0
%define gtk3_version 3.10.0
%define vte_version 0.38.0
%define desktop_file_utils_version 0.2.90

Summary: Terminal emulator for GNOME
Name: gnome-terminal
Version: 3.14.3
Release: 3%{?dist}
License: GPLv3+ and GFDL
Group: User Interface/Desktops
URL: http://www.gnome.org/
#VCS: git:git://git.gnome.org/gnome-terminal
Source0: http://download.gnome.org/sources/gnome-terminal/3.14/gnome-terminal-%{version}.tar.xz

Patch0: 0001-Restore-transparency-gnome-3-14.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=745958
Patch1: 0001-Make-the-ActiveTerminal-field-in-the-config-file-for.patch

Patch2: 0001-RHEL-doesn-t-have-appdata-tools.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=730128
Patch3: 0001-window-Pass-tab-switching-keys-to-the-terminal-for-t.patch

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: GConf2-devel
BuildRequires: gtk3-devel >= %{gtk3_version}
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: vte291-devel >= %{vte_version}
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: autoconf automake libtool
BuildRequires: itstool
BuildRequires: dconf-devel
BuildRequires: libuuid-devel
BuildRequires: nautilus-devel
BuildRequires: gnome-shell
BuildRequires: vala
BuildRequires: vala-devel
BuildRequires: vala-tools
BuildRequires: yelp-tools

Requires: dbus-x11
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gsettings-desktop-schemas
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: vte291%{?_isa} >= %{vte_version}

%description
gnome-terminal is a terminal emulator for GNOME. It features the ability to use
multiple terminals in a single window (tabs) and profiles support.

%package nautilus
Summary: GNOME Terminal extension for Nautilus
Requires: %{name}%{?_isa} = %{version}-%{release}

%description nautilus
This package provides a Nautilus extension that adds the 'Open in Terminal'
option to the right-click context menu in Nautilus.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf --force --install
%configure --disable-static --with-gtk=3.0 --with-nautilus-extension

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la

%find_lang %{gettext_package} --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-terminal.desktop

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{gettext_package}.lang
%doc AUTHORS COPYING NEWS

%{_bindir}/gnome-terminal
%{_datadir}/appdata/gnome-terminal.appdata.xml
%{_datadir}/applications/gnome-terminal.desktop
%{_libexecdir}/gnome-terminal-migration
%{_libexecdir}/gnome-terminal-server
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_datadir}/gnome-shell

%files nautilus
%{_libdir}/nautilus/extensions-3.0/libterminal-nautilus.so

%changelog
* Mon Oct  5 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.14.3-3
- Pass tab switching keys to the terminal for tabless windows
- Resolves: #1268255

* Mon Sep 21 2015 Matthias Clasen <mclasen@redhat.com> - 3.14.3-2
- Drop the dark theme override
- Resolves: #1264054

* Wed Apr  8 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.14.3-1
- Update to 3.14.3
- Drop the appdata-tools BR from RHEL
- Add BRs on vala-devel, vala-tools and yelp-tools to generate the build
  scripts
- Resolves: #1174726, #1180775

* Mon Mar 23 2015 Richard Hughes <rhughes@redhat.com> - 3.14.2-1
- Update to 3.14.2
- Resolves: #1174726

* Mon Mar  3 2014 Matthias Clasen <mclasen@redhat.com> - 3.8.4-8
- Rebuild
- Resolves: #1070811

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.4-7
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.4-6
- Mass rebuild 2013-12-27

* Tue Dec 10 2013 Zeeshan Ali <zeenix@redhat.com> - 3.8.4-5
- Fix #1030352.

* Tue Dec 10 2013 Zeeshan Ali <zeenix@redhat.com> - 3.8.4-4
- Fix #1034618.

* Mon Dec  9 2013 Zeeshan Ali <zeenix@redhat.com> - 3.8.4-3
- Fix #952664.

* Tue Nov 19 2013 Zeeshan Ali <zeenix@redhat.com> - 3.8.4-2
- Fix #1030434.

* Mon Jul  8 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.4-1
- Update to 3.8.4
- Fixes a crash on session resume (#981440)

* Mon Jun 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.3-1
- Update to 3.8.3
- Use desktop-file-validate instead of desktop-file-install

* Mon May 13 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Apr 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0.1-1
- Update to 3.8.0.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 26 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.2-3
- Bring back titlebars on maximized terminals

* Fri Jan 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.2-2
- Backport a fix for a crash in terminal_screen_container_style_updated

* Fri Jan 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1.1-1
- Update to 3.4.1.1

* Tue Mar 27 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0.1-1
- Update to 3.4.0.1
- Avoid listing files twice in %%files

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.0-1
- Update to 3.3.0

* Thu Jan 12 2012 Matthias Clasen <mclasen@redhat.com> - 3.2.1-2
- Update license field (#639132)

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> 3.0.0-1
- Update to 3.0.0

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> 2.33.90-1
- Update to 2.33.90

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> 2.33.5-3
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.33.5-1
- Update to 2.33.5

* Wed Jan 12 2011 Matthias Clasen <mclasen@redhat.com> - 2.33.4-2
- Make the find dialog work again

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.33.4-1
- Update to 2.33.4

* Fri Jan  7 2011 Matthias Clasen <mclasen@redhat.com> - 2.33.3-1
- Update to 2.33.3

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.33.2-2
- Rebuild against new gtk

* Thu Nov 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.33.2-1
- Update to 2.33.2
- Back to gtk3

* Fri Oct  8 2010 Owen Taylor <otaylor@redhat.com> - 2.33.0-3
- Revert back to a gtk2 build - the gtk3 build has major sizing issues
  (rhbz #641337)

* Thu Oct  7 2010 Matthias Clasen <mclasen@redhat.com> - 2.33.0-2
- Build against gtk3

* Mon Oct  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.33.0-1
- Update to 2.33.0

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-1
- Update to 2.31.91

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.90-1
- Update to 2.31.90

* Thu May 27 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.3-1
- Update to 2.31.3

* Tue May  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.2-2
- Add more translations for search UI

* Tue May  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.2-1
- Update to 2.31.2
- Add translations for search UI

* Tue May  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.1-1
- Update to 2.31.1

* Mon Apr 26 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Thu Mar 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.92-1
- Update to 2.29.92

* Sun Feb 14 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.6-3
- Add missing libs

* Thu Jan 14 2010 Behdad Esfahbod <behdad@redhat.com> - 2.29.6-2
- Second try
- Drop stale patch

* Thu Jan 14 2010 Behdad Esfahbod <behdad@redhat.com> - 2.29.6-1
- Update to 2.29.6
