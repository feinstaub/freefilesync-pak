#
# spec file for package FreeFileSync
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# Date    Author           Changelog
# ----    ------           ---------
# 2013    codeminister     Copied from https://build.opensuse.org/package/show/home:hcooh/FreeFileSync
# 2013    codeminister     Modified since FreeFileSync v5.23 to work with openSUSE 12.3, 64 and 32 Bit, and later
# 2013    codeminister     Modified for FreeFileSync 5.23 on openSUSE 13.1
#


# This Name must match the openSUSE build service package name
# (see for example https://build.opensuse.org/package/show/home:codeminister/FreeFileSync)
# in order to a properly filled download page
Name:           FreeFileSync
Summary:        Visual folder comparison and synchronization
Version:        5.23
Release:        3
License:        GPL-3.0+
Group:          Productivity/Networking/System
Url:            http://freefilesync.sourceforge.net/
Source0:        FreeFileSync_%{version}_Source.zip
#Source1:        ChangeLog
Patch0:         0001-progress_indicator.cpp-fix-by-using-wxString-ctor.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  unzip
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  boost-devel >= 1.53
BuildRequires:  wxWidgets-2_9-devel
#BuildRequires:  wxWidgets-devel
#BuildRequires:  wxWidgets-wxcontainer-devel
#BuildRequires:  wxWidgets-2_9-wxcontainer-devel
#PreReq:         %fillup_prereq

%description
FreeFileSync is a folder comparison and synchronization tool
providing highly optimized performance and usability without
needless user interface complexity.

%prep
%setup -q -c %{name}-%{version}
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires

# patches http://www.redhat.com/support/resources/howto/RH-sendmail-HOWTO/x192.html
# https://fedoraproject.org/wiki/How_to_create_an_RPM_package
%patch0 -p1

####???
####%{__cp} %{S:1} .

%build
# since v5.23
cd FreeFileSync/Source

make %{?_smp_mflags} BUILD=Launchpad

%install
# since v5.23
cd FreeFileSync/Source
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/FreeFileSync
%{_datadir}/FreeFileSync
%doc /usr/share/doc/FreeFileSync
#%doc /usr/share/doc/FreeFileSync/changelog.gz
%doc LICENSE

%changelog

