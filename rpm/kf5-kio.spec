%global kf5_version 5.105.0
%global framework kio

Name:			opt-kf5-kio
Version:		5.105.0
Release:		1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon with auto completion widgets and classes

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:		%{name}-%{version}.tar.bz2

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
#BuildRequires:  opt-kf5-kbookmarks-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kcompletion >= %{kf5_version}
BuildRequires:  opt-kf5-kconfigwidgets-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kiconthemes-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kitemviews-devel >= %{kf5_version}
#BuildRequires:  opt-kf5-kjobwidgets-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kwindowsystem-devel >= %{kf5_version}
# others
BuildRequires:  opt-kf5-knotifications-devel >= %{kf5_version}
#BuildRequires:  opt-kf5-ktextwidgets-devel >= %{kf5_version}
#BuildRequires:  opt-kf5-kwallet-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
#BuildRequires:  opt-kf5-kxmlgui-devel >= %{kf5_version}

BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qttools-devel

BuildRequires:  libacl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  zlib-devel
#BuildRequires:  cmake(Qt5UiPlugin)
#BuildRequires:  cmake(Qt5Qml)

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
#Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
#Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-ntlm%{?_isa} = %{version}-%{release}
#Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

%description
KDE Frameworks 5 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
%{?opt_kf5_default_filter}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires:       %{name}%{?_isa} = %{version}-%{release}
#Requires:       opt-kf5-kbookmarks-devel >= %{kf5_version}
Requires:       opt-kf5-kcompletion-devel >= %{kf5_version}
Requires:       opt-kf5-kconfig-devel >= %{kf5_version}
Requires:       opt-kf5-kcoreaddons-devel >= %{kf5_version}
Requires:       opt-kf5-kitemviews-devel >= %{kf5_version}
#Requires:       opt-kf5-kjobwidgets-devel >= %{kf5_version}
Requires:       opt-kf5-kservice-devel >= %{kf5_version}
Requires:       opt-kf5-solid-devel >= %{kf5_version}
#Requires:       opt-kf5-kxmlgui-devel >= %{kf5_version}
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
Requires: opt-kf5-solid >= %{kf5_version}
Requires: opt-kf5-karchive >= %{kf5_version}
Requires: opt-qt5-qtbase-gui

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
  -DKIOCORE_ONLY=ON \
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
#%{_opt_kf5_libexecdir}/kf5/kpac_dhcp_helper
#%{_opt_kf5_libexecdir}/kf5/kioexec
%{_opt_kf5_libexecdir}/kf5/kioslave5
%{_opt_kf5_libexecdir}/kf5/kiod5
%{_opt_kf5_qtplugindir}/kf5/kio/
%{_opt_kf5_qtplugindir}/kf5/kded/
#%{_opt_kf5_qtplugindir}/kcm_*.so
%{_opt_kf5_qtplugindir}/kf5/kiod/
%{_opt_kf5_datadir}/kservices5/*.desktop
#%{_opt_kf5_datadir}/knotifications5/proxyscout.*
#%{_opt_kf5_datadir}/kf5/kcookiejar/domain_info
%{_opt_kf5_datadir}/applications/*.desktop
%{_opt_kf5_bindir}/ktrash5
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

%files ntlm
%{_opt_kf5_libdir}/libKF5KIONTLM.so.*
