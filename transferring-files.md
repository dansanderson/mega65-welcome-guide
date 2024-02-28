# Transferring files

With the v0.96 release installed, you can now use an Ethernet connection to transfer files to and from your MEGA65. You can use an Ethernet cable to connect your MEGA65 to your local network router, or connect it directly to the Ethernet jack of your PC. This is also expected to work with Ethernet-to-USB adapters for laptops, and also Wifi-Ethernet adapters for connecting to a wireless network.

This feature is described in full in the _MEGA65 User's Guide, 2nd edition_ in chapter 7. Here's a quick overview.

## M65Connect

The M65Connect app runs on your PC, and is available for Windows, macOS, and Linux. It's a windowed app, and also includes command line tools that perform similar functions.

Download:

* [M65Connect for Windows (Intel)](https://files.mega65.org?id=d612d745-360e-4e86-8e15-14af525b6220)
* [M65Connect for Windows (ARM)](https://files.mega65.org?id=1b849d0a-2ceb-44aa-beb4-a2cdfa51eb19)
* [M65Connect for macOS](https://files.mega65.org?id=5919a8b8-c23c-4616-9a52-37e077076638)
* [M65Connect for Linux](https://files.mega65.org?id=c1dbc7fe-89ad-4f1d-9e72-ad3f55cf02a1)

```{tip}
Mac users: You will need to run a command to convince macOS Gatekeeper to allow the app to be run. Unpack the archive to produce the `M65Connect.app`. Open the Terminal, then change the current working directory to where `M65Connect.app` resides. Run this command: `xattr -cr M65Connect.app` You should now be able to double-click the app icon to run it.
```

## Setting DIP switch #2

If you have a 2022 MEGA65, you will need to set a DIP switch on the main board to use Ethernet file transfer. If you have a 2024 MEGA65, this switch is flipped for you at the factory.

Open the case, then locate the four DIP switches on the main board. Examine the markings on the DIP switch and identify switch #2, as well as the On position. Notice that when facing the front of the machine, the switches are numbered from front to back, the On position is to the left, and all switches are Off by default. Flip switch #2 to On.

It is safe to leave DIP #2 in this position for regular operation.

## Enabling network listening

By default, the MEGA65 ignores all attempts by other computers to connect to it over the network. Software running on the MEGA65 can listen for network connections, but the MEGA65 does not do this on its own.

To transfer files with M65Connect, you must tell the MEGA65 to listen for incoming connection attempts from M65Connect. To enable a network listening session, press <kbd>Shift</kbd> + <kbd>£</kbd>. The power light blinks between yellow and green when network listening is active.

```{tip}
If the power lights do not start to blink when you press <kbd>Shift</kbd> + <kbd>£</kbd>, double-check that you are running the v0.96 core, and that DIP switch #2 is set to On.
```

M65Connect should notice when you put the MEGA65 into network listening mode, saying it is connected. The "PRG" and "SD Card" buttons are enabled. You can now proceed to transfer files.

## Transferring files with M65Connect

In M65Connect, click the "SD Card" button. This opens the file transfer utility, on the MEGA65 side and in M65Connect.

```{note}
Starting a file transfer session resets the MEGA65 to load the file transfer utility. Be sure to save any data on the MEGA65 before starting the session.
```

Use the pane on the left to navigate files on your PC. Use the pane on the right to navigate files on the MEGA65 SD card. To transfer a file, select the file, then click the arrow button. The button indicates the direction the file will transfer.

You can also use M65Connect to create D81 disk images, and copy files to and from D81 disk images. Locate a D81 disk image on your PC or click the + D81 button to create one, then click the ”Open” command in the file browser to open the disk image in the left pane. Transfer files to and from the image with the arrow button. Click the X button in the upper right to return to the file browser.
Click the Close button to end the file transfer session and close the SD Card Manager window. This resets the MEGA65.