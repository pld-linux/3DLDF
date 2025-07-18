Summary:	Three-dimensional drawing with MetaPost output
Summary(pl.UTF-8):	Tworzenie trójwymiarowej grafiki z wyjściem w formacie MetaPost
Name:		3DLDF
Version:	2.0.3
Release:	7
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://ftp.gnu.org/gnu/3dldf/%{name}-%{version}.tar.gz
# Source0-md5:	5e669f4efd3d576d42308ba61619a63f
Patch0:		%{name}-info.patch
Patch1:		upstream-cleanup-permissive_cxx_code.patch
Patch2:		upstream-gcc-init_priority.patch
Patch3:		upstream-sys-std_numeric_limits.patch
Patch4:		upstream-w2help2man.patch
Patch5:		%{name}-gcc6.patch
URL:		http://www.gnu.org/software/3dldf/
# ps2pdf
BuildRequires:	ghostscript
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	texlive
BuildRequires:	texlive-fonts-type1-hoekwater
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3DLDF is a package for three-dimensional drawing with MetaPost output.
It is intended, among other things, to provide a convenient way of
creating 3D graphics for inclusion in TeX documents.
 
%description -l pl.UTF-8
3DLF to pakiet do tworzenia trójwymiarowej grafiki z wyjściem w
formacie MetaPost. Ma on służyć między innymi do udostępnienia
wygodnego sposobu tworzenia grafiki 3D w celu włączenia do dokumentów
w TeXu.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
# only 3dlfb binary uses libs, symbols are messed - no sense in building shared libs
%configure \
	--disable-shared
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D doc/3dldf.info $RPM_BUILD_ROOT%{_infodir}/3dldf.info

# headers not installed
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib3dldf*.{la,a}
# too common name
%{__rm} $RPM_BUILD_ROOT%{_bindir}/dummy

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/3dldf
%attr(755,root,root) %{_bindir}/prbsnflx
%{_infodir}/3dldf.info*
