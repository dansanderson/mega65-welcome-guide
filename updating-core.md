# Updating the core firmware

A new version of the MEGA65 core has been released since the batch #1 MEGA65 was produced, so you will want to update it. The newest ROM expects the new core.

## Downloading the latest MEGA65 core

You can download the latest MEGA65 core from Filehost. For the batch #1 MEGA65 hardware, you want the [MEGA65 R3 Core - COR file](https://files.mega65.org?id=13e1ce8a-ed5b-4046-aea6-491323697ead).

Other "core" related files on Filehost are used for different purposes. You probably don't need them. "MEGA65 R2" is a previous version of the mainboard. "Nexys 4" and "Nexys 4 DDR" are FPGA development boards that can be configured to run like a MEGA65. The "MCS" and "BIT" files are different ways to update the core; you use COR files with the recommended update procedure.

```{caution}
A new core version is uploaded to Filehost every time someone changes the source code. Occasionally, a change may introduce a bug. If you're having difficulty with the latest core, [go to the Filehost page](https://files.mega65.org?id=13e1ce8a-ed5b-4046-aea6-491323697ead) and click "All versions" to access previous versions.

As of this writing, build 182 (Filehost version 182, May 28, 2022, `98dd39d`) is known to be working and compatible with the latest ROM. Build 183 introduced a bug related to disk mounting that is still being investigated.
```

## Installing the latest MEGA65 core

Download "[mega65r3-dev.cor](https://files.mega65.org?id=13e1ce8a-ed5b-4046-aea6-491323697ead)" from Filehost. Copy this file to the microSD card.

Eject the microSD card from your PC and insert it into the MEGA65 external slot. Make sure the MEGA65 is off, then hold the No Scroll key (in the top row) and turn it on. This opens the core selection and installation menu.

![The core menu, factory configuration](screenshots/cor_menu_empty.jpg)

Core 0 is always the factory-installed core and cannot be overwritten. This can help you restore your MEGA65 to a working state if something goes wrong with updating a core. If this is your first time seeing the core selection menu, slots 1 through 7 should be empty.

When you turn on your MEGA65 normally, it checks to see if slot 1 contains a core, and uses it if present. Otherwise it falls back to core 0. You will put the updated core in slot 1 for regular use.

Hold the Ctrl key and press 1. Use the cursor keys to find the `mega65-1.cor` filename (a shortened version of the full filename). If there is a second one with a stripey thing next to it, select the one _without_ the stripey thing. Press Return, then press any key when prompted to install the core.

![The core file selection screen](screenshots/cor_selection.jpg)

The flashing process takes a minute or so. When it is complete, you'll see the message, "Flash slot successfully updated," and the border will twinkle. Press any key to return to the core selection menu. Finally, press 1 (without Ctrl) to start the system with the new core.

![The core verification screen](screenshots/cor_verified.jpg)
![Loading a core](screenshots/cor_loading.jpg)
![Core loading finished](screenshots/cor_finished.jpg)
![The core menu after loading a new core](screenshots/cor_menu_onecore.jpg)

```{note}
If you use a Mac computer to copy a file to a MEGA65 SD card, it creates another file with a name like `._filename` to store the macOS resource fork. The appears in the core file selection screen as the original name with a stripey thing next to it. Be sure to select the original core file, and not the one with the stripey thing, when installing a core.

If you select the wrong one, MEGA65 will warn that the incorrect file does not have a matching device ID (because it isn't a real core file). Press RUN/STOP to abort and try again with the correct file.
```

```{tip}
For more on installing cores, see the User's Guide, chapter 6, starting page 47.
```

## Symptoms that you're using the wrong MEGA65 core

If you've been following along with this Guide, you should now have a MEGA65 that uses the latest core and ROM when you turn it on. You can confirm the core and ROM versions as described in {ref}`determining-versions:determining the versions of things`.

Some actions, such as accessing the Configuration or SD card utility from the Alt menu, cause the MEGA65 to boot into its factory core (slot 0) instead of the updated core in slot 1. This can cause issues with the older core to reappear, or for the newer ROM to interact poorly with the older core.

The community has noticed a few common symptoms caused by older versions of the ROM, the core, or a version mismatch:

-   _The Freeze menu appears too low on the screen, obscuring the bottom._
    -   You have an older ROM, or an older version of `FREEZER.M65`.
-   _The Freeze menu does not display the name of the selected D81 file next to the drive, and the disk does not mount properly._
    -   You are using the newer ROM with the older core.
-   _Disk directory misbehavior, such as an extra file, or missing files._
    -   You are using the newer ROM with the older core.

Use "Matrix mode" (hold Mega, hit Tab) to double check that MEGA65 is using the latest core. If it is using the factory core (`1586ad4`) and you have the latest core installed in slot 1, turn off your MEGA65, then turn it back on.

## The C64 core

We mentioned that the MEGA65 can run other cores besides the one that causes your Mega to act like a Commodore 65. One such core is a Commodore 64.

The C64 core is _not the same_ as the C65's Commodore 64 mode, the one you start by typing `GO 64` (see {ref}`try-this-first:commodore 64 mode`). The C64 core completely transforms your Mega into a Commodore 64, with no C65 or MEGA65 features.

The initial version of the C64 core is available for you to try, and it's worth installing just to see how cores work. The C64 core strives to be more compatible with C64 software than the C65's Commodore 64 mode. The initial version supports PAL displays, a simulated C1541 drive that supports D64 image files, and joysticks.

If you'd like to try it, go to Filehost, then locate and download "[C64 for MEGA65](https://files.mega65.org?id=896a012f-59e4-456c-b91f-7e989b958241)". Install it like you did the MEGA65 core update, using slot 2.

The C64 core can read D64 image files off of the SD card. While the C64 core is running, press the Help key to open the menu. Press Return on the first line to browse the SD card, then select a disk image to mount to device 8. Press Help again to close the menu. The disk image you selected is now mounted, and you can execute C64 disk commands as usual (such as `LOAD "*",8,1`).

![C64 core with Help menu open](screenshots/c64core_menu.jpeg)

```{tip}
To avoid cluttering your SD card with D64 images, you can use your PC to create a folder named `c64` and put the D64 files in there. The C64 core will notice the folder and limit its browser to just these files.
```

See the [Commodore 64 for MEGA65 manual](https://github.com/MJoergen/C64MEGA65/blob/V1/README.md) for more information.

To return to the MEGA65 core in slot 1, turn off the machine, then turn it on again.

```{tip}
For information on other cores that work with the MEGA65, see [What are "alternative" MEGA65 cores?](https://sy2002.github.io/m65cores/). You can use alternate cores to convert your MEGA65 into a [ZX Spectrum](https://files.mega65.org?id=bdaeb7e0-9fc8-4185-99de-104d01229f27) or a [Game Boy Color](https://files.mega65.org/html/main.php?id=03b68172-d6ff-49f0-971e-15bea2c6ad9a)!
```
