Latest info
===========
The build recipies were merged to here:

https://build.opensuse.org/package/show/network/FreeFileSync

So there you find the latest maintained build of FreeFileSync.


Source information
==================
* FreeFileSync_6.13_Source.zip
    is the original source downloaded from the sourceforge project
    at http://sourceforge.net/projects/freefilesync/files/freefilesync/v{VERSION}/FreeFileSync_{VERSION}_Source.zip/download (2015)

  * FreeFileSync homepage: http://sourceforge.net/projects/freefilesync/
  * FreeFileSync author: zenju

* freefilesync.png
  - copied from /usr/share/FreeFileSync/Resources.zip:/sync.png
  - to be copied to /usr/share/icons/hicolor/32x32/apps/freefilesync.png
  - used in freefilesync.desktop

* freefilesync.desktop
    Created for use in /usr/share/applications/ (start menu entry)


Build service info
==================
* URL: https://build.opensuse.org/package/show/home:codeminister/FreeFileSync

osc usage:
```
# local build
osc build openSUSE_13.2 x86_64
# intermediate results see: /var/tmp/build-root/openSUSE_13.2-x86_64/home/abuild/rpmbuild/

# one-time checkout of empty project (does not exist anymore)
osc co home:codeminister/freefilesync-6.13 -o .

# add all files
osc add *

# commit to server
osc commit
```

for current time in freefilesync.changes
`date --utc`


TODO
====
* add desktop file to integrate FreeFileSync e. g. with the KDE Kickoff Application Launcher
  * [ok] files present
  * create install script for .desktop file and icon and use in spec file


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
