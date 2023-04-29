%global kf5_version 5.105.0
%global framework kio

Name:			opt-kf5-kio
Version:		5.105.0
Release:		1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution for filesystem abstraction

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:	%{name}-%{version}.tar.bz2

# filter plugin provides
%global __provides_exclude_from ^(%{_opt_kf5_qtplugindir}/.*\\.so)$

# SFOS patch
Patch2:    0001-telnet-remove.patch

# core
BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}
BuildRequires:  opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires:  opt-kf5-karchive-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kauth-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kcrash-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kdbusaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kguiaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kservice-devel >= %{kf5_version}
BuildRequires:  opt-kf5-solid-devel >= %{kf5_version}
# extras
BuildRequires:  opt-kf5-kbookmarks-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kcompletion-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kconfigwidgets-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kiconthemes-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kitemviews-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kjobwidgets-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kwindowsystem-devel >= %{kf5_version}
# others
BuildRequires:  opt-kf5-knotifications-devel >= %{kf5_version}
BuildRequires:  opt-kf5-ktextwidgets-devel >= %{kf5_version}
#BuildRequires:  opt-kf5-kwallet-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kxmlgui-devel >= %{kf5_version}

BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qttools-devel
BuildRequires:  opt-qt5-qtdeclarative-devel

BuildRequires:  libacl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  zlib-devel

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-ntlm%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

%description
KDE Frameworks 5 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
%{?opt_kf5_default_filter}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opt-kf5-kbookmarks-devel >= %{kf5_version}
Requires:       opt-kf5-kcompletion-devel >= %{kf5_version}
Requires:       opt-kf5-kconfig-devel >= %{kf5_version}
Requires:       opt-kf5-kcoreaddons-devel >= %{kf5_version}
Requires:       opt-kf5-kitemviews-devel >= %{kf5_version}
Requires:       opt-kf5-kjobwidgets-devel >= %{kf5_version}
Requires:       opt-kf5-kservice-devel >= %{kf5_version}
Requires:       opt-kf5-solid-devel >= %{kf5_version}
Requires:       opt-kf5-kxmlgui-devel >= %{kf5_version}
Requires:       opt-kf5-kwindowsystem-devel >= %{kf5_version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        core
Summary:        Core components of the KIO Framework
## org.kde.klauncher5 service referenced from : src/core/slave.cpp
%{?kf5_kinit_requires}
%{?opt_kf5_default_filter}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires: opt-kf5-karchive >= %{kf5_version}
Requires: opt-kf5-kconfigwidgets >= %{kf5_version}
Requires: opt-kf5-kdbusaddons >= %{kf5_version}
Requires: opt-kf5-knotifications >= %{kf5_version}
Requires: opt-kf5-solid >= %{kf5_version}
Requires: opt-kf5-kwidgetsaddons >= %{kf5_version}
Requires: opt-kf5-kwindowsystem >= %{kf5_version}
Requires: opt-qt5-qtbase-gui
Requires: opt-qt5-qtdeclarative

%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
%{?opt_kf5_default_filter}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: %{name}-core = %{version}-%{release}
Requires: opt-kf5-kauth >= %{kf5_version}
Requires: opt-kf5-kconfig-core >= %{kf5_version}
Requires: opt-kf5-kcoreaddons >= %{kf5_version}
Requires: opt-kf5-kcrash >= %{kf5_version}
Requires: opt-kf5-ki18n >= %{kf5_version}
Requires: opt-kf5-kservice >= %{kf5_version}

%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
## org.kde.klauncher5 service referenced from : widgets/krun.cpp
## included here for completeness, even those -core already has a dependency.
%{?kf5_kinit_requires}
%{?opt_kf5_default_filter}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets-libs = %{version}-%{release}
Requires: opt-kf5-kitemviews
%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
%{?opt_kf5_default_filter}
Requires:       %{name}-widgets = %{version}-%{release}
Requires: opt-kf5-kcompletion >= %{kf5_version}
Requires: opt-kf5-kconfig-gui >= %{kf5_version}
Requires: opt-kf5-kguiaddons >= %{kf5_version}
Requires: opt-kf5-kiconthemes >= %{kf5_version}
Requires: opt-kf5-kjobwidgets >= %{kf5_version}
%description    widgets-libs
%{summary}.

%package        file-widgets
Summary:        Widgets for file-handling for KIO Framework
%{?opt_kf5_default_filter}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires: opt-kf5-kbookmarks
Requires: opt-kf5-kxmlgui
%description    file-widgets
The KIOFileWidgets library provides the file selection dialog and
its components.

%package        gui
Summary:        Gui components for the KIO Framework
%{?opt_kf5_default_filter}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    gui
%{summary}.

%package        ntlm
Summary:        NTLM support for KIO Framework
%{?opt_kf5_default_filter}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

%description    ntlm
KIONTLM provides support for NTLM authentication mechanism in KIO

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
  -DKIOCORE_ONLY=OFF \
  -DBUILD_DESIGNERPLUGIN=OFF \
  -DWITH_X11=OFF \

%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang_kf5 kio5_qt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post core-libs -p /sbin/ldconfig
%postun core-libs -p /sbin/ldconfig

%post gui -p /sbin/ldconfig
%postun gui -p /sbin/ldconfig

%post widgets-libs -p /sbin/ldconfig
%postun widgets-libs -p /sbin/ldconfig

%post file-widgets -p /sbin/ldconfig
%postun file-widgets -p /sbin/ldconfig

%post ntlm -p /sbin/ldconfig
%postun ntlm -p /sbin/ldconfig

%files
%license LICENSES/*.txt
%doc README.md

%files core
%{_opt_kf5_datadir}/locale/
%{_opt_kf5_sysconfdir}/xdg/accept-languages.codes
%{_opt_kf5_datadir}/qlogging-categories5/*categories
%{_opt_kf5_libexecdir}/kf5/kio_http_cache_cleaner
%{_opt_kf5_libexecdir}/kf5/kpac_dhcp_helper
%{_opt_kf5_libexecdir}/kf5/kioexec
%{_opt_kf5_libexecdir}/kf5/kioslave5
%{_opt_kf5_libexecdir}/kf5/kiod5
%{_opt_kf5_qtplugindir}/kf5/kio/
%{_opt_kf5_qtplugindir}/kf5/kded/
%{_opt_kf5_qtplugindir}/kcm_*.so
%{_opt_kf5_qtplugindir}/kf5/kiod/
%{_opt_kf5_datadir}/kservices5/*.desktop
%{_opt_kf5_datadir}/knotifications5/proxyscout.*
%{_opt_kf5_datadir}/kf5/kcookiejar/domain_info
%{_opt_kf5_datadir}/applications/*.desktop
%{_opt_kf5_bindir}/ktrash5
%{_opt_kf5_bindir}/kcookiejar5
%{_opt_kf5_datadir}/kconf_update/*
%{_opt_qt5_datadir}/dbus-1/services/org.kde.*.service

%files core-libs
%{_opt_kf5_libdir}/libKF5KIOCore.so.*

%files devel
%{_opt_qt5_datadir}/dbus-1/interfaces/*.xml
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_*.pri
%{_opt_kf5_bindir}/protocoltojson
%{_opt_kf5_datadir}/kdevappwizard/templates/kioworker.tar.bz2
%{_opt_kf5_includedir}/KF5/
%{_opt_kf5_libdir}/*.so
%{_opt_kf5_libdir}/cmake/KF5KIO/

%files gui
%{_opt_kf5_libdir}/libKF5KIOGui.so.*

%files widgets
#{_opt_kf5_datadir}/kservices5/fixhosturifilter.desktop
#{_opt_kf5_datadir}/kservices5/kshorturifilter.desktop
#{_opt_kf5_datadir}/kservices5/kuriikwsfilter.desktop
#{_opt_kf5_datadir}/kservices5/kurisearchfilter.desktop
#{_opt_kf5_datadir}/kservices5/localdomainurifilter.desktop
%config %{_opt_kf5_sysconfdir}/xdg/kshorturifilterrc
%dir %{_opt_qt5_plugindir}/kf5/urifilters/
%{_opt_kf5_datadir}/kservices5/searchproviders
%{_opt_kf5_datadir}/kservices5/webshortcuts.desktop
%{_opt_kf5_datadir}/kservicetypes5/*.desktop
%{_opt_qt5_plugindir}/kf5/urifilters/*.so
%{_opt_kf5_qtplugindir}/kcm_webshortcuts.so
%{_opt_kf5_qtplugindir}/plasma/kcms/systemsettings/kcm_smb.so
%{_opt_kf5_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_*.so

%files widgets-libs
%{_opt_kf5_libdir}/libKF5KIOWidgets.so.*
#{_opt_kf5_qtplugindir}/designer/*5widgets.so

%files file-widgets
%{_opt_kf5_libdir}/libKF5KIOFileWidgets.so.*

%files ntlm
%{_opt_kf5_libdir}/libKF5KIONTLM.so.*
