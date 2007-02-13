%define		_automakever	automake1.9
Summary:	KSmoothDock - a cool desktop panel
Summary(pl.UTF-8):	KSmoothDock - przyjemny panel dla pulpitu
Name:		ksmoothdock
Version:	4.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/ksmoothdock/%{name}-%{version}_%{_automakever}.tar.gz
# Source0-md5:	fa75237f0b1102d31dc2b60304ab59fc
URL:		http://www.kde-look.org/content/show.php?content=6585
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

%description -l pl.UTF-8
KSmoothDock to przyjemny panel dla pulpitu (podobnie jak kicker z KDE)
dla KDE 3.2 z gładkim powiększaniem (2 tryby: normalny i
paraboliczny). Jego celem jest dostarczenie alternatywy/dopełnienia
dla kickera. Jako że jest przeznaczony dla Linuksa z KDE, zachowanie
przypomina kickera.

%prep
%setup -q -n %{name}-%{version}_%{_automakever}

%build
%{__make} -f admin/Makefile.common cvs
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
