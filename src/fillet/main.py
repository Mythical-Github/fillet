import sys

from fillet import cli, trimmer


def enable_vt():
    return


def main():
    enable_vt()
    if len(sys.argv) > 1:
        cli.cli()
    else:
        trimmer.automatic_detection_run()
