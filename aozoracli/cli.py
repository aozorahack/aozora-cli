import click

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
    else:
        print('gonna invoke %s' % ctx.invoked_subcommand)


@cli.command(help='list books')
@click.argument('target', required=False)
def books(target):
    import aozoracli.books
    aozoracli.books.main()

