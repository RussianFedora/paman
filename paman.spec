Name:           paman
Version:        0.9.4
Release:        7%{?dist}.R
Summary:        Management tool for PulseAudio

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://0pointer.de/lennart/projects/paman
Source0:        http://0pointer.de/lennart/projects/paman/paman-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pulseaudio-lib-devel gtkmm24-devel libglademm24-devel lynx
BuildRequires:  desktop-file-utils

%description
PulseAudio Manager (paman) is a simple GTK frontend for the PulseAudio sound
server. With paman you may browser most of PulseAudio's internals. There is
support for changing volume of sinks and sink outputs. You're able to play
samples from the sample cache. 

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --add-category="X-Fedora" --vendor="" \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE doc/README
%{_bindir}/paman
%dir %{_datadir}/paman
%{_datadir}/paman/paman.glade
%{_datadir}/applications/paman.desktop


%changelog
* Thu Feb  2 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.9.4-7.R
- rebuilt for EL

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.4-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.4-2
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> 0.9.4-1
- Update to 0.9.4
- Adjust License tag

* Thu Aug 16 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.4-0.1.svn20070816
- Update from SVN snapshot

* Sat Sep  9 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.3-2
- Add BuildRequires for desktop-file-utils.

* Fri Sep  8 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.3-1
- Update to 0.9.3
- Fix installation of desktop file.

* Sun Jul  9 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.2-1
- Update to 0.9.2

* Thu Jun  8 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.1-1
- Update to 0.9.1

* Mon May 29 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.0-1
- Initial package for Fedora Extras
