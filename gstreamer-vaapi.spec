%define api 1.0
%define major 0
%define libname %mklibname gstreamer-vaapi %{api} %{major}
%define devellibname %mklibname gstreamer-vaapi -d

Name:		gstreamer-vaapi
Version:	1.24.6
Release:	1
Summary:	A collection of VA-API based plugins for GStreamer and helper libraries
Group:		System/Libraries
License:	LGPLv2+ and GPLv2+
URL:		https://gstreamer.freedesktop.org/modules/gstreamer-vaapi.html
Source0:	https://gstreamer.freedesktop.org/src/gstreamer-vaapi/%{name}-%{version}.tar.xz
BuildRequires: meson
BuildRequires: nasm
BuildRequires: yasm
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires: pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
Obsoletes:	%{mklibname gstreamer-vaapi -d} < 1.10.2

%description
Gstreamer-vaapi is a collection of VA-API based plugins for GStreamer
and helper libraries. vaapidecode is used to decode MPEG-2, MPEG-4,
H.264, VC-1, WMV3 videos to video/x-vaapi-surface surfaces, depending
on the underlying HW capabilities. vaapiconvert is used to convert from
video/x-raw-yuv pixels to video/x-vaapi-surface surfaces. vaapisink is
used to display video/x-vaapi-surface surfaces to the screen. 

%package -n %{libname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	gstreamer1.0-vaapi = %{EVRD}
Obsoletes:	gstreamer0.10-vaapi
Obsoletes:	%{mklibname gstvaapi 0.10 0}

%description -n %{libname}
Gstreamer-vaapi is a collection of VA-API based plugins for GStreamer
and helper libraries. vaapidecode is used to decode MPEG-2, MPEG-4,
H.264, VC-1, WMV3 videos to video/x-vaapi-surface surfaces, depending
on the underlying HW capabilities. vaapiconvert is used to convert from
video/x-raw-yuv pixels to video/x-vaapi-surface surfaces. vaapisink is
used to display video/x-vaapi-surface surfaces to the screen. 

%package -n %{devellibname}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devellibname}
Development files for gstreamer-vaapi.

%prep
%autosetup -p1

%build
%meson \
       -Ddoc=disabled \
       -Dencoders=enabled \
       -Ddrm=enabled \
       -Dx11=enabled \
       -Dglx=enabled \
       -Dwayland=enabled \
       -Degl=enabled \
       --buildtype=release

#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%meson_build

%install
%meson_install
rm -rf %{buildroot}/%{_datadir}/gtk-doc/

%files -n %{libname}
%doc NEWS README
%{_libdir}/gstreamer-%{api}/*.so

