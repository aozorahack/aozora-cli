import click

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
    else:
        ctx.invoked_subcommand


@cli.command(help='list books')
@click.option('--id', required=False, type=int)
@click.option('--name', required=False)
def books(id, name):
    import aozoracli.books
    aozoracli.books.main(
            id=id,
            name=name,
    )

