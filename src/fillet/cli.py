import click
from trogon import tui

from fillet import trimmer


@tui()
@click.group()
def cli():
    pass


@cli.command(name='trim_install')


@click.option(
    '--install_directory',
    required=True,
    help='The path of the install directory to trim.'
)


@click.option(
    '--game',
    type=click.Choice(
        [
            "Call of Duty World at War", 
            "Call of Duty Black Ops I", 
            "Call of Duty Black Ops II"
        ], 
    case_sensitive=True
    ),
    help='An optional override string that overrides the automatic game detection. Choices: Call of Duty World at War, Call of Duty Black Ops I, or Call of Duty Black Ops II.'
)


@click.option(
    '--skip_verification',
    default=False,
    help='Skips the verification of all install files after the trim has been completed.'
)


def trim_install(
    install_directory: str,
    game: str,
    skip_verification: bool
):
    game_enum_value = game
    trimmer.trim_install(
        install_directory,
        game_enum_value,
        skip_verification
    )
