Name: SphinxTrain
Version: 1.0
Release: %mkrel 1
Summary: An acoustic model trainer for CMU's Sphinx tools
Group: Applications/Multimedia
License: BSD and LGPLv2+
URL: http://www.cmusphinx.org/
Source: http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: blas-devel, festival, lapack-devel, perl, python-devel
BuildRequires: python-setuptools, python-scipy

%description
SphinxTrain is Carnegie Mellon University's open source acoustic model
trainer.  It contains the scripts and instructions necessary for building
models for the CMU Sphinx Recognizer.

%prep
%setup -q
# Remove spurious executable bits
chmod a-x src/libs/libmllr/*.c include/s3/lexicon.h
# Fix a typo
sed -i -e 's|/usr/bni|/usr/bin|' python/sphinx/arpalm_test.py

%build
%configure
# The configure script only turns PIC on for x86_64 architectures
if [[ ! $(grep -F 'PIC' config/config) ]]; then
  sed -i 's/-Wall/-Wall -fPIC -DPIC/' config/config
fi
%make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}
cd %{buildroot}%{_libdir}/%{name}
%{buildroot}%{name}-%{version}/scripts_pl/setup_SphinxTrain.pl -task Mandriva
sed -e "s|\\\$CFG_BASE_DIR = .*;|\\\$CFG_BASE_DIR = \"%{_libdir}/%{name}\";|" \
    -i etc/sphinx_train.cfg
# The installer ADDS spurious executable bits
chmod a-x python/sphinx/__init__.py python/sphinx/arpalm.py \
  python/sphinx/corpus.py python/sphinx/divergence.py python/sphinx/feat/*.py \
  python/sphinx/gmm.py python/sphinx/hmm.py python/sphinx/htkmfc.py \
  python/sphinx/hypseg.py python/sphinx/lattice.py python/sphinx/mfcc.py \
  python/sphinx/s2mfc.py python/sphinx/s3file.py python/sphinx/s3gau.py \
  python/sphinx/s3gaucnt.py python/sphinx/s3lda.py python/sphinx/s3mdef.py \
  python/sphinx/s3mixw.py python/sphinx/s3model.py python/sphinx/s3tmat.py \
  scripts_pl/lib/*.pm scripts_pl/lib/Queue/*.pm scripts_pl/lib/SphinxTrain/*.pm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.tracing README.txt ReleaseNotes
%doc doc/s3_fe_spec.pdf doc/tinydoc.txt src/programs/README
%{_libdir}/%{name}
