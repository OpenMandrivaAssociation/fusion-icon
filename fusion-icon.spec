%define git 20100215

%if  %{git}
# git clone git://anongit.compiz-fusion.org/users/crdlb/fusion-icon
# git archive --format=tar --prefix=fusion-icon-$(date +%Y%m%d)/ master | bzip2 > ../fusion-icon-$(date +%Y%m%d).tar.bz2
%define distname %{name}-%{git}
%define rel 0.%{git}.5
%else
%define distname %{name}-%{version}
%define rel 1
%endif

Name:		fusion-icon
Version:	0.1
Release:	%{rel}
Summary:	Simple tray icon for compiz fusion
Group:		System/X11
License:	GPLv2
URL:		http://www.compiz-fusion.org/
Source:		%{distname}.tar.bz2
Patch0:		fusion-icon-20071127-icon32.patch
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(python)
Requires:	python-compizconfig0.8
Requires:	pygtk2.0
Requires:	glxinfo
Requires:	xvinfo
BuildArch:	noarch

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
	--add-category="Settings" \
	--add-category="DesktopSettings" \
	--add-category="X-MandrivaLinux-CrossDesktop" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{py_puresitedir}/FusionIcon
%{py_puresitedir}/*.egg-info
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop

