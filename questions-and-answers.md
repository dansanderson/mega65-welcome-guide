# Questions and answers

Here are a few additional common questions about the status of MEGA65 features.

## Does the cartridge port work?

Yes! If a Commodore 64 cartridge is in the MEGA65 cartridge port when the MEGA65 is turned on, it will attempt to start in GO64 mode and execute the cartridge.

The latest version of the C64 core supports hardware cartridges. Be sure to enable the hardware cartridge port in the C64 core Help menu.

Starting with release v0.96, with the new core installed in slot 0, you can configure the core selection process to automatically select the C64 core if it is installed and a C64 cartridge is connected. This allows you to play C64 cartridge games with full compatibility, as an optional alternative to GO64 mode.

Also starting with release v0.96, there is [a protocol](https://mega65.atlassian.net/wiki/spaces/MEGA65/pages/36962324/MEGA65+Style+Cartridge+Work+in+Progress) for implementing MEGA65 cartridges. We can look forward to MEGA65 games being published as cartridges in the future.

## Does the Ethernet port do anything?

Yes! As we saw in this guide, platform release v0.96 introduces a built-in feature for transferring files over the Ethernet connection.

The Ethernet port can be used by software to connect to other devices and to the Internet. There isn't much software for it yet.

[The MEGA65 WeeIP repo](https://github.com/MEGA65/mega65-weeip) by Paul has active open source projects for a telnet-based terminal program [Haustierbegriff (PETterminal)](https://files.mega65.org/html/main.php?id=bc0b666a-ba62-423f-b301-b2f39bb03ed9) and an HTTP file fetcher. See [Paul's blog entry exploring the technical details](https://c65gs.blogspot.com/2021/07/debugging-tcpip-problems.html). Contributions welcome!
