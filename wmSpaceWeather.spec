Summary: 	wmSpaceWeather is a space weather monitor
Summary(lp):	wmSpaceWeather jest monitorem pogody kosmicznej
Name: 		wmSpaceWeather
Version:	1.02
Release:	2
Copyright:	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Source0: 	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmSpaceWeather.wmconfig
BuildPrereq:    XFree86-devel
BuildPrereq:    xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
wmSpaceWeather is a space weather monitor. The monitor shows:
2 relativistic electron and 3 relativistic  proton flux levels
at geosyncronous  orbit (currently from the NOAA GOES spacecraft),
current Solar Flare X-ray flux, and the last 8 3-hour Kp index values.

%description -l pl
wmSpaceWeather jest monitorem pogody w przestrzeni kosmiczej. 

%prep
%setup -q

%build
make -C %{name} \
        CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT/etc/X11/wmconfig

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/GetKp $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

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

/etc/X11/wmconfig/%{name}

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.02-2]
- spec file modified for PLD use,
- package is FHS 2.0 compliant.

* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release.
