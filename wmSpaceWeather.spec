Summary:	wmSpaceWeather is a space weather monitor
Summary(pl):	wmSpaceWeather jest monitorem pogody kosmicznej
Name:		wmSpaceWeather
Version:	1.04
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	b91415bc9e234d3e6fcd93d34c7fd680
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmSpaceWeather is a space weather monitor. The monitor shows: 2
relativistic electron and 3 relativistic proton flux levels at
geosyncronous orbit (currently from the NOAA GOES spacecraft), current
Solar Flare X-ray flux, and the last 8 3-hour Kp index values.

%description -l pl
wmSpaceWeather jest monitorem pogody w przestrzeni kosmicznej.
Pokazuje 2 wzgl�dne elektronowe i 3 wzgl�dne protonowe poziomy
strumieni na geosynchronicznej orbicie (aktualnie sonda NOAA GEOS),
aktualne strumienie promieni X wiatru s�onecznego oraz ostatnie 8
3-godzinnych warto�ci indeksu Kp.

%prep
%setup -q

%build
%{__make} -C %{name} clean
%{__make} -C %{name} \
        CFLAGS="%{rpmcflags} -Wall" \
	INCDIR="-I%{_includedir}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/GetKp $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/GetKp
%{_mandir}/man1/*
%{_desktopdir}/docklets/wmSpaceWeather.desktop