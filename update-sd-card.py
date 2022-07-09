#!/usr/bin/env python3
#
# Updates the system files of a MEGA65 SD card, from a bluewaysw build.
#
# The full process creates a backup of the SD card, installs the system
# files and core file using a technique that avoids fragmenting files,
# and removes dot-files from the SD card.
#
# To get a bluewaysw build, look for messages posted by Jenkins in the
# #experimental-releases channel of the MEGA65 Discord. The download
# URL looks something like this:
# https://ftp.bluewaysw.de/ci-logs/MEGA65/f5553164001c3fa8ad1d4a73bb985965c01e4f17-198.zip
#
# Unpack the .zip file, then provide the path to the tool.
#
#  python3 update-sd-card.py --sdcardpath=/Volumes/MyCard f5553164001c3fa8ad1d4a73bb985965c01e4f17-198
#
# Use the --dry-run option to print messages about what it will do
# without actually doing it. Use the --verbose option to print those
# messages while also doing it.
#
# TODO:
# * Support installing from SD Card Essentials archives from the Filehost.
# * Support automatically unzipping the archive, if the archive file is provided.

import click
import datetime
import os.path
import shutil


DEFAULT_SD_CARD_PATH = '/Volumes/Untitled'
DEFAULT_BACKUP_DIR = os.path.expanduser('~/Desktop')


def find_unused_name(pth):
    tmpnum = 1
    tmppth = pth
    while os.path.exists(tmppth):
        tmppth = pth + '_' + str(tmpnum)
        tmpnum += 1
    return tmppth


def backup_sdcard(srcpath, backupdir, verbose, dry_run):
    backup_root = find_unused_name(os.path.join(
        backupdir,
        'm65_sd_bak_' + datetime.datetime.now().strftime('%Y%m%d')))
    if verbose or dry_run:
        print(f'Backing up SD card from {srcpath} to {backup_root}')
    if not dry_run:
        shutil.copytree(srcpath, backup_root, ignore=shutil.ignore_patterns('.*'))


def replace_file(srcpath, destpath, verbose, dry_run):
    tmppath = find_unused_name(destpath)
    if tmppath != destpath:
        if verbose or dry_run:
            print(f'Replacing SD card file, {srcpath} to {destpath}')
        if not dry_run:
            os.rename(destpath, tmppath)
            shutil.copyfile(srcpath, destpath)
            os.remove(tmppath)
    else:
        if verbose or dry_run:
            print(f'Copying file to SD card, {srcpath} to {destpath}')
        if not dry_run:
            shutil.copyfile(srcpath, destpath)


def replace_sd_card_files(srcdir, destdir, verbose, dry_run):
    for fname in os.listdir(srcdir):
        replace_file(os.path.join(srcdir, fname), os.path.join(destdir, fname), verbose, dry_run)


def clean_dotfiles(destdir, verbose, dry_run):
    for fname in os.listdir(destdir):
        if fname.startswith('.'):
            to_remove = os.path.join(destdir, fname)
            if verbose or dry_run:
                print(f'Removing dotfile {to_remove}')
            try:
                if not dry_run:
                    if os.path.isfile(to_remove):
                        os.remove(to_remove)
                    else:
                        shutil.rmtree(to_remove)
            except PermissionError as e:
                if verbose or dry_run:
                    print(f'Could not remove dotfile {to_remove}')


@click.command()
@click.option('--sdcardpath', default=DEFAULT_SD_CARD_PATH, help='Filesystem path to the mounted SD card root')
@click.option('--backupdir', default=DEFAULT_BACKUP_DIR, help='Filesystem path to the mounted SD card root')
@click.option('--verbose/--no-verbose', default=False, help='Print messages of what is happening')
@click.option('--dry-run/--no-dry-run', default=False, help='Do not perform actions, only report what would happen')
@click.argument('releasepath')
def main(sdcardpath, backupdir, verbose, dry_run, releasepath):
    if not os.path.exists(sdcardpath):
        raise click.ClickException(message=f'SD card path does not exist. (Is the card inserted?) : {sdcardpath}', error_code=1)
    if not os.path.isdir(sdcardpath):
        raise click.ClickException(message=f'SD card path is not a directory: {sdcardpath}', error_code=1)
    if not os.path.exists(os.path.join(sdcardpath, 'FREEZER.M65')):
        raise click.ClickException(message=f'SD card does not contain an expected file. (Was this card formatted by the MEGA65?)')

    if not os.path.exists(backupdir):
        raise click.ClickException(message=f'Backup directory does not exist: {backupdir}', error_code=1)

    if not os.path.exists(releasepath):
        raise click.ClickException(message=f'Release path does not exist: {releasepath}', error_code=1)
    if not os.path.isdir(releasepath):
        raise click.ClickException(message=f'Release path is not a directory: {releasepath}', error_code=1)
    if not os.path.exists(os.path.join(releasepath, 'mega65r3.cor')):
        raise click.ClickException(message=f'Release directory does not contain an expected file. (Is this an unpacked bluewaysw file host .zip?)')

    backup_sdcard(sdcardpath, backupdir, verbose, dry_run)
    replace_sd_card_files(os.path.join(releasepath, 'sdcard-files'), sdcardpath, verbose, dry_run)
    replace_file(os.path.join(releasepath, 'mega65r3.cor'), os.path.join(sdcardpath, 'mega65r3.cor'), verbose, dry_run)
    clean_dotfiles(sdcardpath, verbose, dry_run)


if __name__ == '__main__':
    main()
