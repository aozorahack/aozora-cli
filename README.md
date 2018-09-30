# CLI tool for Aozora Bunko API

[(Japanese / 日本語)](./README.ja.md)

## Requirements

- Python 3.x
- [requests](https://github.com/kennethreitz/requests)
- [click](https://github.com/pallets/click)
- [jmespath](https://github.com/jmespath/jmespath.py)

## Getting Started

```
$ pip install aozora-cli
```

### For Development

1. `git clone https://github.com/aozorahack/aozora-cli`
1. `cd aozora-cli`
1. `export PYTHONPATH=.`

### Environment Variable

- `AOZORAPI_HOST`: `host` or `host:port` of Aozora Bunko API server (default: `www.aozorahack.net`)

## Commands

### `books`

```bash
$ ./bin/aozora books
```
#### Options

```bash
$ ./bin/aozora books --help
Usage: aozora books [OPTIONS]

  list books

Options:
  --id INTEGER
  --title TEXT
  --author TEXT
  --output [json|txt]
  --query TEXT
  --help               Show this message and exit.
```

### `persons`

```bash
$ ./bin/aozora persons
```
#### Options

```bash
$ ./bin/aozora persons --help
Usage: aozora persons [OPTIONS]

  list persons

Options:
  --id INTEGER
  --name TEXT
  --output [json|txt]
  --query TEXT
  --help               Show this message and exit.
```

### `content`

```bash
$ ./bin/aozora content --id <book_id>
```
#### Options

```bash
$ ./bin/aozora content --help

Usage: aozora content [OPTIONS]

  show content

Options:
  --id INTEGER         [required]
  --format [txt|html]
  --output [txt]
  --help               Show this message and exit.
```

### `ranking`

```bash
$ ./bin/aozora ranking --type [txt|xhtml] --year 2018 --month 8
```
#### Options

```bash
$ ./bin/aozora ranking --help
Usage: aozora ranking [OPTIONS]

  show access ranking

Options:
  --type [txt|xhtml]   [required] default=xhtml
  --year INTEGER       [required]
  --month INTEGER      [required]
  --query TEXT
  --output [json|txt]
  --help               Show this message and exit.
```
