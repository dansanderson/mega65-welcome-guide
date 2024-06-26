# Opening the MEGA65 case

Your MEGA65 consists of an injection molded plastic case, built-in keyboard and disk drive, ports for peripherals, and internal components. The case is designed to be opened by its owner if needed.

*You may not need to open the case at all!* With the latest firmware, you can perform all file transfers using an Ethernet connection, without ever removing the SD card. If you have a 2024 MEGA65, you don't even need a battery for the RTC: the R6 board includes a "super capacitor" that retains a charge for days at a time to keep the RTC ticking when not in use.

You may want to open the case for the following reasons:

-   To access the internal SD card
    -   There is a small door in the bottom of the case that provides access to the internal SD card without opening the case, but I find it too difficult to access this way. If you use the external microSD card slot as I recommend in this Guide, you won't need to access the internal SD card.
-   To install (or replace) the CR1220 or CR2032 battery for the Real-Time Clock
-   To resolve issues with the case by adjusting its assembly (see {ref}`hardware-issues:known hardware issues`)
-   To install a JTAG adapter (see {ref}`using-jtag:using the jtag connector`)
-   To install a replacement Real-Time Clock if the one built into the MEGA65 isn't working (see {ref}`hardware-issues:the real-time clock doesn't advance the time`)

To open the MEGA65 case, locate three screws along the bottom front of the case and remove them with a Phillips head screwdriver.

![The bottom of the MEGA65 with three screws for opening the case](photos/mega65_bottom.jpeg)

The case separates into a top piece and a bottom piece. The keyboard is attached to the top, while the disk drive, ports, and main board are attached to the bottom. The keyboard is connected to the main board with a ribbon cable.

![The MEGA65 with case open](photos/mega65_open.jpeg)

![The MEGA65 main board](photos/mainboard_annotated.jpeg)

![The RTC battery on the main board](photos/rtc_battery.jpeg)

Install the battery: type CR1220 for R3 main boards (2022 model), type CR2032 for R6 main boards (2024 model). Locate the battery holder on the main board. Insert the battery under the tab, with the positive (`+`) side facing upward. Push down to secure it.

```{tip}
See [Install battery CR1220 in MEGA65 for Real-Time Clock (RTC)](https://files.mega65.org?ar=14d5ca1e-bc16-45d4-83f5-41b0a0545e0d) for more photos and instructions. Remember that the R6 main board uses a CR2032 battery.
```

If you'd like to make a backup of the internal SD card for safe keeping, remove the full-size SD card from the internal slot. Connect it to your PC with an SD card reader. On your PC, copy all of the files to a folder. Eject the device from your PC, then return the card to the MEGA65's internal slot.

With the new Ethernet file transfer feature of the latest firmware, you don't need to remove the SD card at all: it can remain in the computer, and behave like an internal hard drive. Personally, I still like to add a microSD card in the external card slot, so I can keep the internal SD card in its factory condition. The MEGA65 only needs a memory card in one of the two slots.

To close the case, align the plastic tabs along the back of the top and bottom case parts, then replace the three screws.
