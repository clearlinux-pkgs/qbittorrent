#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0x6E4A2D025B7CC9A2 (hammered999@gmail.com)
#
Name     : qbittorrent
Version  : 4.6.4
Release  : 43
URL      : https://sourceforge.net/projects/qbittorrent/files/qbittorrent/qbittorrent-4.6.4/qbittorrent-4.6.4.tar.xz
Source0  : https://sourceforge.net/projects/qbittorrent/files/qbittorrent/qbittorrent-4.6.4/qbittorrent-4.6.4.tar.xz
Source1  : https://sourceforge.net/projects/qbittorrent/files/qbittorrent/qbittorrent-4.6.4/qbittorrent-4.6.4.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: qbittorrent-bin = %{version}-%{release}
Requires: qbittorrent-data = %{version}-%{release}
Requires: qbittorrent-license = %{version}-%{release}
Requires: qbittorrent-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-configure
BuildRequires : openssl-dev
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libtorrent-rasterbar)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)
BuildRequires : qttools-dev
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
qBittorrent - A BitTorrent client in Qt
------------------------------------------

%package bin
Summary: bin components for the qbittorrent package.
Group: Binaries
Requires: qbittorrent-data = %{version}-%{release}
Requires: qbittorrent-license = %{version}-%{release}

%description bin
bin components for the qbittorrent package.


%package data
Summary: data components for the qbittorrent package.
Group: Data

%description data
data components for the qbittorrent package.


%package license
Summary: license components for the qbittorrent package.
Group: Default

%description license
license components for the qbittorrent package.


%package man
Summary: man components for the qbittorrent package.
Group: Default

%description man
man components for the qbittorrent package.


%prep
%setup -q -n qbittorrent-4.6.4
cd %{_builddir}/qbittorrent-4.6.4
pushd ..
cp -a qbittorrent-4.6.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711374707
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711374707
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qbittorrent
cp %{_builddir}/qbittorrent-%{version}/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/qbittorrent/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qbittorrent-%{version}/COPYING.GPLv3 %{buildroot}/usr/share/package-licenses/qbittorrent/31a3d460bb3c7d98845187c716a30db81c44b615 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/qbittorrent
/usr/bin/qbittorrent

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.qbittorrent.qBittorrent.desktop
/usr/share/icons/hicolor/128x128/apps/qbittorrent.png
/usr/share/icons/hicolor/128x128/status/qbittorrent-tray.png
/usr/share/icons/hicolor/16x16/apps/qbittorrent.png
/usr/share/icons/hicolor/16x16/status/qbittorrent-tray.png
/usr/share/icons/hicolor/192x192/apps/qbittorrent.png
/usr/share/icons/hicolor/192x192/status/qbittorrent-tray.png
/usr/share/icons/hicolor/22x22/apps/qbittorrent.png
/usr/share/icons/hicolor/22x22/status/qbittorrent-tray.png
/usr/share/icons/hicolor/24x24/apps/qbittorrent.png
/usr/share/icons/hicolor/24x24/status/qbittorrent-tray.png
/usr/share/icons/hicolor/32x32/apps/qbittorrent.png
/usr/share/icons/hicolor/32x32/status/qbittorrent-tray.png
/usr/share/icons/hicolor/36x36/apps/qbittorrent.png
/usr/share/icons/hicolor/36x36/status/qbittorrent-tray.png
/usr/share/icons/hicolor/48x48/apps/qbittorrent.png
/usr/share/icons/hicolor/48x48/status/qbittorrent-tray.png
/usr/share/icons/hicolor/64x64/apps/qbittorrent.png
/usr/share/icons/hicolor/64x64/status/qbittorrent-tray.png
/usr/share/icons/hicolor/72x72/apps/qbittorrent.png
/usr/share/icons/hicolor/72x72/status/qbittorrent-tray.png
/usr/share/icons/hicolor/96x96/apps/qbittorrent.png
/usr/share/icons/hicolor/96x96/status/qbittorrent-tray.png
/usr/share/icons/hicolor/scalable/apps/qbittorrent.svg
/usr/share/icons/hicolor/scalable/status/qbittorrent-tray-dark.svg
/usr/share/icons/hicolor/scalable/status/qbittorrent-tray-light.svg
/usr/share/icons/hicolor/scalable/status/qbittorrent-tray.svg
/usr/share/metainfo/org.qbittorrent.qBittorrent.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qbittorrent/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/qbittorrent/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/qbittorrent.1
