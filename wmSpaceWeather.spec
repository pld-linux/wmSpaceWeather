Summary:	wmSpaceWeather is a space weather monitor
Summary(pl):	wmSpaceWeather jest monitorem pogody kosmicznej
Name:		wmSpaceWeather
Version:	1.04
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
wmSpaceWeather is a space weather monitor. The monitor shows: 2
relativistic electron and 3 relativistic proton flux levels at
geosyncronous orbit (currently from the NOAA GOES spacecraft), current
Solar Flare X-ray flux, and the last 8 3-hour Kp index values.

%description -l pl
wmSpaceWeather jest monitorem pogody w przestrzeni kosmicznej.
Pokazuje 2 wzgl�dne elektronowe i 3 wzgl�dne protonowe poziomy
strumieni na geosynchronicznej orbicie (aktualnie sonda NOAA GEOS),
aktulne strumienie promieni X wiatru s�onecznego oraz ostatnie 8
3-godzinnych warto�ci indexu Kp.

%prep
%setup -q

%build
%{__make} -C %{name} clean
%{__make} -C %{name} \
        CFLAGS="%{rpmcflags} -Wall" \
	INCDIR="-I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/GetKp $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf BUGS CHANGES HINTS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/GetKp
%{_mandir}/man1/*
#%{_applnkdir}/DockApplets/wmSpaceWeather.desktop
