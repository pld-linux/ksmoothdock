Summary:	KSmoothDock - a cool desktop panel
Summary(pl):	KSmoothDock - przyjemny panel dla pulpitu
Name:		ksmoothdock
Version:	3.6.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/ksmoothdock/%{name}-%{version}.tar.gz
# Source0-md5:	f6d69c5d74de55f86bdc92e835df6cb8
URL:		http://kde-look.org/content/show.php?content=6585
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSmoothDock is a cool desktop panel (like KDE's kicker) for KDE 3.2
with smooth zooming (2 modes: normal and parabolic). Its aim is to
provide a cool alternative/complement to kicker. As it is intended for
KDE/Linux, its behaviour will be like that of kicker.

%description -l pl
KSmoothDock to przyjemny panel dla pulpitu (podobnie jak kicker z KDE)
dla KDE 3.2 z g³adkim powiêkszaniem (2 tryby: normalny i
paraboliczny). Jego celem jest dostarczenie alternatywy/dope³nienia
dla kickera. Jako ¿e jest przeznaczony dla Linuksa z KDE, zachowanie
przypomina kickera.

%prep
%setup -q -n %{name}

%build
%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	shelldesktopdir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/kde/*.desktop
%{_kdedocdir}/en/ksmoothdock
