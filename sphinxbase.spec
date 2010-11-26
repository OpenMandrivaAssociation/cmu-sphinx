Name: sphinxbase
Version: 0.6.1
Release: %mkrel 1
BuildRoot: %{_tmppath}/%{name}-%{version}
Summary: Base files of CMU Sphinx Recognition System
Group: Applications/Multimedia
License: BSD and LGPLv2+
Url: http://cmusphinx.sourceforge.net/
Source: http://downloads.sourceforge.net/cmusphinx/%name-%version.tar.gz

%description
The CMU Sphinx Recognition System is a library and a set
of examples and utilities for speech recognition.

This package will install the cmu-sphinx library and some examples.

%package devel
Summary: Header files for developing with sphinxbase
Group: Applications/Multimedia
Requires: pkgconfig

%description devel
Header files for developing with sphinxbase

%prep
%setup -q -n %{name}-%{version}

%build
./autogen.sh
%configure
%make %{?_smp_mflags}

%install
rm -fr %{buildroot}
%makeinstall

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/sphinx*
%{_libdir}/libsphinx*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/python2.6/site-packages/*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
