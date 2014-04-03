#
# Conditional build:
%bcond_without	python	# Python binding

Summary:	Library to handle UPnP IGD port mapping
Summary(pl.UTF-8):	Biblioteka do obsługi odwzorowywania portów IGD dla UPnP
Name:		gupnp-igd
Version:	0.2.3
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-igd/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	c0a7b0c4a79e3f6cac45664d764519a4
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gobject-introspection-devel >= 0.10
BuildRequires:	gssdp-devel
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gupnp-devel >= 0.18.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-pygobject-devel >= 2.16.0}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.26
Requires:	gupnp >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to handle UPnP Internet Gateway Device port mappings.

%description -l pl.UTF-8
Biblioteka do obsługi odwzorowywania portów IGD (Internet Gateway
Device - bramek internetowych) dla UPnP.

%package devel
Summary:	Header files for gupnp-igd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gupnp-igd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26
Requires:	gupnp-devel >= 0.18.0

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
gupnp-igd library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gupnp-igd.

%package -n python-gupnp-igd
Summary:	gupnp-igd Python bindings
Summary(pl.UTF-8):	Wiązania Pythona do gupnp-igd
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject >= 2.16.0

%description -n python-gupnp-igd
gupnp-igd Python bindings.

%description -n python-gupnp-igd -l pl.UTF-8
Wiązania Pythona do gupnp-igd.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	%{?with_python:--enable-python} \
	--with-html-dir=%{_gtkdocdir}

# there are some races with gir generation
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gupnp/*.{a,la}
%endif

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgupnp-igd-1.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-igd-1.0.so.4
%{_libdir}/girepository-1.0/GUPnPIgd-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.0.so
%{_includedir}/gupnp-igd-1.0
%{_pkgconfigdir}/gupnp-igd-1.0.pc
%{_datadir}/gir-1.0/GUPnPIgd-1.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-igd-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-igd

%if %{with python}
%files -n python-gupnp-igd
%defattr(644,root,root,755)
%dir %{py_sitedir}/gupnp
%attr(755,root,root) %{py_sitedir}/gupnp/igd.so
%{py_sitedir}/gupnp/*.py[co]
%endif
