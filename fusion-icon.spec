%define name fusion-icon
%define version 0.0
%define rel 1
%define git 20071127

%if  %{git}
# git clone git://anongit.compiz-fusion.org/users/crdlb/fusion-icon
# git archive --format=tar --prefix=fusion-icon-$(date +%Y%m%d)/ master | bzip2 > ../fusion-icon-$(date +%Y%m%d).tar.bz2
%define distname %{name}-%{git}
%define release %mkrel 0.%{git}.%{rel}
%else
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif

Name: %name
Version: %version
Release: %release
Summary: Simple tray icon for compiz fusion
Group: System/X11
URL: http://www.compiz-fusion.org/
Source: %{distname}.tar.bz2
Patch0: fusion-icon-20071127-icon32.patch
License: GPL
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Requires: compizconfig-python
Requires: pygtk2.0
Requires: mesa-demos
Requires: xvinfo

%description
fusion-icon is a simple tray icon for compiz fusion.

%prep
%setup -q -n %{distname}
%patch0 -p1 -b .icon32

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%find_lang %{name}

desktop-file-install \
  --vendor="" \
  --remove-category="Compiz" \
  --add-category="GTK" \
  --add-category="Settings" \
  --add-category="DesktopSettings" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{py_puresitedir}/FusionIcon
%{py_puresitedir}/FusionIcon/*.py*
%{py_puresitedir}/FusionIcon/interface_*/*.py*
%{py_puresitedir}/*.egg-info
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
