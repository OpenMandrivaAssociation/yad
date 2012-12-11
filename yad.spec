Summary:	A fork of Zenity with many improvements
Name:		yad
Version:	0.16.3
Release:	1
Group:		Development/GNOME and GTK+
License:	GPLv2
URL:		http://code.google.com/p/yad/
Source0:	%{name}-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Yad (yet another dialog) is a fork of Zenity with many improvements, such as
custom buttons, additional dialogs, pop-up menu in notification icon and more.

There were two main reasons to make this fork. The first one is to remove
dependencies on deprecated libraries, such as libglade and gnome-canvas.
And the second one - as for me, Zenity looks like an abandoned project.
Its ChangeLog consists of just "bump version to..." and "translation updated"
for the long time, but many interesting ideas which are ignored by
developers/maintainers were in GNOME Bugzilla.

%prep
%setup -q 

%build
%configure2_5x 
       
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}/usr/share/aclocal/yad.m4

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO THANKS
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/yad.png
%{_mandir}/man1/*.1*



%changelog
* Wed Jan 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.16.3-1
+ Revision: 768132
- added missing BR
- imported package yad


* Tue Jan 24 2012 Matthew Dawkins <mdawkins@unity-linux.org> 0.16.3-1-unity2011
- new version 0.16.3

* Mon Mar 07 2011 Gianvacca <gianvacca@unity-linux.org> 0.9.0-1-unity2011
- First release for Unity
