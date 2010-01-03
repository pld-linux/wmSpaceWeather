Summary:	wmSpaceWeather is a space weather monitor
Summary(pl.UTF-8):	wmSpaceWeather jest monitorem pogody kosmicznej
Name:		wmSpaceWeather
Version:	1.04
Release:	9
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	b91415bc9e234d3e6fcd93d34c7fd680
Source1:	%{name}.desktop
Source2:	%{name}.Makefile
Patch0:		%{name}-fix.patch
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmSpaceWeather is a space weather monitor. The monitor shows: 2
relativistic electron and 3 relativistic proton flux levels at
geosynchronous orbit (currently from the NOAA GOES spacecraft),
current Solar Flare X-ray flux, and the last 8 3-hour Kp index values.

%description -l pl.UTF-8
wmSpaceWeather jest monitorem pogody w przestrzeni kosmicznej.
Pokazuje poziom strumienia relatywistycznych elektronów (oddzielnie
dla 2 przedziałów energii) oraz wartości strumienia relatywistycznych
protonów (oddzielnie dla 3 przedziałów energii) mierzonego na orbicie
geosynchronicznej (aktualnie sondą NOAA GEOS), aktualne strumienie
promieniowania rentgenowskiego z wiatru słonecznego oraz ostatnie 8
3-godzinnych wartości indeksu Kp.

%prep
%setup -q
%patch0 -p1

awk '/OBJS *=/{p=1} {if(p)print} !/\\$/{p=0}' wmSpaceWeather/Makefile \
	> wmSpaceWeather/Makefile.include

cat << 'EOF' >> wmSpaceWeather/Makefile.include
NAME = %{name}
EXTRABIN = GetKp
MAN1FILE = %{name}.1
DOCKLETFILE = %{SOURCE1}
CC = %{__cc}
OPTCFLAGS = %{rpmcflags}
LDFLAGS = %{rpmldflags}
EOF

install %{SOURCE2} wmSpaceWeather/Makefile

%build
%{__make} -C wmSpaceWeather clean
%{__make} -C wmSpaceWeather

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C wmSpaceWeather install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/GetKp
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/docklets/wmSpaceWeather.desktop
