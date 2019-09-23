from datetime import datetime

import click

from digibujogens.core import logger
from digibujogens.generators import spread


LOG = logger.Logger(__name__)
LOG.start(level='DEBUG')


command_settings = {
    "ignore_unknown_options": True,
}

@click.command(context_settings=command_settings)
def main():
    date = datetime.now()
    click.echo(spread.monthly(date))


if __name__ == "__main__":
    main()
