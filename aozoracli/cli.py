import json
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
@click.option('--output', required=False, default='json', type=click.Choice(['json']))
def books(id, title, author, output):
    import aozoracli.books
    res = aozoracli.books.main({
            'id': id,
            'title': title,
            'author': author,
    })
    _print(res, output)

@cli.command(help='list persons')
@click.option('--id', required=False, type=int)
@click.option('--name', required=False)
@click.option('--output', required=False, default='json', type=click.Choice(['json']))
def persons(id, name, output):
    import aozoracli.persons
    res = aozoracli.persons.main({
            'id': id,
            'name': name,
    })
    _print(res, output)

@cli.command(help='show content')
@click.option('--id', required=True, type=int)
@click.option('--format', required=False, default='txt', type=click.Choice(['txt', 'html']))
@click.option('--output', required=False, default='txt', type=click.Choice(['txt']))
def content(id, format, output):
    import aozoracli.content
    res = aozoracli.content.main({
            'id': id,
            'format': format,
    })
    _print(res, output)

def _print(res, output_format):

    if res == False:
        return

    if output_format == 'json':
        output = json.dumps(res, ensure_ascii=False)
    elif  output_format in {'txt', 'html'}:
        output = res
    else:
        output = res
    print(output)

