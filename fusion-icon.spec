%global __requires_exclude	typelib\\(AyatanaAppIndicator3\\)

Name:		fusion-icon
Version:	0.2.4
Release:	2
Summary:	Simple tray icon for compiz
Group:		System/X11
License:	GPLv2+
URL:		https://github.com/compiz-reloaded/fusion-icon
Source0:	https://gitlab.com/compiz/fusion-icon/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# Upstream patches
Patch0001:	0001-Gtk-Avoid-GtkStock-for-the-Quit-button.patch
Patch0002:	0002-Fix-typeerror-in-python3.6.patch
Patch0005:	0005-Add-support-for-Ayatana-AppIndicators.patch
Patch0006:	0006-Qt-Add-Qt-for-Python-PySide-support.patch
Patch0008:	0008-Account-for-KWin-X11-from-KDE-Plasma-5.patch
# Mageia patches
Patch0101:	fusion-icon-0.2.4-mga-add_mageia_gl_paths.patch
Patch0102:	fusion-icon-0.2.2-mga-ignore_desktop_hints.patch

BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

Recommends:	compizconfig-python
Requires:	python-gi
Requires:	glxinfo
Requires:	xvinfo
Requires:	compiz
Requires:	ccsm

Provides:	fusion-icon = %{version}-%{release}

%description
Compiz-fusion-icon is a simple tray icon for compiz, it allows you
to graphically choose decorator, window manager and access control center.

If you use a Qt5 based desktop then you should also install
%{name}-qt package.

%package qt
Summary:	Simple tray icon for compiz
Group:		System/X11
Requires:	%{name} = %{version}-%{release}
Requires:	python-qt5

%description qt
Compiz-fusion-icon is a simple tray icon for compiz, it allows you
to graphically choose decorator, window manager and access control center.

This package provides Qt gui to the application.
If you don't use Qt5 based desktop then %{name} should suffice.

%prep
%autosetup -n %{name}-v%{version} -p1

# Fix libdir in data.py
sed -i "s|MULTILIBDIR|%{_libdir}|g" FusionIcon/data.py

%build
%py_build -- --with-gtk=3.0 --with-qt=5.0

%install
%py_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc NEWS VERSION
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%dir %{python3_sitelib}/FusionIcon/
%{python_sitelib}/FusionIcon/interface_gtk/
%{python_sitelib}/FusionIcon/*pycache*
%{python_sitelib}/FusionIcon/*.py
%{python_sitelib}/fusion_icon-%{version}-py?.?.egg-info

%files qt
%{python_sitelib}/FusionIcon/interface_qt/
