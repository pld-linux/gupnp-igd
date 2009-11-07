Summary:	Library to handle UPnP IGD port mapping
Name:		gupnp-igd
Version:	0.1.3
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.gupnp.org/sources/gupnp-igd/%{name}-%{version}.tar.gz
# Source0-md5:	ea0afa85c19fda67ef0ae54fa4faeb9f
URL:		http://www.gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gupnp-devel >= 0.12.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to handle UPnP Internet Gateway Device port mappings.

%package devel
Summary:	Header files for gupnp-igd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gupnp-igd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gupnp-devel >= 0.12.3

%description devel
Header files for gupnp-igd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gupnp-igd.

%package static
Summary:	Static gupnp-igd library
Summary(pl.UTF-8):	Statyczna biblioteka gupnp-igd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gupnp-igd library.

%description static -l pl.UTF-8
Statyczna biblioteka gupnp-igd.

%package apidocs
Summary:	gupnp-igd library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gupnp-igd
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gupnp-igd library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gupnp-igd.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-igd-1.0.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.0.so
%{_libdir}/libgupnp-igd-1.0.la
%{_includedir}/gupnp-igd-1.0
%{_pkgconfigdir}/gupnp-igd-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-igd-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-igd
