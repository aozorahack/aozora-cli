# 青空文庫コマンドラインツール

## 環境

Python 3.x

Dependencies

- [requests](https://github.com/kennethreitz/requests)
- [click](https://github.com/pallets/click)
- [jmespath](https://github.com/jmespath/jmespath.py)

## 使い方

### インストール

pip

1. `pip install aozora-cli`

### Development

1. `git clone https://github.com/aozorahack/aozora-cli`
1. `cd aozora-cli`
1. `export PYTHONPATH=.`

### 環境変数

- `AOZORAPI_HOST`: 青空APIサーバのホスト名:ポート

## コマンド

### books

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

### persons

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

### content

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

