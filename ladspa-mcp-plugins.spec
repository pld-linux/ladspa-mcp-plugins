Summary:	The Moog VCF, chorus and phaser LADSPA plugins
Summary(pl.UTF-8):	Wtyczki LADSPA - Moog VCF, chorus i phaser
Name:		ladspa-mcp-plugins
Version:	0.4.0
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/MCP-plugins-%{version}.tar.bz2
# Source0-md5:	2a0fc50281a150eb781dbcfe2fb9c532
Patch0:		%{name}-misc_fixes.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
Obsoletes:	ladspa-mcp-plugins-amsynth-examples < 0.2.2
Obsoletes:	ladspa-mcp-plugins-alsa-modular-synth-examples < 0.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This LADSPA plugin contains a digital implementation of the voltage
controlled lowpass filter (used in Moog synthesizers), chorus and
phaser effects.

%description -l pl.UTF-8
Ta wtyczka LADSPA zawiera cyfrową implementację sterowanego napięciem
filtra dolnoprzepustowego (używanego w syntezatorach Moog) oraz efekty
chorus i phaser.

%prep
%setup -q -n MCP-plugins-%{version}
%patch0 -p1

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDLAGS="%{rpmldflags}" \
%{__make} \
	CXX="%{__cxx}" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/cs_chorus.so
%attr(755,root,root) %{_libdir}/ladspa/cs_phaser.so
%attr(755,root,root) %{_libdir}/ladspa/mvchpf24.so
%attr(755,root,root) %{_libdir}/ladspa/mvclpf24.so
