%define		_name MCP-plugins
Summary:	The Moog VCF, chorus and phaser LADSPA plugins
Summary(pl):	Wtyczki LADSPA - Moog VCF, chorus i phaser
Name:		ladspa-mcp-plugins
Version:	0.0.2
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://alsamodular.sourceforge.net/%{_name}-%{version}.tar.bz2
# Source0-md5:	fd4d725c21ce836275bfc012a68002a3
Patch0:		%{name}-misc_fixes.patch
URL:		http://alsamodular.sourceforge.net/
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This LADSPA plugin contains a digital implementation of the voltage
controlled lowpass filter (used in Moog synthesizers), chorus and
phaser effects.

%description -l pl
Ta wtyczka LADSPA zawiera cyfrow± implementacjê sterowanego napiêciem
filtra dolnoprzepustowego (u¿ywany w syntezatorach Moog) oraz efekty
chorus i phaser.

%package ams-examples
Summary:	Examples for Alsa Modular Synth
Summary(pl):	Przyk³ady dla Alsa Modular Synth
Group:		Applications/Sound
Requires:	alsa-modular-synth

%description ams-examples
Some examples for Alsa Modular Synth.

%description ams-examples -l pl
Pare przyk³adów wykorzystania z Alsa Modular Synth.

%prep
%setup -q -n %{_name}-%{version}
%patch -p1

%build
%{__make} CPPFLAGS="-I. -I%{_includedir} -fPIC -D_REENTRANT -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/ladspa,%{_datadir}/ams}
%{__make} DESTDIR=$RPM_BUILD_ROOT install
cp ams/* $RPM_BUILD_ROOT%{_datadir}/ams

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/*.so

%files ams-examples
%defattr(644,root,root,755)
%{_datadir}/ams/*.ams
