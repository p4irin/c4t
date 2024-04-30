import argparse
import os
import typing
from . import Assets, __version__

assets = Assets()


def list_versions() -> list:
    versions = []
    items = os.listdir(assets.path)
    for n, item in enumerate(items, start=0):
        if os.path.isdir(f'{assets.path}/{item}'):
            print(f'{n} - {item}')
            versions.append(item)
    return versions


def select_version(versions: list) -> typing.Union[str, None]:
    try:
        selection = int(input("Select a version by number: ")) - 1
        return versions[selection]
    except ValueError:
        return
    except IndexError:
        return


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

    parser.add_argument(
        '-a',
        '--active',
        action='store_true',
        help="Show the currently active version of 'Chrome for Testing' assets"
             + " installed."
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

    sub_parsers.add_parser(
        'list',
        help='Show installed versions.'
    )

    sub_parsers.add_parser(
        'switch',
        help='Switch the active version.'
    )    

    args = parser.parse_args()

    if args.active:
        print("Active version of 'Chrome for Testing' assets installed: "
              + f'{assets.active_version}'
        )

    if args.command == 'install':
        print(f"Installing version '{args.version}'")
        assets.install(version=args.version)

    if args.command == 'path':
        print(f'Path to assets: {assets.path}')

    if args.command == 'list':
        list_versions()

    if args.command == 'switch':
        versions = list_versions()
        version = select_version(versions)
        if not version is None:
            assets.switch(to_version=version)