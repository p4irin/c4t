import argparse
from . import Assets, __version__

def cli() -> None:
    parser = argparse.ArgumentParser(
        description="Install 'Chrome for Testing' assets.",
        epilog='Reference: https://github.com/GoogleChromeLabs/chrome-for-testing'
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

    args = parser.parse_args()

    if args.command == 'install':
        print(f"Installing version '{args.version}'")
        assets = Assets()
        assets.install(version=args.version)
