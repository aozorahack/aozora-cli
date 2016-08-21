import json
import click
import jmespath

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
    else:
        ctx.invoked_subcommand


@cli.command(help="show version")
def version():
    import aozoracli.version
    print(aozoracli.version.__version__)

@cli.command(help='list books ')
@click.option('--id', required=False, type=int)
@click.option('--title', required=False)
@click.option('--author', required=False)
@click.option('--output', required=False, default='json', type=click.Choice(['json', 'txt']))
@click.option('--query', required=False, type=str)
def books(id, title, author, output, query):
    import aozoracli.books
    res = aozoracli.books.main({
            'id': id,
            'title': title,
            'author': author,
    })
    if query != None:
        res = jmespath.search(query, res)

    _print(res, output)

@cli.command(help='list persons')
@click.option('--id', required=False, type=int)
@click.option('--name', required=False)
@click.option('--output', required=False, default='json', type=click.Choice(['json', 'txt']))
@click.option('--query', required=False, type=str)
def persons(id, name, output, query):
    import aozoracli.persons
    res = aozoracli.persons.main({
            'id': id,
            'name': name,
    })
    if query != None:
        res = jmespath.search(query, res)

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
    # contentは、Jsonレスポンスではないので、とりあえずそのまま出力
    print(res)

def _print(res, output_format):
    if res == False:
        return

    if output_format == 'json':
        output = json.dumps(res, ensure_ascii=False)
    elif  output_format == 'txt':
        output = _format_print_txt(res)
    else:
        output = res
    print(output)

def _format_print_txt(data):
    if isinstance(data, list):
        return "\n".join([_to_txt(d) for d in data])
    elif isinstance(data, dict):
        return _format_print_txt(d)
    else:
        return str(data)

def _to_txt(data):
    if isinstance(data, list):
        output = ""
        for d in data:
            output += _to_txt(d)
        return output
    elif isinstance(data, dict):
        sorted_keys = sorted(data.keys())
        sorted_values = []
        for key in sorted_keys:
            val = _to_txt(data[key])
            sorted_values.append(val)
        return " ".join(sorted_values)
    else:
        return str(data)

