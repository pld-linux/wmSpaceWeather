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
BuildRoot:      /tmp/%{name}-%{version}-root

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
make -C wmSpaceWeather \
        CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/{bin,share/man/man1}}

install -s wmSpaceWeather/wmSpaceWeather $RPM_BUILD_ROOT/usr/X11R6/bin
install wmSpaceWeather/GetKp $RPM_BUILD_ROOT/usr/X11R6/bin
install wmSpaceWeather/wmSpaceWeather.1 $RPM_BUILD_ROOT/usr/X11R6/share/man/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmSpaceWeather

gzip -9nf BUGS CHANGES HINTS README \
        $RPM_BUILD_ROOT/usr/X11R6/share/man/man1/wmSpaceWeather.1


%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS,README}.gz
%attr(755,root,root) /usr/X11R6/bin/wmSpaceWeather
%attr(755,root,root) /usr/X11R6/bin/GetKp
/usr/X11R6/share/man/man1/wmSpaceWeather.1.gz

/etc/X11/wmconfig/wmSpaceWeather

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.02-2]
- spec file modified for PLD use,
- package is FHS 2.0 compliant.

* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release
