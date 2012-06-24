Summary:	Three-dimensional drawing with MetaPost output
Summary(pl.UTF-8):	Tworzenie trójwymiarowej grafiki z wyjściem w formacie MetaPost
Name:		3DLDF
Version:	1.1.5.1
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	ftp://ftp.gnu.org/gnu/3dldf/%{name}-%{version}.tar.gz
# Source0-md5:	abe73cec9db802c039c2399b87e2528b
Patch0:		%{name}-info.patch
URL:		http://wwwuser.gwdg.de/~lfinsto1/
BuildRequires:	libstdc++-devel
BuildRequires:	tetex
BuildRequires:	texinfo
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
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README DOC/TEXINFO/3DLDF.ps
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
