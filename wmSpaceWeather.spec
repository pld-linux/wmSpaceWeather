Summary: wmSpaceWeather is a space weather monitor
%define version 1.02
Name: wmSpaceWeather
Version: %{version}
Release: 1
Copyright: GPL
Group: X Windows/Window Managers
Source: ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Packager: Ian Macdonald <ianmacd@xs4all.nl>
BuildRoot: /var/tmp/%{name}-root

%description
wmSpaceWeather is a space weather monitor. The monitor shows:
2 relativistic electron and 3 relativistic  proton flux levels
at geosyncronous  orbit (currently from the NOAA GOES spacecraft),
current Solar Flare X-ray flux, and the last 8 3-hour Kp index values.

%prep
%setup

%build
make -C %{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}
install -s -m 755 %{name}/%{name} $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -m 755 %{name}/GetKp $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 444 %{name}/%{name}.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1

%files
%defattr(-,root,root)
/usr/X11R6/bin/%{name}
/usr/X11R6/bin/GetKp
/usr/X11R6/man/man1/%{name}.1
%doc BUGS CHANGES COPYING HINTS INSTALL README

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>

- first RPM release
