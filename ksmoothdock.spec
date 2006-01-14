Summary:	KSmoothDock - a cool desktop panel
Summary(pl):	KSmoothDock - przyjemny panel dla pulpitu
Name:		ksmoothdock
Version:	3.6
Release:	1
License:	GPL v2
Group:		KDE/Applications
Source0:	http://dl.sourceforge.net/ksmoothdock/%{name}-%{version}.tar.gz
# Source0-md5:	4e169c14a1dae41357dc6b1176365442
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
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

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
