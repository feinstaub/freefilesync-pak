Source information
==================
* FreeFileSync_5.23_Source.zip
    is the original source downloaded from the sourceforge project
    at http://sourceforge.net/projects/freefilesync/files/freefilesync/v5.23/FreeFileSync_5.23_Source.zip/download (2013)

  * FreeFileSync homepage: http://sourceforge.net/projects/freefilesync/
  * FreeFileSync author: zenju

* freefilesync.png
  - copied from /usr/share/FreeFileSync/Resources.zip:/sync.png
  - to be copied to /usr/share/icons/hicolor/32x32/apps/freefilesync.png
  - used in freefilesync.desktop

* FreeFileSync.spec
    was found at https://build.opensuse.org/package/show/home:hcooh/FreeFileSync on October 2013
    and will be continously adapted

* 0001-progress_indicator.cpp-fix-by-using-wxString-ctor.patch
    changes to the source to make it compile under openSUSE
    TODO: find out reason source does compile without these changes or ask author to fix upstream

* freefilesync.desktop
    Created for use in /usr/share/applications/ (start menu entry)


Build service info
==================
* URL: https://build.opensuse.org/package/show/home:codeminister/FreeFileSync


TODO
====
* add desktop file to integrate FreeFileSync e. g. with the KDE Kickoff Application Launcher
  * [ok] files present
  * create install script for .desktop file and icon and use in spec file

* FreeFileSync 6.0 needs wxWidgets 2.9.5 which is not provided by openSUSE 13.1 (wxWidgets 2.9)
  see http://docs.wxwidgets.org/trunk/classwx_grid.html#a3f0bb553b28e7f00185c6c56d3c1262e (wxGrid::SetTabBehaviour)
  

Misc infos
==========
* Review installation procedure and how settings are stored
  * settings stored in ~/.FreeFileSync


Build information
=================
home:codeminister/FreeFileSync> osc buildhist
Valid arguments for this package are:

openSUSE_Factory  i586
openSUSE_Factory  x86_64
openSUSE_13.1     i586
openSUSE_13.1     x86_64
openSUSE_12.3     i586
openSUSE_12.3     x86_64
openSUSE_12.2     i586
openSUSE_12.2     x86_64
Missing arguments

Build specific platform
-----------------------
osc build openSUSE_13.1 x86_64
osc build openSUSE_13.1 i586
