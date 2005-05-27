Summary:	KSmoothDock is a cool desktop panel
Name:		ksmoothdock
Version:	3.5.1
Release:	0.1
License:	GPL v2
Group:		KDE/Applications
Source0:	http://dl.sourceforge.net/ksmoothdock/%{name}-%{version}.tar.gz
# Source0-md5:	df2bcbbafbf0726db802c6434012eb7c
URL:		http://kde-look.org/content/show.php?content=6585
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSmoothDock is a cool desktop panel (like KDE's kicker) for KDE 3.2
with smooth zooming (2 modes: normal and parabolic). Its aim is to
provide a cool alternative/complement to kicker. As it is intended for
KDE/Linux, its behaviour will be like that of kicker.

%prep
%setup -q

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
