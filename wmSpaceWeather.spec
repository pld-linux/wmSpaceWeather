Summary: 	wmSpaceWeather is a space weather monitor
Summary(lp):	wmSpaceWeather jest monitorem pogody kosmicznej
Name: 		wmSpaceWeather
Version:	1.04
Release:	2
Copyright:	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Source0: 	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmSpaceWeather.desktop
BuildRequires:    XFree86-devel
BuildRequires:    xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6
%define _mandir %{_prefix}/man

%description
wmSpaceWeather is a space weather monitor. The monitor shows: 2 relativistic
electron and 3 relativistic proton flux levels at geosyncronous orbit
(currently from the NOAA GOES spacecraft), current Solar Flare X-ray flux,
and the last 8 3-hour Kp index values.

%description -l pl
wmSpaceWeather jest monitorem "pogody" w przestrzeni kosmiczej.

%prep
%setup -q

%build
make -C %{name} clean
make -C %{name} \
        CFLAGS="$RPM_OPT_FLAGS -Wall" \
	INCDIR="-I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/GetKp $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

gzip -9nf BUGS CHANGES HINTS README \
        $RPM_BUILD_ROOT%{_mandir}/man1/*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS,README}.gz
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/GetKp
%{_mandir}/man1/*

/usr/X11R6/share/applnk/DockApplets/wmSpaceWeather.desktop
