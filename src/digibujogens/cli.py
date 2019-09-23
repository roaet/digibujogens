import click


command_settings = {
    "ignore_unknown_options": True,
}

@click.command(context_settings=command_settings)
def main():
    click.echo("Life before death")


if __name__ == "__main__":
    main()
