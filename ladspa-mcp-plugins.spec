%define		_name MCP-plugins
Summary:	The Moog VCF, chorus and phaser LADSPA plugins
Summary(pl):	Wtyczki LADSPA - Moog VCF, chorus i phaser
Name:		ladspa-mcp-plugins
Version:	0.2.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://users.skynet.be/solaris/linuxaudio/downloads/%{_name}-%{version}.tar.bz2
# Source0-md5:	97c7956fadced24be2768d1abe04aead
Patch0:		%{name}-misc_fixes.patch
URL:		http://users.skynet.be/solaris/linuxaudio/
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
Obsoletes:	%{name}-alsa-modular-synth-examples
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This LADSPA plugin contains a digital implementation of the voltage
controlled lowpass filter (used in Moog synthesizers), chorus and
phaser effects.

%description -l pl
Ta wtyczka LADSPA zawiera cyfrow± implementacjê sterowanego napiêciem
filtra dolnoprzepustowego (u¿ywanego w syntezatorach Moog) oraz efekty
chorus i phaser.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/*.so
