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
@click.option('--title', required=False)
def books(id, title):
    import aozoracli.books
    aozoracli.books.main({
            'id': id,
            'title': title,
    })

