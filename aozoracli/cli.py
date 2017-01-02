#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    _print_utf8(res.encode("UTF-8"))

def _print(res, output_format):
    if res == False:
        return

    if output_format == 'json':
        import json
        output = json.dumps(res, ensure_ascii=False).encode("UTF-8")
    elif  output_format == 'txt':
        import aozoracli.output.txt
        output = aozoracli.output.txt.dump(res)
    else:
        output = res
    _print_utf8(output)

def _print_utf8(output):
    try:
        unicode
        print(output)
    except:
        print(output.decode("UTF-8"))

