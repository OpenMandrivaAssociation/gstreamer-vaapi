%define api 1.0
%define major 0
%define libname %mklibname gstreamer-vaapi %{api} %{major}
%define devellibname %mklibname gstreamer-vaapi -d

Name:		gstreamer-vaapi
Version:	1.10.2
Release:	1
Summary:	A collection of VA-API based plugins for GStreamer and helper libraries
Group:		System/Libraries
License:	LGPLv2+ and GPLv2+
URL:		https://github.com/01org/gstreamer-vaapi
Source0:	http://www.freedesktop.org/software/vaapi/releases/gstreamer-vaapi/%{name}-%{version}.tar.xz
BuildRequires:	nasm
BuildRequires:	yasm
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(wayland-client)

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
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Obsoletes:      %{mklibname -d gstvaapi 0.10}

%description -n %{devellibname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files -n %{libname}
%doc NEWS README
%{_libdir}/*%{api}.so.%{major}*
%{_libdir}/gstreamer-%{api}/*.so
%exclude %{_libdir}/gstreamer-%{api}/*.a
%exclude %{_libdir}/gstreamer-%{api}/*.la
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%files -n %{devellibname}
%{_includedir}/gstreamer-%{api}/gst/vaapi
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
