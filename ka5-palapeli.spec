%define		kdeappsver	18.04.0
%define		qtver		5.8.0
%define		kaname		palapeli
Summary:	Puzzle game
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	92e80e75f89704a864f665de85573d2d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ka5-libkdegames-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Puzzle game.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.


%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/palapeli-collectionrc
%attr(755,root,root) %{_bindir}/palapeli
%ghost %{_libdir}/libpala.so.0
%{_libdir}/libpala.so.0.*.*
%{_libdir}/qt5/plugins/palapeli_goldbergslicer.so
%{_libdir}/qt5/plugins/palapeli_jigsawslicer.so
%{_libdir}/qt5/plugins/palapeli_rectslicer.so
%{_libdir}/qt5/plugins/palathumbcreator.so
%{_desktopdir}/org.kde.palapeli.desktop
%{_iconsdir}/hicolor/128x128/apps/palapeli.png
%{_iconsdir}/hicolor/128x128/mimetypes/application-x-palapeli.png
%{_iconsdir}/hicolor/16x16/apps/palapeli.png
%{_iconsdir}/hicolor/16x16/mimetypes/application-x-palapeli.png
%{_iconsdir}/hicolor/24x24/apps/palapeli.png
%{_iconsdir}/hicolor/24x24/mimetypes/application-x-palapeli.png
%{_iconsdir}/hicolor/32x32/apps/palapeli.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-x-palapeli.png
%{_iconsdir}/hicolor/48x48/apps/palapeli.png
%{_iconsdir}/hicolor/48x48/mimetypes/application-x-palapeli.png
%{_iconsdir}/hicolor/64x64/apps/palapeli.png
%{_iconsdir}/hicolor/64x64/mimetypes/application-x-palapeli.png
%{_datadir}/knotifications5/palapeli.notifyrc
%{_datadir}/kservices5/ServiceMenus/palapeli_servicemenu.desktop
%{_datadir}/kservices5/palapeli_goldbergslicer.desktop
%{_datadir}/kservices5/palapeli_jigsawslicer.desktop
%{_datadir}/kservices5/palapeli_rectslicer.desktop
%{_datadir}/kservices5/palathumbcreator.desktop
%{_datadir}/kservicetypes5/libpala-slicerplugin.desktop
%dir %{_datadir}/kxmlgui5/palapeli
%{_datadir}/kxmlgui5/palapeli/palapeliui.rc
%{_datadir}/metainfo/org.kde.palapeli.appdata.xml
%{_datadir}/mime/packages/palapeli-mimetypes.xml
%{_datadir}/palapeli

%files devel
%defattr(644,root,root,755)
%{_includedir}/Pala
%{_includedir}/libpala
%{_libdir}/libpala.so
%{_libdir}/libpala
