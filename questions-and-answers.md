# Questions and answers

Here are a few additional common questions about the status of MEGA65 features.

## Does the cartridge port work?

Yes. If a Commodore 64 cartridge is in the MEGA65 cartridge port when the MEGA65 is turned on, it will attempt to start in C64 mode and execute the cartridge.

C64 mode is known to not be fully compatible with all Commodore 64 software, including some cartridges. If you are experiencing difficulty, try using the Freeze menu to switch from NTSC to PAL video mode or vice-versa (assuming you have a monitor that can show at least partial video with the other mode).

In my personal cartridge collection, I have also had difficulty with some cartridges not being recognized at all, causing the MEGA65 to boot into BASIC.

The C64 core does not yet support the cartridge port, as of this writing. Cartridge support is planned for the future.

## Does the ethernet port do anything?

The ethernet port does not yet do things most people would want, such as connect to the Internet or download files. For now it is mostly used for low-level testing and troubleshooting. (See {ref}`using-jtag:the m65 command line tool`, if you dare.)

There is software in active development to make good use of an ethernet connection. Stay tuned!
