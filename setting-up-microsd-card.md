# Setting up the microSD card

Your microSD card will be your MEGA65's primary storage, and the primary way to transfer files to and from your PC. You will use it to update the firmware and store updated system software and ROMs. You will also use it to manage D81 disk images and store applications you have downloaded.

## Preparing the microSD memory card

To use an SD card with the MEGA65, it must be formatted (erased and prepared) using the MEGA65. The SD card works like a regular storage drive when connected to your PC, but it contains additional data not visible to the PC that is used by MEGA65.

To prepare a new microSD card for use, insert it into your MEGA65's external microSD card slot. Turn off your MEGA65, then hold the Alt key (top row near the left) and turn it on. Select option 2: SDCard FDisk+Format Utility (press 2).

![Hypervisor utility menu, holding Alt during boot](screenshots/hypervisor_altmenu.jpg)

The SD card utility will look for cards in the available slots. Confirm that it has detected your microSD card correctly, then select option 1 for the external microSD slot (press 1). Follow the prompts.

![SD card utility](screenshots/sdcard_util.jpg)

The MEGA65 formats the SD card, erasing all of its data. It also writes the factory-installed ROM files, the demo disk image, and a few other things.

```{caution}
The SD card utility will erase the internal SD card if you ask it to. Be careful to select the correct card.
```

```{tip}
For more on preparing SD cards for use, see the User's Manual, starting page 23.
```

## Updating the SD card essentials

MEGA65 prepares the SD card with files from the factory-installed core. You will want to update these files with newer versions.

Visit [the Filehost website](https://files.mega65.org/html/main.php) and make sure you are signed in. Select "Files," then filter the Category column for the Firmware category. Locate the item named "[MEGA65 SD card essentials](https://files.mega65.org?id=a809e0ae-30ac-42f5-ab9c-766d72fd6331)," click it to open the item, then click Download.

```{note}
There is also a "MEGA65 SD card essentials - No ROM" file. This is the same archive, but with the licensed ROM files removed.
```

This file is in the [RAR archive format](<https://en.wikipedia.org/wiki/RAR_(file_format)>). You will need software on your PC to unpack this archive. I recommend [The Unarchiver](https://theunarchiver.com/), which has a graphical app for macOS and a command-line tool for Mac, Windows, and Linux. Windows users might prefer [7-Zip](https://www.7-zip.org/). Unpack the RAR archive to a folder of files.

Remove the microSD card from MEGA65, then insert it in your PC's card reader. Copy the unpacked files to the microSD card (in the root level, not in a sub-folder), replacing all files that have the same names.

## Updating the ROM

The SD card essentials archive includes MEGA65 ROM files, but these might be out of date. Just to be sure, let's grab the absolute latest ROM from Filehost.

Still in the Filehost Firmware category, locate and download "[C65/MEGA65 Kernal ROM](https://files.mega65.org?id=54e69439-f25e-4124-8c78-22ea7ddc0f1c)." Notice the funny filename, something like `920350.BIN`. The number in the filename is the ROM version number for this ROM. (Yours may be newer than the example in this guide. It gets updated frequently.)

Rename the ROM file to `MEGA65.ROM`. Copy it to the microSD card, replacing the file that is already there.

```{note}
If you're using a Mac, the Finder can sometimes be defensive about changing the filename extension when renaming a file. Click on the desktop, then open the Finder menu, Preferences... Under the Advanced tab, make sure "Show all filename extensions" is checked. Without this, it is possible to accidentally rename `920349.BIN` to `MEGA65.ROM.BIN` and not notice. The correct name is `MEGA65.ROM`.
```

## Optional: reinstalling bundled software

The SD card formatting process does not fully recreate the SD card that was bundled with the computer. You can re-add the bundled software from the backup you made in the previous section, if desired.

See {ref}`try-this-first:other bundled software` for a list of bundled D81 disk images that you might want to install. The new card is also missing `HEAVY.MOD`, one of the two bundled MOD music files that work with the MOD player on the demo disk. (`POPCORN.MOD` does get installed automatically on a fresh card. Nice!)
