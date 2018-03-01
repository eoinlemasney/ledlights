# -*- coding: utf-8 -*-

"""Console script for ledlights."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for ledlights."""
    click.echo("Replace this message by putting your code into "
               "ledlights.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input", input)
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
