# Determining the versions of things

The MEGA65 core (which includes the Hypervisor), ROM, and Freeze menu are all upgradable components. It is often useful to know which versions of these components are currently operating your machine.

## The MEGA65 core version

One way to determine which version of the MEGA65 core is installed is to turn off the computer, then hold the <kbd>Ctrl</kbd> key while turning on the computer to pause the Hypervisor screen.

![Hypervisor startup paused with Ctrl key](screenshots/hypervisor_paused.jpg)

The MEGA65 factory core shipped with batch #1 in 2022 has this version number:

```
GIT commit: master,20220109.11,1586ad4
```

(Or just `1586ad4`.) As of this writing, the latest available version of the MEGA65 core is:

```
GIT commit: development,20220625.19,80fc1c0
```

(Or just `80fc1c0`.)

Alternatively, you can see the version of the MEGA65 core while the computer is running without turning it off. At any time with the MEGA65 core running, hold the <kbd>Mega</kbd> key (the fancy M in the lower left of your keyboard) and press <kbd>Tab</kbd>. Welcome to "Matrix mode!" This is a special mode used by the MEGA65 development team to tweak the memory of the computer while it is running, among other things. It also displays the version of the running MEGA65 core. Press <kbd>Mega</kbd> + <kbd>Tab</kbd> again to exit.

```{tip}
The file downloads for core updates on Filehost are labeled with both the GIT commit suffix (like `f555316`) and a build version number (`build 198`, or `version 198.0`). You can find the full list of builds at [the Filehost page](https://files.mega65.org?id=13e1ce8a-ed5b-4046-aea6-491323697ead): click the grey "All versions" box to access all previous builds.

The build version number does not appear on the Hypervisor start-up screen or Matrix mode. You can use the "All versions" list on Filehost to match GIT commit suffixes to build numbers.
```

## The MEGA65 ROM version

You can determine the version of the MEGA65 ROM that is running from the BASIC title screen.

![ROM version from the BASIC screen, 920287](screenshots/basic_920287_number.jpg)

The original Commodore 65 ROM data used a number resembling a date to represent the software version, such as `910828` or `911001`. The MEGA65 enhanced versions of the original ROMs continues the numbering sequentially from `92xxxx`.

The MEGA65 ROM that shipped with batch #1 in 2022 has this version number:

```
920287
```

As of this writing, the latest stable version of the MEGA65 ROM is:

```
920371
```

The MEGA65 team has an "experimental" branch of ROM development with new features that might break compatibility with existing software. Experimental versions use a version number prefix of `99xxxx`.

## Utility version numbers

Some parts of the operating system, such as the Hypervisor and Freeze functions, have their own version numbers displayed on their respective screens. You do not typically need these, but they can be useful when installing experimental versions of the utility files (e.g. `FREEZER.M65`) independently of a full core upgrade.

To see the Hypervisor screen, hold <kbd>Ctrl</kbd> while turning on the computer. As of core `bdeeb15`, the Hypervisor version is v00.16. The Hypervisor is built into the core.

To see the Freeze screen, simply open the menu: hole <kbd>Restore</kbd> for a second, then release. As of core `80fc1c0`, the Freeze menu version is v0.1.6. It is possible to upgrade the Freeze menu separately from the core with a file on the SD card.

```{note}
Theese version numbers are not always updated consistently. For example, a fix to the issue with the Freeze menu appearing too low on the screen was released in a newer version, but the Freeze menu version number was not incremented. When we upgrade later in this Guide, the Freeze menu version number will not change.

In typical use, you will upgrade the core and utility files together, and will only need the core version number or build number when reporting issues.
```
