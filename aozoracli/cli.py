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
@click.option('--author', required=False)
def books(id, title, author):
    import aozoracli.books
    aozoracli.books.main({
            'id': id,
            'title': title,
            'author': author,
    })

@cli.command(help='list persons')
@click.option('--id', required=False, type=int)
@click.option('--name', required=False)
def persons(id, name):
    import aozoracli.persons
    aozoracli.persons.main({
            'id': id,
            'name': name,
    })

@cli.command(help='show content')
@click.option('--id', required=True, type=int)
@click.option('--format', required=False, default='txt', type=click.Choice(['txt', 'html']))
def content(id, format):
    import aozoracli.content
    res = aozoracli.content.main({
            'id': id,
            'format': format,
    })

