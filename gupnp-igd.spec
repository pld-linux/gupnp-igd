Summary:	Library to handle UPnP IGD port mapping
Name:		gupnp-igd
Version:	0.1.7
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.gupnp.org/sources/gupnp-igd/%{name}-%{version}.tar.gz
# Source0-md5:	75aaca3361046ac42125f81d07c072ac
URL:		http://www.gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gupnp-devel >= 0.13.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-pygobject-devel >= 2.16.0
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to handle UPnP Internet Gateway Device port mappings.

%package devel
Summary:	Header files for gupnp-igd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gupnp-igd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gupnp-devel >= 0.13.2

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

%package -n python-gupnp-igd
Summary:	gupnp-igd Python bindings
Summary(pl.UTF-8):	Wiązania Pythona do gupnp-igd
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

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
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -f $RPM_BUILD_ROOT%{py_sitedir}/gupnp/*.{a,la}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-igd-1.0.so.3

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

%files -n python-gupnp-igd
%defattr(644,root,root,755)
%dir %{py_sitedir}/gupnp
%attr(755,root,root) %{py_sitedir}/gupnp/igd.so
%{py_sitedir}/gupnp/*.py[co]
