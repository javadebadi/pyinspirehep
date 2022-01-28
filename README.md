# pyinspirehep
pyinspirehep is a package which is a simple wrapper of **inspirehep API** in Python.

### Installation
You can install this package using 
```bash
pip install pyinspirehep
```

### Features

- A simple client to get json data from Inspirehap API

### Usage
The class `Client` is the simple Python wrapper to get data from Inspirehep API.

```Python
from pyinsiprehep import Client

>>> client = Client()
>>> paper = client.get_literature("451647")
>>> paper["metadata"]["titles"][0]["title"]
'The Large N limit of superconformal field theories and supergravity'
```
The other method of the `Client` which may be usefull are here:
- `get_literature()`
- `get_author()`
- `get_institution()`
- `get_journal()`
- `get_experiment()`
- `get_seminar()`
- `get_conference()`
- `get_job()`
- `get_doi()`
- `get_arxiv()`
- `get_orcid()`
- `get_data()`

Each of these methods have a docstring you can get using `help` function of the Python. Basically all of them gets an identifier which determines the record in Inspirehep database.

## Contributing
Everyone who want's to work on this library is welcome to collaborate by creating pull requests or sending email to authors.


## LICENSE
MIT License

Copyright (c) [2022] [Javad Ebadi, Vahid Hoseinzade]
