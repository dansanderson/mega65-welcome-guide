# Using the JTAG connection

The MEGA65 main board has a 12-pin [JTAG](https://en.wikipedia.org/wiki/JTAG) connection, a standard for connecting test equipment to devices. It is not intended for regular users of a device—but we MEGA65 owners are not regular users, are we?

With a JTAG USB adapter and software available on Filehost, you can connect your PC directly to the main board to:

- Transfer files directly from your PC to MEGA65 without removing the SD card
- Perform remote debugging on programs and even the built-in MEGA65 utilities
- Upload cores for testing

The MEGA65 does not have a user-accessible port for the JTAG connection. You will have to acquire a JTAG USB adapter and a mini-USB cable, install it, and run the cable out the back of the MEGA65 case.

```{tip}
For another version of these instructions with more photos, see [JTAG adapter, how to plug and DIP switch settings](https://files.mega65.org?ar=3c388c8c-bc3f-461b-84bb-e12dfd479ae2).
```

## Acquiring a JTAG adapter

The [XMOD FTDI JTAG Adapter TE0790-03](https://shop.trenz-electronic.de/en/TE0790-03-XMOD-FTDI-JTAG-Adapter-Xilinx-compatible) (Trenz Electronic) is compatible with the MEGA65. You might also be able to [order the TE0790-03 from DigiKey](https://www.digikey.com/en/products/detail/TE0790-03/1686-1180-ND/10071026). As of this writing, this item is difficult to get to supply chain issues.

![XMOD FTDI JTAG Adapter TE0790-03 in its box](photos/jtag_box.jpeg)
![XMOD FTDI JTAG Adapter TE0790-03 out of its box](photos/jtag_unit.jpeg)

## Installing the JTAG adapter

You will have to open the MEGA65 case to connect the adapter to the 12-pin JTAG connector on the main board, in the back right corner. (See {ref}`opening-the-case:opening the mega65 case` for an annotated photo of the main board.) The adapter connects with the mini-USB connector facing to the right.

![Installing the JTAG adapter](photos/jtag_installing.jpeg)

Use a pin to set the DIP switches on the connector to left, right, right, left. This configures the adapter to draw power from the USB connection instead of the MEGA65.

![Setting the JTAG adapter DIP switches](photos/jtag_switches.jpeg)

Connect a mini-USB cable to the JTAG connector, and run the cable out the back of the MEGA65 case. You can feed it out the cartridge port, or punch out one of the unused ports in the back case. Connect the other end to your PC.

## Getting the software tools

On your PC, download the M65Connect app for Windows, Mac, or Linux, available from the Filehost. You can also use the `m65` and `m65_ftp` command line tools, available from [the mega65-tools Github repository](https://github.com/MEGA65/mega65-tools/releases/tag/CI-latest). If you're interested in the debugging feature, download the M65 Debugger app from Filehost.

See [the M65Connect README](https://github.com/MEGA65/m65connect) and [the m65dbg README](https://github.com/MEGA65/m65dbg) for more information on how to use these tools.
