# pyinspirehep
The [pyinspirehep](https://pypi.org/project/pyinspirehep/) is a package which is a simple wrapper of [**inspirehep API**](https://github.com/inspirehep/rest-api-doc) in Python.

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

client = Client()
paper = client.get_literature("451647")
paper["metadata"]["titles"][0]["title"]
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

#### Author
There is an `Author` class which is a data models for author objects of Inspirehep and you can use its methods for various operations on Author:
```Python
>>> from pyinspirehep import Client
>>> client = Client()
>>> author = client.get_author_object('1019113')  # 1019113 is the inspire hep control number of 't Hooft
>>> author.get_name()
"'t Hooft, Gerardus"
>>> author.get_name_preferred()
"Gerardus 't Hooft"
>>> author.get_institutions()
['Utrecht U.', 'Utrecht U.', 'Utrecht U.']
>>> author.get_institutions_ids()
['903317', '903317', '903317']
>>> author.get_id_orcid()
'0000-0002-5405-5504'
>>> author.get_arxiv_categories()
['gr-qc', 'hep-th', 'quant-ph']
>>> author.get_advisors()
['Veltman, Martinus J.G.']
>>> author.get_advisors_id()
['984831']
```

## Contributing
Everyone who want's to work on this library is welcome to collaborate by creating pull requests or sending email to authors.


## LICENSE
MIT License

Copyright (c) [2022] [Javad Ebadi, Vahid Hoseinzade]
