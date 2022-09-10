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
GIT commit: development,20220623.13,f555316
```

(Or just `f555316`.)

Alternatively, you can see the version of the MEGA65 core while the computer is running without turning it off. At any time with the MEGA65 core running, hold the <kbd>Mega</kbd> key (the fancy M in the lower left of your keyboard) and press <kbd>Tab</kbd>. Welcome to "Matrix mode!" This is a special mode used by the MEGA65 development team to tweak the memory of the computer while it is running, among other things. It also displays the version of the running MEGA65 core. Press <kbd>Mega</kbd> + <kbd>Tab</kbd> again to exit.

```{tip}
The `20220623` portion of the core version is a date, with a four-digit year, a two-digit month, and a two-digit day. The `f555316` portion is a hash code that represents the most recent change in the code repository ("GIT commit"). Hash codes are not in any order, so you can't tell if one version is newer than the other by the hash code alone.

Core updates are also assigned a sequential build version number, such as `198.0`. This doesn't appear on the MEGA65 itself, though it sometimes appears in filenames. You can find the full list of builds, build version IDs, and hash codes at [this Filehost page](https://files.mega65.org?id=13e1ce8a-ed5b-4046-aea6-491323697ead): click the grey "All versions" box to access all previous builds. (Versions later than 198.0 may appear on [this Filehost page](https://files.mega65.org?id=f461df65-4957-4d5b-9f6e-890dc63ee501) instead.)
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
920376
```

## "Stable" vs. "experimental" releases

Trenz Electronic shipped the first batch of 400 MEGA65 computers in May of 2022 with core version `20220109.11,1586ad4` and ROM version `920287` pre-installed. Prior to shipping, the MEGA65 team and contributors did a ton of work to validate the software so that batch #1 recipients would have a good experience. Despite best efforts, some bugs were not discovered until after the batch #1 shipment. Batch #1 owners can upgrade to newer firmware and system software with fixes and improvements.

The next batch of 400 computers (batch #2) will include the latest firmware and system software. The MEGA65 team and community will do another round of validation on the new release candidate just before batch #2 goes out. This will likely include everything up to core build v198 (`f555316`) and ROM `920376`, though this is still being finalized and may include additional fixes for bugs discovered during validation.

To make it clear which versions have gone through this validation process, the MEGA65 team makes a distinction between the latest _stable_ release and the latest _experimental_ release of the software.

**The latest stable release** is the version that shipped with batch #1: core `1586ad4` and ROM `920287`. It has known bugs that are fixed in later versions. When validation of the batch #2 release candidate is complete, that will become the new latest stable release, and all batch #1 owners will be encouraged to upgrade.

**The latest experimental release** contains all of the fixes and improvements that have been contributed to the project so far. It may have new bugs and backwards compatibility issues that need to be fixed. All MEGA65 owners are invited to install the latest version, help test it, and report issues. As of this writing, this is core `20220632.13,f555316` and ROM `920376`.

### Which one should you choose?

For batch #1 owners, I recommend installing the latest experimental release packages. There have been some issues with experimental releases this year, but they have mostly been resolved, and core `f555316` and ROM `920376` appear to be working well. They contain important fixes and quality-of-life upgrades for batch #1, and future third-party software will likely rely on them.

It is possible to install multiple cores and multiple ROMs, and switch between them when rebooting the machine. If you don't want to hassle with future issues with experimental releases, you can install the stable release as the default and the experimental release as an alternate. I might recommend this approach for batch #1 owners after the batch #2 release candidate has been declared stable. For now, I believe you'll have the best experience with the most recent experimental release.
