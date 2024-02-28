# Determining the versions of things

The MEGA65 internal hardware has minor differences between the models shipped in the year 2022 and the models that will ship in 2024 and later. It is important to know which model you have.

The MEGA65 core (which includes the Hypervisor), ROM, and Freeze menu are all upgradable components. It is often useful to know which versions of these components are currently operating your machine.

## The MEGA65 Information screen

You can find out most of the information you need about the versions of various components using the MEGA65 Information screen.

![The MEGA65 Information screen](screenshots/megainfo.jpeg)

You can access the Information screen as follows:

1. Open the Freezer: hold <kbd>Restore</kbd> for one second, then release.
2. Press the <kbd>Help</kbd> key.

If pressing the <kbd>Help</kbd> key from the Freezer does nothing, you probably have the early 2022 model with the v0.9 firmware and system software. The Information screen was added in v0.95. (We will describe how to upgrade later in this Guide.)

Some important information on this screen:

* **MEGA65 Model**: the hardware model, such as `MEGA65 R6`
* **Artix Version**: the MEGA65 core version and date, such as `3C104883 2024-02-24`
* **ROM Version**: the version of the MEGA65 operating system (known as the "ROM" or "KERNAL"), such as `M65 V920395`

This Guide was originally written for the first MEGA65 model. I have left the instructions for finding this information in other ways below.

## The MEGA65 core version

Another way to determine which version of the MEGA65 core is installed is to turn off the computer, then hold the <kbd>Ctrl</kbd> key while turning on the computer to pause the Hypervisor screen.

![Hypervisor startup paused with Ctrl key](screenshots/hypervisor_paused.jpg)

The core version is represented by the "GIT commit" string. For example:

| MEGA65 shipment | Core version |
|-|-|
| Batch #1: early 2022 | `GIT commit: master,20220109.11,1586ad4` |
| Batch #2: late 2022 | `GIT commit: master,20221012.18,93d55f0` |
| Batch #3: mid 2024 | `GIT commit: master,20240224.00,3c10488` |

These `master` releases have been tested and declared stable for widespread use by the MEGA65 team. You can also download `development` releases (sometimes called "experimental" releases) to help test newer changes made to the core. Experimental releases have a version string that begins with the word `development`.

The `20240224` portion of the core version is a date, with a four-digit year, a two-digit month, and a two-digit day. The `3c10488` portion is a hash code that represents the most recent change in the code repository ("GIT commit"). Hash codes are not in any order, so you can't tell if one version is newer than the other by the hash code alone.

```{tip}
You can check the version of the MEGA65 core while the computer is running without turning it off. At any time with the MEGA65 core running, hold the <kbd>Mega</kbd> key (the fancy M in the lower left of your keyboard) and press <kbd>Tab</kbd>. Welcome to "Matrix mode!" This is a special mode used by the MEGA65 development team to tweak the memory of the computer while it is running, among other things. It also displays the version of the running MEGA65 core. Press <kbd>Mega</kbd> + <kbd>Tab</kbd> again to exit.
```

## The MEGA65 ROM version

You can determine the version of the MEGA65 ROM that is running from the BASIC title screen.

![ROM version from the BASIC screen, 920287](screenshots/basic_920287_number.jpg)

| MEGA65 shipment | ROM version |
|-|-|
| Batch #1: early 2022 | MEGA65 ROM v920287 |
| Batch #2: late 2022 | MEGA65 ROM v920377 |
| Batch #3: mid 2024 | MEGA65 ROM v920395 |

The original Commodore 65 ROM data used a number resembling a date to represent the software version, such as `910828` or `911001`. The MEGA65 enhanced versions of the original ROMs continues the numbering sequentially from `92xxxx`. A higher number implies a newer ROM.

## Bundled releases

To make it easy to know which versions of these components are known to work well together, the MEGA65 team provides release bundles that have been tested as a set. These releases have version numbers.

-   **Release bundle 0.9**, factory-installed for MEGA65s delivered early 2022 (batch #1)

    -   Core `master,20220109.11,1586ad4`
    -   ROM `920287`

-   **Release bundle 0.95**, factory-installed for MEGA65s delivered late 2022 and early 2023 (batch #2)
    -   Core `master,20221012.18,93d55f0`
    -   ROM `920377`

-   **Release bundle 0.96**, factory-installed for MEGA65s to be delivered mid 2024 (batch #3)
    -   Core `master,20240224.00,3c10488`
    -   ROM `920395`

The latest system software (`.M65` files on the SD card) is always bundled with the core.

In general, the core, ROM, and system software tend to serve independent functions, and most versions of one are compatible with most versions of the others. This is not always the case! I recommend upgrading release bundle components all at once. If you wish to try a newer beta test version of a component, be sure to follow beta test instructions to assure you are using compatible versions of other components.
