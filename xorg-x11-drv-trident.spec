%define tarball xf86-video-trident
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:    Xorg X11 trident video driver
Name:       xorg-x11-drv-trident
Version:    1.3.3
Release:    1.1%{?dist}
URL:        http://www.x.org
License:    MIT
Group:      User Interface/X Hardware Support
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:    ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:    trident.xinf

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6

%description 
X.Org X11 trident video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/trident_drv.so
%{_datadir}/hwdata/videoaliases/trident.xinf
%{_mandir}/man4/trident.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3.3-1.1
- Rebuilt for RHEL 6

* Wed Aug 05 2009 Dave Airlie <airlied@redhat.com> 1.3.3-1
- trident 1.3.3

* Tue Aug 04 2009 Adam Jackson <ajax@redhat.com> 1.3.2-3
- trident-1.3.2-dpms.patch: Fix for new DPMS headers

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.3.2-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 1.3.2-1
- trident 1.3.2

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 1.3.1-1
- new upstream release

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 1.3.0-2
- new server API

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 1.3.0-1
- Latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.3-8
- Autorebuild for GCC 4.3

* Mon Feb 18 2008 Dave Airlie <airlied@redhat.com> - 1.2.3-7
- pciaccess support (#433254)

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 1.2.3-6
- Rebuild for ppc toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.2.3-5
- Update Requires and BuildRequires.  Add Requires: hwdata.

* Mon Feb 26 2007 Adam Jackson <ajax@redhat.com> 1.2.3-4
- Don't compile a dead file

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.2.3-3
- ExclusiveArch -> ExcludeArch

* Mon Jan 29 2007 Adam Jackson <ajax@redhat.com> 1.2.3-2
- Rebuild for 6 to 7 upgrade path

* Wed Jan 24 2007 Adam Jackson <ajax@redhat.com> 1.2.3-1
- Update to 1.2.3

* Tue Jul 25 2006 Mike A. Harris <mharris@redhat.com> 1.2.1-3.fc6
- Added trident-missing-symbols-bug168713.patch to fix bug (#168713)
- Remove moduledir/driverdir directory ownership (#198294)
- Added {?dist} tag to Release field.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.2.1-2.1
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.2.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr 09 2006 Adam Jackson <ajackson@redhat.com> 1.2.1-1
- Update to 1.2.1 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.1.2-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.1.2-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1.2-1
- Updated xorg-x11-drv-trident to version 1.0.1.2 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.1.1-1
- Updated xorg-x11-drv-trident to version 1.0.1.1 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.2-1
- Updated xorg-x11-drv-trident to version 1.0.0.2 from X11R7 RC2

* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-trident to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 04 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64, ppc

* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for trident video driver generated automatically
  by my xorg-driverspecgen script.
