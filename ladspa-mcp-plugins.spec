%define		_name MCP-plugins
Summary:	The Moog VCF, chorus and phaser LADSPA plugins
Summary(pl):	Wtyczki LADSPA - Moog VCF, chorus i phaser
Name:		ladspa-mcp-plugins
Version:	0.2.1b
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://alsamodular.sourceforge.net/%{_name}-%{version}.tar.bz2
# Source0-md5:	69d515102f0683b51f3571866bbd3f76
Patch0:		%{name}-misc_fixes.patch
URL:		http://alsamodular.sourceforge.net/
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This LADSPA plugin contains a digital implementation of the voltage
controlled lowpass filter (used in Moog synthesizers), chorus and
phaser effects.

%description -l pl
Ta wtyczka LADSPA zawiera cyfrow± implementacjê sterowanego napiêciem
filtra dolnoprzepustowego (u¿ywanego w syntezatorach Moog) oraz efekty
chorus i phaser.

%package alsa-modular-synth-examples
Summary:	Examples for Alsa Modular Synth
Summary(pl):	Przyk³ady dla Alsa Modular Synth
Group:		Applications/Sound
Requires:	alsa-modular-synth

%description alsa-modular-synth-examples
Some examples for Alsa Modular Synth.

%description alsa-modular-synth-examples -l pl
Parê przyk³adów wykorzystania wtyczki z Alsa Modular Synth.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%{__make} \
	CPPFLAGS="-I. -fPIC -D_REENTRANT -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/ladspa,%{_datadir}/ams/examples}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT install

install ams/* $RPM_BUILD_ROOT%{_datadir}/ams/examples

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/*.so

%files alsa-modular-synth-examples
%defattr(644,root,root,755)
%{_datadir}/ams/examples/*.ams
