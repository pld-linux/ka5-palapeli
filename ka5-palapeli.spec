%define		kdeappsver	21.04.3
%define		qtver		5.9.0
%define		kaname		palapeli
Summary:	Puzzle game
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	54b29f87ff081dcece68b3658f7ff2ec
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-karchive-devel >= 5.30.0
BuildRequires:	kf5-kcompletion-devel >= 5.30.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kio-devel >= 5.30.0
BuildRequires:	kf5-kitemviews-devel >= 5.30.0
BuildRequires:	kf5-knotifications-devel >= 5.30.0
BuildRequires:	kf5-kservice-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Palapeli is a single-player jigsaw puzzle game. Unlike other games in
that genre, you are not limited to aligning pieces on imaginary grids.
The pieces are freely moveable. Also, Palapeli features real
persistency, i.e. everything you do is saved on your disk immediately.

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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%{_libdir}/libpala.so.*.*.*
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
%{_datadir}/kservices5/palathumbcreator.desktop
%{_datadir}/metainfo/org.kde.palapeli.appdata.xml
%{_datadir}/mime/packages/palapeli-mimetypes.xml
%{_datadir}/palapeli
%{_datadir}/qlogging-categories5/palapeli.categories
%dir %{_libdir}/qt5/plugins/palapelislicers
%attr(755,root,root) %{_libdir}/qt5/plugins/palapelislicers/palapeli_goldbergslicer.so
%attr(755,root,root) %{_libdir}/qt5/plugins/palapelislicers/palapeli_jigsawslicer.so
%attr(755,root,root) %{_libdir}/qt5/plugins/palapelislicers/palapeli_rectslicer.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/Pala
%{_libdir}/libpala.so
%{_libdir}/cmake/Pala
