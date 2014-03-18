Summary:	X.org video driver for NVIDIA graphics chipsets
Name:		xorg-driver-video-nouveau
Version:	1.0.10
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/driver/xf86-video-nouveau-%{version}.tar.bz2
# Source0-md5:	44fd65897630fdd19c086133cc1bd679
URL:		http://nouveau.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libpciaccess-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	udev-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-libXvMC-devel
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for NVIDIA video adapters.

%prep
%setup -qn xf86-video-nouveau-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/*.so
%{_mandir}/man4/nouveau.4*

