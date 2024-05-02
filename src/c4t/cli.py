import argparse
import os
import typing
from . import Assets, __version__

assets = Assets()


def cli() -> None:
    parser = argparse.ArgumentParser(
        description="Install 'Chrome for Testing' assets.",
        epilog='Reference: https://github.com/GoogleChromeLabs/'
               +'chrome-for-testing'
    )

    parser.add_argument(
        '-V',
        '--version',
        action='version',
        version=f'v{__version__}',
        help='Show version and exit.'
    )

    sub_parsers = parser.add_subparsers(
        title='Commands',
        dest='command'
    )

    sp_install = sub_parsers.add_parser(
        'install',
        help="Install a version of 'Chrome for Testing' assets."
    )
    sp_install.add_argument(
        '--version',
        default='latest',
        help="The version of 'Chrome for Testing' assets to install. " +
             "The default is '%(default)s'"
    )

    sub_parsers.add_parser(
        'path',
        help='Show the installation path of assets and exit.'
    )

    sp_list = sub_parsers.add_parser(
        'list',
        help='List versions'
    )
    sp_list.add_argument(
        '-a',
        '--active',
        action='store_true',
        help="List the currently active version of 'Chrome for Testing' assets"
             + " installed."
    )
    sp_list.add_argument(
        '-i',
        '--installed',
        action='store_true',
        help='List installed versions'
    )
    sp_list.add_argument(
        '-l',
        '--last-known-good-versions',
        action='store_true',
        help='List last known good versions'
    )

    sub_parsers.add_parser(
        'switch',
        help='Switch the active version.'
    )    

    args = parser.parse_args()

    if args.command == 'install':
        print(f"Installing version '{args.version}'")
        assets.install(version=args.version)

    if args.command == 'path':
        print(f'Path to assets: {assets.path}')

    if args.command == 'list':
        if args.installed:
            assets.installed()
        if args.active:
            print("Active version of 'Chrome for Testing' assets installed: "
                + f'{assets.active_version}'
        )
        if args.last_known_good_versions:
            pass

    if args.command == 'switch':
        assets.switch()
