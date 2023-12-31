Summary:	A fork of Zenity with many improvements
Name:		yad
Version:	13.0
Release:	1
Group:		Development/GNOME and GTK+
License:	GPLv2
Url:		https://sourceforge.net/projects/yad-dialog/
Source0:	https://github.com/v1cont/yad/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(gspell-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(webkitgtk-6.0)
BuildRequires:	perl(XML::Parser)

%description
Yad (yet another dialog) is a fork of Zenity with many improvements, such as
custom buttons, additional dialogs, pop-up menu in notification icon and more.

There were two main reasons to make this fork. The first one is to remove
dependencies on deprecated libraries, such as libglade and gnome-canvas.
And the second one - as for me, Zenity looks like an abandoned project.
Its ChangeLog consists of just "bump version to..." and "translation updated"
for the long time, but many interesting ideas which are ignored by
developers/maintainers were in GNOME Bugzilla.

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS NEWS THANKS TODO
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/aclocal/%{name}.m4
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/*.1*

#----------------------------------------------------------------------

%prep
%autosetup -p1 

# build against webkit2gtk-6.0
sed -i -e 's/webkit2gtk-4.0/webkit2gtk-6.0/g' configure.ac

%build
autoreconf -fiv
%configure\
	--enable-icon-browser \
	--with-gtk=gtk3 \
	--enable-html
%make_build

%install
%make_install

# remove unwanted
rm -rf %{buildroot}/usr/share/aclocal/yad.m4

# locales
%find_lang %{name}

