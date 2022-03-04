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

#### Literature
There is a `Literature` class which is a data model for literature objects of Inspirhep and you can use that for operations on literature objects:
```Python
>>> from pyinspirehep.client import Client
>>> client = Client()
>>> literature = client.get_literature_object('1713040')
>>> n_citations = literature.get_citation_count()
>>> print(n_citations)
26
>>> references_ids = literature.get_references_ids()
>>> print(references_ids)
['3438', '537599', '1707528', '119084', '1334702', '1334702', '1489868', '534214', '1702664', '1512593', '1685089', '1509929', '1391503', '1317641', '1596919', '1614158', '1628805', '1477399', '1697838', '1709994', '1665240', '1699990', '1712684', '1702624', '1257621', '922834', '912611', '1121392', '712925', '1244313', '796887', '1614097', '955176', '779080', '1500696', '1364506', '1500688', '1409104', '1603635', '1633591', '1094530', '1318669', '1114764', '1473822', '1208951', '1241586', '1307489', '918766', '918766', '1644387', '1335264', '1699055', '1468075']
```

### Clone
The are classes in `pyinspirehpe.contrib.clone` module which can be used to clone all avaialable data. For example to get all literature data from the API:
```Python
>>> import os
>>> from pathlib import Path
>>> from pyinspirehep.contrib.clone import LiteratureClone
>>> directory = os.path.join(Path.home(), "Desktop", "literature")
>>> cloner = LiteratureClone(directory)
>>> cloner.clone()
``` 
Note that you need stable interent connection to clone all data. The data will be saved as json file batches in a directory and if you lost the connection, you can re-run the `clone` method by givin the appropriate arguments.

## Contributing
Everyone who want's to work on this library is welcome to collaborate by creating pull requests or sending email to authors.


## LICENSE
MIT License

Copyright (c) [2022] [Javad Ebadi, Vahid Hoseinzade]
