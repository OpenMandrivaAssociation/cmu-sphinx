Name: pocketsphinx
Version: 0.6.1
Release: %mkrel 1
Summary: Real-time speech recognition
Group: Applications/Multimedia
License: BSD and LGPLv2+
URL: https://www.pocketsphinx.org/
Source: http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: pkgconfig, python-setuptools, sphinxbase-devel
Requires: sphinxbase

%description
PocketSphinx is a version of the open-source Sphinx-II speech recognition
system which is able to recognize speech in real-time.  While it may be
somewhat less accurate than the offline speech recognizers, it is lightweight
enough to run on handheld and embedded devices.

%package devel
Summary: Header files for developing with pocketsphinx
Group: Applications/Multimedia
Requires: %{name}-libs = %{version}-%{release}, pkgconfig
Requires: sphinxbase-devel

%description devel
Header files for developing with pocketsphinx.

%package libs
Summary: Shared libraries for pocketsphinx executables
Group: Applications/Multimedia

%description libs
Shared libraries for pocketsphinx executables.

%package python
Summary: Python interface to pocketsphinx
Group: Applications/Multimedia
Requires: %{name}-libs = %{version}-%{release}, sphinxbase-python

%description python
Python interface to pocketsphinx.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --disable-dependency-tracking --disable-static
%make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{python_sitearch}
%makeinstall
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/pocketsphinx
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/libpocketsphinx.so
%{_libdir}/libpocketsphinx.la
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%defattr(-,root,root,-)
%{_libdir}/libpocketsphinx.so.*

%files python
%defattr(-,root,root,-)
%{_libdir}/python2.6/site-packages/*
