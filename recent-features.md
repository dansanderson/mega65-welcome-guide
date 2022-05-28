# Recently added features

The MEGA65 batch #1 shipped from the factory with ROM version 920287, and a User's Guide printed in late 2021. The MEGA65 team has been enhancing the ROM with new features and improvements. As of 2022, the ROM is still considered a work in progress, and MEGA65 owners are encouraged to update to the latest ROM.

Below is an _incomplete_ list of new features that have been added since the factory ROM, or may exist in the factory ROM but were not included in the User's Guide. I can't possibly keep this list up to date, but I wanted to describe a few so you know what you're getting with the updates. I'm leaving out the many bug fixes that have also been included in new ROMs.

```{tip}
MEGA65 documentation writers are keeping the [downloadable PDF version of the User's Guide](https://files.mega65.org/manuals-upload/mega65-userguide.pdf) up to date with new features. Be sure to download this periodically along with ROM updates.
```

## New features

Some of the new features that have been added since the factory-installed ROM was delivered in batch #1 include:

- Holding RUN/STOP during boot immediately enters the machine language `MONITOR`.
- Filename pattern matching supports `#` to match a single number character, and `$` to match a single letter character: `DIR "ME$$*"`
- To toggle between 40-column mode and 80-column mode, press ESC then press X. To go directly to 40-column mode, use ESC then 4. To go directly to 80-column mode, use ESC then 8.
- BASIC supports arithmetic shift operators: `<<` and `>>`. `PRINT 7<<3`
- Single-letter BASIC variables are "fast" variables stored in fixed memory addresses `$FD00-$FEFF`.
- The `PLAY` and `SOUND` commands have improved background playback and use of SID voices, so BASIC games can sensibly have both background music and sound effects.
- Some disk commands can access files on the SD card directly (and not via a mounted D81 disk image) using the virtual device `U12`. `DIR U12` lists the files on the SD card. `DLOAD "FILE.PRG",U12` loads a `PRG` file.

## New BASIC commands

Many new BASIC commands have been added to the factory-installed ROM, or have been added to the User's Guide since it was printed. See [the latest User's Guide](https://files.mega65.org/manuals-upload/mega65-userguide.pdf) for specifics. New commands include:

### Newer disk commands

`MOUNT` controls the mounting of disk images and drives to the unit numbers from BASIC, without having to enter the Freezer.

- To mount a D81 disk image from the SD card to unit 8: `MOUNT "FILENAME.D81"`
- To mount the built-in physical 3-1/2" disk drive: `MOUNT`

`FORMAT` formats (erases) a mounted disk. This is an alias for `HEADER`.

- To prepare a new disk in unit 8 for use: `FORMAT "DISKNAME",I01`
- To quick-erase a previously prepared disk in unit 8: `FORMAT "DISKNAME"`

`CHDIR` and `MKDIR` support sub-directories on D81 disks and the SD card.

- To change to a sub-directory of the current directory on unit 8: `CHDIR "SUBDIR"`
- To return to the root directory on unit 8: `CHDIR "/"`
- To make a sub-directory on unit 8: `MKDIR "SUBDIR"`
- To change to a sub-directory on the SD card: `CHDIR "SUBDIR",U12`
- To change to the parent directory of the current directory (SD card only): `CHDIR "..",U12`

`LOCK` and `UNLOCK` set the status of a file on disk so that it cannot be deleted when locked.

- To lock a file on unit 8: `LOCK "FILENAME"`
- To unlock a file on unit 8: `UNLOCK "FILENAME"`

`IMPORT` takes a SEQ file of PETSCII text as if typed into the BASIC editor. Unnumbered lines are ignored: it does not run commands in immediate mode.

- To import a text file as BASIC: `IMPORT "LISTING"`
  - Any BASIC program already in memory will remain in memory, with only the lines in the listing overwriting what is already there. This makes `IMPORT` useful for adding a file of common routines to an existing program.
- To export the current BASIC program as a text file that can be imported: `DOPEN#1,"LISTING",W:CMD 1:LIST:DCLOSE#1`
  - Every command that outputs text between `CMD 1` and `DCLOSE#1` writes to the file. For example, you can add arguments to `LIST` to only export a portion of a program: `LIST 2000-2999`

### Newer graphics commands

`CUT`, `GCOPY`, `PASTE` act on a rectangle of a graphics screen as a clipboard. `GCOPY` copies a rectangle of pixels to a buffer; `CUT` copies the rectangle then fills with the color of the pen. `PASTE` paints the previously copied rectangle onto the screen at a given location. An example from the manual:

```
10 SCREEN 320,200,2
20 BOX 60,60,300,180,1
30 PEN 2
40 CUT 140,80,40,40
50 PASTE 10,10,40,40
60 GETKEY A$
70 SCREEN CLOSE
```

`DOT` draws a single pixel on a graphics screen.

```
10 SCREEN 320,200,5
20 DOT 100, 80, 7
30 GETKEY A$
40 SCREEN CLOSE
```

`CHARDEF` changes the image for a single character based on its arguments. This makes it easy to produce custom fonts or character graphics in a BASIC program.

- To replace the letter A with a happy face:

```
CHARDEF 1,$3C,$7E,$DB,$FF,$BD,$C3,$7E,$3C
```

- To restore the PETSCII font: `FONT C`

### Newer memory commands

`MEM` reserves 8K segments of memory in banks 4 and 5 for use by the program, such that the graphics library does not use them.

- To reserve `$40000-$41FFF` for program use: `MEM 1,0`

`SETBIT` and `CLRBIT` set and clear a given bit at a given byte memory location. Bit numbers are 0-7 from least significant to most significant.

- Given address `$03FFF` containing the bit pattern `00110111` (`$37`), to set bit 6 so it becomes `0110111` (`$77`): `SETBIT $03FFF, 6`

`WPOKE` and `WPEEK()` write and read, respectively, a 16-bit ("word") value at two consecutive locations in memory, least significant byte first.

- To store the word `$FABC` across byte addresses `$0C000` (the least significant byte `$BC`) and `$0C001` (the most significant byte `$FA`): `BANK 0 : WPOKE $C000,$FABC`
- To read the 16-bit value stored at `$0C000-$0C001`: `V = WPEEK($C000)`

### Other newer BASIC features

The `FREEZER` command opens the Freeze menu, as if you pressed Restore for a second.

The `INFO` command prints useful information about the system and available BASIC memory.

```{tip}
For bleeding edge information about new BASIC features as they stabilize and get added to the documentation, see [the mega65-user-guide Github repo commit list](https://github.com/MEGA65/mega65-user-guide/commits/master). We also discuss new features in [the community Discord](https://discord.com/invite/5DNvESf).
```
