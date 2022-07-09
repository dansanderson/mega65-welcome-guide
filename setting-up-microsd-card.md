# Setting up the microSD card

Your microSD card will be your MEGA65's primary storage, and the primary way to transfer files to and from your PC. You will use it to update the firmware and store updated system software and ROMs. You will also use it to manage D81 disk images and store applications you have downloaded.

## Preparing the microSD memory card

To use an SD card with the MEGA65, it must be formatted (erased and prepared) using the MEGA65. The SD card works like a regular storage drive when connected to your PC, but it contains additional data not visible to the PC that is used by MEGA65.

To prepare a new microSD card for use, insert it into your MEGA65's external microSD card slot. Turn off your MEGA65, then hold the <kbd>Alt</kbd> key (top row near the left) and turn it on. Select option 2: SDCard FDisk+Format Utility (press <kbd>2</kbd>).

![Hypervisor utility menu, holding Alt during boot](screenshots/hypervisor_altmenu.jpg)

The SD card utility will look for cards in the available slots. Confirm that it has detected your microSD card correctly, then select option 1 for the external microSD slot (press <kbd>1</kbd>). Follow the prompts.

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

Visit [the Filehost website](https://files.mega65.org/html/main.php) and make sure you are signed in. Select "Files," then filter the Category column for the Firmware category. Locate the item named "[MEGA65 SD card essentials - No ROM](https://files.mega65.org?id=0fb941fe-5c5f-4608-b0f1-32849d4a8dff)," click it to open the item, then click Download.

This file is in the [RAR archive format](<https://en.wikipedia.org/wiki/RAR_(file_format)>). You will need software on your PC to unpack this archive. I recommend [The Unarchiver](https://theunarchiver.com/), which has a graphical app for macOS and a command-line tool for Mac, Windows, and Linux. Windows users might prefer [7-Zip](https://www.7-zip.org/). Unpack the RAR archive to a folder of files.

Remove the microSD card from MEGA65, then insert it in your PC's card reader. Copy the unpacked files to the microSD card (in the root level, not in a sub-folder), replacing all files that have the same names.

### Preventing "fragmented" files

The SD card uses a modern file system that stores each file as one or more _blocks_ on the card. In some cases, a file's blocks may not be stored contiguously: pieces of a single file may be stored in different places on the card. The MEGA65 Hypervisor does not have complete support for files stored this way, and may fail to find a system file or D81 disk image if the file is stored discontinuously, or _fragmented_.

One method to avoid fragmenting the system files when copying them to an SD card is to _not_ simply copy the new files over the existing files. Instead, rename each of the old files on the card (e.g. rename `FREEZER.M65` to `OLD_FREEZER.M65`), copy the new file (e.g. `FREEZER.M65` from the archive) onto the card, then delete the old file. This discourages your PC from attempting to reuse the space occupied by the old file for the new file, noticing that the new file is larger than the old file, and allocating discontinuous blocks for the additional data. If you notice problems after upgrading SD card system files, try reinstalling the files onto the card using this technique.

To make this easier, I wrote [a Python script](https://github.com/dansanderson/mega65-welcome-guide/blob/main/update-sd-card.py) that updates an SD card using this technique for all files to avoid fragmentation. Feel free to use it or adapt it for other purposes.

[This article](https://files.mega65.org?ar=73fd7977-aad3-4e13-8b5a-e9f0548b6cb2) recommends using defragmentation tools on the SD card. I have not tested these.

## Updating the ROM

As indicated by the phrase "No ROM" in the title, the SD card essentials "No ROM" archive does not include the MEGA65 ROM file. If you have registered your owner ID with your Filehost account, you can get the latest ROM as a separate download.

Still in the Filehost Firmware category, locate and download "[C65/MEGA65 Kernal ROM](https://files.mega65.org?id=54e69439-f25e-4124-8c78-22ea7ddc0f1c)." Notice the funny filename, something like `920371.BIN`. The number in the filename is the version number for this ROM.

Rename the ROM file to `MEGA65.ROM`. Copy it to the microSD card, replacing the file that is already there.

```{note}
If you're using a Mac, the Finder can sometimes be defensive about changing the filename extension when renaming a file. Click on the desktop, then open the Finder menu, Preferences... Under the Advanced tab, make sure "Show all filename extensions" is checked. Without this, it is possible to accidentally rename `920349.BIN` to `MEGA65.ROM.BIN` and not notice. The correct name is `MEGA65.ROM`.
```

```{tip}
You can keep multiple versions of the MEGA65 ROM on your SD card and switch between them. By default, MEGA65 will boot using `MEGA65.ROM`. If you have alternate ROMs on the SD card named `MEGA65<#>.ROM` where `<#>` is a single digit number (for example, `MEGA651.ROM`), you can hold down the corresponding number key (for example, `1`) during start-up to select the alternate ROM.
```

## Optional: reinstalling bundled software

The SD card formatting process does not fully recreate the SD card that was bundled with the computer. You can re-add the bundled software from the backup you made in the previous section, if desired.

See {ref}`try-this-first:other bundled software` for a list of bundled D81 disk images that you might want to install. The new card is also missing `HEAVY.MOD`, one of the two bundled MOD music files that work with the MOD player on the demo disk. (`POPCORN.MOD` does get installed automatically on a fresh card. Nice!)

```{tip}
If you erased your factory-installed SD card without backing up its contents, you can find the original [MEGA65 Release SD Card - Intro Disk #1](https://files.mega65.org?id=f588fd55-f2b8-4ca0-b5f4-9ae5b1c2e914) on Filehost. You must be a registered owner to see this file, because it contains licensed software including the ROM and GEOS. Note that the system files on this SD card image are the factory-installed versions, not the new ones we just upgraded.
```
