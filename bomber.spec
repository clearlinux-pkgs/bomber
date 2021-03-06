#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : bomber
Version  : 21.04.2
Release  : 30
URL      : https://download.kde.org/stable/release-service/21.04.2/src/bomber-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/bomber-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/bomber-21.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 LGPL-2.0
Requires: bomber-bin = %{version}-%{release}
Requires: bomber-data = %{version}-%{release}
Requires: bomber-license = %{version}-%{release}
Requires: bomber-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n bomber-21.04.2
cd %{_builddir}/bomber-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623360745
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623360745
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bomber
cp %{_builddir}/bomber-21.04.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/bomber/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/bomber-21.04.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/bomber/a4c60b3fefda228cd7439d3565df043192fef137
pushd clr-build
%make_install
popd
%find_lang bomber

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bomber/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/bomber/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f bomber.lang
%defattr(-,root,root,-)

