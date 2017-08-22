%global libname vterm

%global revision 681

Name:           lib%{libname}
Version:        0
Release:        0.4.bzr%{revision}%{?dist}
Summary:        An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator

License:        MIT
URL:            https://launchpad.net/libvterm
# Upstream D/L link seems to be dead (as of 22.08.2017)
#
# Steps to recreate tarball from bazaar:
# bzr branch lp:libvterm
# cd libvterm
# bzr export -r 681 --root ~leonerd/libvterm/trunk ../libvterm-%{revision}.tgz
Source0:        http://bazaar.launchpad.net/~leonerd/libvterm/trunk/tarball/%{revision}/%{name}-%{revision}.tgz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool

%description
An abstract C99 library which implements a VT220 or xterm-like
terminal emulator. It does not use any particular graphics toolkit or
output system. Instead, it invokes callback function pointers that
its embedding program should provide it to draw on its behalf.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
%{summary}.

%prep
%autosetup -n ~leonerd/libvterm/trunk

%build
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
make test CFLAGS="%{optflags}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}.h
%{_includedir}/%{libname}_*.h
%{_libdir}/pkgconfig/%{libname}.pc

%files tools
%{_bindir}/unterm
%{_bindir}/%{libname}-ctrl
%{_bindir}/%{libname}-dump

%changelog
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.bzr681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.bzr681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.bzr681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1.bzr681
- Initial package
