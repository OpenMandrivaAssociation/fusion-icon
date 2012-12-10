%define name fusion-icon
%define version 0.1
%define rel 4
%define git 20100215

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
BuildArch: noarch
BuildRequires: desktop-file-utils python-devel
Requires: compizconfig-python
Requires: pygtk2.0
Requires: glxinfo
Requires: xvinfo

%description
fusion-icon is a simple tray icon for compiz fusion.

%prep
%setup -q -n %{distname}
%patch0 -p1 -b .icon32

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

desktop-file-install \
  --vendor="" \
  --remove-category="Compiz" \
  --add-category="GTK" \
  --add-category="Settings" \
  --add-category="DesktopSettings" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{py_puresitedir}/FusionIcon
%{py_puresitedir}/FusionIcon/*.py*
%{py_puresitedir}/FusionIcon/interface_*/*.py*
%{py_puresitedir}/*.egg-info
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 0.1-0.20100215.3mdv2011.0
+ Revision: 594759
- rebuild for python 2.7

* Sat Feb 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1-0.20100215.2mdv2010.1
+ Revision: 512440
- require mesa-demos for distros < 2010.1 (tip from Anssi)

* Mon Feb 15 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1-0.20100215.1mdv2010.1
+ Revision: 506397
- update to 0.1 (new git snapshot)

* Wed Feb 03 2010 Thierry Vignaud <tv@mandriva.org> 0.0-0.20071127.4mdv2010.1
+ Revision: 499984
- requires glxinfo instead of mesa-demos

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.0-0.20071127.3mdv2010.0
+ Revision: 437610
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.0-0.20071127.2mdv2009.1
+ Revision: 323363
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.0-0.20071127.1mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 16 2008 Olivier Blin <oblin@mandriva.com> 0.0-0.20071127.1mdv2008.1
+ Revision: 153629
- buildrequire desktop-file-utils
- buildrequire python-devel
- buildrequire python
- initial fusion-icon package
- create fusion-icon

