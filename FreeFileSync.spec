#
# spec file for package FreeFileSync
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2013, 2015 Gregor Mi
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# No   Date    Author           Changelog
# --   ----    ------           ---------
#  1   2013    codeminister     Copied from https://build.opensuse.org/package/show/home:hcooh/FreeFileSync
#  2   2013    codeminister     Modified since FreeFileSync v5.23 to work with openSUSE 12.3, 64 and 32 Bit, and later
#  3   2013    codeminister     Modified for FreeFileSync 5.23 on openSUSE 13.1
#  4   2015    codeminister     FreeFileSync 6.13 for openSUSE 13.2

# The 'Name' must match the openSUSE build service package name
# in order to get a properly filled download page
# (see for example https://build.opensuse.org/package/show/home:codeminister/FreeFileSync)
Name:           FreeFileSync
Summary:        Visual folder comparison and synchronization
Version:        6.13
Release:        1
License:        GPL-3.0+
Group:          Productivity/Networking/System
Url:            http://freefilesync.sourceforge.net/
Source0:        FreeFileSync_%{version}_Source.zip
# everything removed from zip except for zenxml folder:
Source1:        zenXml_2.1-stripped.zip
#Patch0:         0001-progress_indicator.cpp-fix-by-using-wxString-ctor.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  unzip
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  boost-devel >= 1.54
BuildRequires:  wxWidgets-3_0-devel
#PreReq:         %%fillup_prereq

%description
FreeFileSync is a free Open Source software that helps you synchronize files
and synchronize folders for Windows, Linux and Mac OS X. It is designed to save
your time setting up and running backup jobs while having nice visual feedback along the way.

%prep
# see http://www.rpm.org/max-rpm/s1-rpm-inside-macros.html
%setup -T -b 0 -c %{name}-%{version}      # unpack Source0 (-T -b 0) to given directory (-c)
%setup -T -a 1 -c %{name}-%{version} -D   # unpack Source1 (-T -a 1) to given directory (-c) but do not delete it (-D)
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires

# patches http://www.redhat.com/support/resources/howto/RH-sendmail-HOWTO/x192.html
# https://fedoraproject.org/wiki/How_to_create_an_RPM_package
# %%patch0 -p1

%build
cd FreeFileSync/Source

make %{?_smp_mflags} BUILD=FreeFileSync

%install
cd FreeFileSync/Source
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/FreeFileSync
%{_datadir}/FreeFileSync
%doc /usr/share/doc/FreeFileSync
%doc LICENSE

%changelog
