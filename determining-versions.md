# Determining the versions of things

The MEGA65 core (which includes the Hypervisor), ROM, and Freeze menu are all upgradable components. It is often useful to know which versions of these components are currently operating your machine.

## The MEGA65 core version

One way to determine which version of the MEGA65 core is installed is to turn off the computer, then hold the <kbd>Ctrl</kbd> key while turning on the computer to pause the Hypervisor screen.

![Hypervisor startup paused with Ctrl key](screenshots/hypervisor_paused.jpg)

MEGA65 computers delivered in early 2022 ("batch #1") have this version of the MEGA65 core:

```
GIT commit: master,20220109.11,1586ad4
```

MEGA65 computers delivered in late 2022 ("batch #2") will ship with this newer version of the MEGA65 core:

```
GIT commit: master,20221012.18,93d55f0
```

If you have a batch #1 MEGA65, I recommend upgrading to the newer `93d55f0` core. We'll describe how to do this later in this Guide.

These two `master` releases have been tested and declared stable for widespread use by the MEGA65 team. You can also download `development` releases (sometimes called "experimental" releases) to help test newer changes made to the core. Experimental releases have a version string that begins with the word `development`.

The `20221012` portion of the core version is a date, with a four-digit year, a two-digit month, and a two-digit day. The `93d55f0` portion is a hash code that represents the most recent change in the code repository ("GIT commit"). Hash codes are not in any order, so you can't tell if one version is newer than the other by the hash code alone.

```{tip}
You can check the version of the MEGA65 core while the computer is running without turning it off. At any time with the MEGA65 core running, hold the <kbd>Mega</kbd> key (the fancy M in the lower left of your keyboard) and press <kbd>Tab</kbd>. Welcome to "Matrix mode!" This is a special mode used by the MEGA65 development team to tweak the memory of the computer while it is running, among other things. It also displays the version of the running MEGA65 core. Press <kbd>Mega</kbd> + <kbd>Tab</kbd> again to exit.
```

## The MEGA65 ROM version

You can determine the version of the MEGA65 ROM that is running from the BASIC title screen.

![ROM version from the BASIC screen, 920287](screenshots/basic_920287_number.jpg)

The MEGA65 ROM that shipped with batch #1 in early 2022 has this version number:

```
920287
```

Late 2022 batch #2 computers will ship with this version of the MEGA65 ROM:

```
920377
```

I recommend that all owners of a batch #1 MEGA65 upgrade to ROM 920377. We'll describe how to do this later in this Guide.

The original Commodore 65 ROM data used a number resembling a date to represent the software version, such as `910828` or `911001`. The MEGA65 enhanced versions of the original ROMs continues the numbering sequentially from `92xxxx`. A higher number implies a newer ROM.

You may also see MEGA65 ROMs with a version number that begins with `99`. These are "experimental" releases, similar to the experimental cores, and are used for testing new features.

## Bundled releases

To make it easy to know which versions of these components are known to work well together, the MEGA65 team provides release bundles that have been tested as a set. These releases have version numbers.

-   **Release bundle 0.9**, factory-installed for MEGA65s delivered early 2022 (batch #1)

    -   Core `master,20220109.11,1586ad4`
    -   ROM `920287`

-   **Release bundle 0.95**, factory-installed for MEGA65s to be delivered late 2022 and early 2023 (batch #2)
    -   Core `master,20221012.18,93d55f0`
    -   ROM `920377`

The system software (`.M65` files on the SD card) does not have its own version number. The latest system software is always bundled with the core.

Experimental versions are not included in release bundles. If you want to try an experimental version of a component, you'll be replacing the component individually.

In general, the core, ROM, and system software tend to serve independent functions, and most versions of one are compatible with most versions of the others. This has not always been the case! I recommend upgrading all components from release 0.9 to 0.95 together, as described in this Guide.
