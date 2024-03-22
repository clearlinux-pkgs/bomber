#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: f4bef72
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : bomber
Version  : 24.02.1
Release  : 65
URL      : https://download.kde.org/stable/release-service/24.02.1/src/bomber-24.02.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.1/src/bomber-24.02.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.1/src/bomber-24.02.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 LGPL-2.0
Requires: bomber-bin = %{version}-%{release}
Requires: bomber-data = %{version}-%{release}
Requires: bomber-license = %{version}-%{release}
Requires: bomber-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
THEMES IN BOMBER
----------------
This file explains the format of the themes used by bomber.

%package bin
Summary: bin components for the bomber package.
Group: Binaries
Requires: bomber-data = %{version}-%{release}
Requires: bomber-license = %{version}-%{release}

%description bin
bin components for the bomber package.


%package data
Summary: data components for the bomber package.
Group: Data

%description data
data components for the bomber package.


%package doc
Summary: doc components for the bomber package.
Group: Documentation

%description doc
doc components for the bomber package.


%package license
Summary: license components for the bomber package.
Group: Default

%description license
license components for the bomber package.


%package locales
Summary: locales components for the bomber package.
Group: Default

%description locales
locales components for the bomber package.


%prep
%setup -q -n bomber-24.02.1
cd %{_builddir}/bomber-24.02.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711067951
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711067951
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bomber
cp %{_builddir}/bomber-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/bomber/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/bomber-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/bomber/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/bomber-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/bomber/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/bomber-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/bomber/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/bomber-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/bomber/a4c60b3fefda228cd7439d3565df043192fef137 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang bomber
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/bomber
/usr/bin/bomber

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.bomber.desktop
/usr/share/bomber/sounds/bomb.ogg
/usr/share/bomber/sounds/crash.ogg
/usr/share/bomber/themes/Lava-Island.desktop
/usr/share/bomber/themes/Lava-Island.svgz
/usr/share/bomber/themes/kbomber.desktop
/usr/share/bomber/themes/kbomber.png
/usr/share/bomber/themes/kbomber.svgz
/usr/share/bomber/themes/lava-Island.png
/usr/share/config.kcfg/bomber.kcfg
/usr/share/icons/hicolor/128x128/apps/bomber.png
/usr/share/icons/hicolor/32x32/apps/bomber.png
/usr/share/icons/hicolor/48x48/apps/bomber.png
/usr/share/icons/hicolor/64x64/apps/bomber.png
/usr/share/metainfo/org.kde.bomber.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/bomber/index.cache.bz2
/usr/share/doc/HTML/ca/bomber/index.docbook
/usr/share/doc/HTML/cs/bomber/index.cache.bz2
/usr/share/doc/HTML/cs/bomber/index.docbook
/usr/share/doc/HTML/de/bomber/index.cache.bz2
/usr/share/doc/HTML/de/bomber/index.docbook
/usr/share/doc/HTML/en/bomber/index.cache.bz2
/usr/share/doc/HTML/en/bomber/index.docbook
/usr/share/doc/HTML/en/bomber/mainscreen.png
/usr/share/doc/HTML/es/bomber/index.cache.bz2
/usr/share/doc/HTML/es/bomber/index.docbook
/usr/share/doc/HTML/et/bomber/index.cache.bz2
/usr/share/doc/HTML/et/bomber/index.docbook
/usr/share/doc/HTML/fr/bomber/index.cache.bz2
/usr/share/doc/HTML/fr/bomber/index.docbook
/usr/share/doc/HTML/gl/bomber/index.cache.bz2
/usr/share/doc/HTML/gl/bomber/index.docbook
/usr/share/doc/HTML/it/bomber/index.cache.bz2
/usr/share/doc/HTML/it/bomber/index.docbook
/usr/share/doc/HTML/nl/bomber/index.cache.bz2
/usr/share/doc/HTML/nl/bomber/index.docbook
/usr/share/doc/HTML/pl/bomber/index.cache.bz2
/usr/share/doc/HTML/pl/bomber/index.docbook
/usr/share/doc/HTML/pt/bomber/index.cache.bz2
/usr/share/doc/HTML/pt/bomber/index.docbook
/usr/share/doc/HTML/pt_BR/bomber/index.cache.bz2
/usr/share/doc/HTML/pt_BR/bomber/index.docbook
/usr/share/doc/HTML/sv/bomber/index.cache.bz2
/usr/share/doc/HTML/sv/bomber/index.docbook
/usr/share/doc/HTML/uk/bomber/index.cache.bz2
/usr/share/doc/HTML/uk/bomber/index.docbook
/usr/share/doc/HTML/uk/bomber/mainscreen.png
/usr/share/doc/HTML/zh_CN/bomber/index.cache.bz2
/usr/share/doc/HTML/zh_CN/bomber/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bomber/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/bomber/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/bomber/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/bomber/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/bomber/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f bomber.lang
%defattr(-,root,root,-)

