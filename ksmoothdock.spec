Summary:	KSmoothDock - a cool desktop panel
Summary(pl):	KSmoothDock - przyjemny panel dla pulpitu
Name:		ksmoothdock
Version:	3.6.1
Release:	1
License:	GPL v2
Group:		KDE/Applications
Source0:	http://dl.sourceforge.net/ksmoothdock/%{name}-%{version}.tar.gz
# Source0-md5:	f6d69c5d74de55f86bdc92e835df6cb8
URL:		http://kde-look.org/content/show.php?content=6585
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSmoothDock is a cool desktop panel (like KDE's kicker) for KDE 3.2
with smooth zooming (2 modes: normal and parabolic). Its aim is to
provide a cool alternative/complement to kicker. As it is intended for
KDE/Linux, its behaviour will be like that of kicker.

%description -l pl
KSmoothDock to przyjemny panel dla pulpitu (podobnie jak kicker z KDE)
dla KDE 3.2 z g�adkim powi�kszaniem (2 tryby: normalny i
paraboliczny). Jego celem jest dostarczenie alternatywy/dope�nienia
dla kickera. Jako �e jest przeznaczony dla Linuksa z KDE, zachowanie
przypomina kickera.

%prep
%setup -q -n %{name}

%build
rm -f acinclude.m4
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
