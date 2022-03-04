import os
from pathlib import Path
from datetime import date
import json
from unittest import TestCase
from pyinspirehep.literature import (
    Literature,
    LiteratureMetadata,
    )


directory = Path(__file__).parent
with open( os.path.join(directory, 'literature.json'), 'r') as f:
    METADATA_SAMPLE = json.load(f)


class LiteratureTest(TestCase):

    def setUp(self) -> None:
        metadata = LiteratureMetadata.from_dict(METADATA_SAMPLE)
        self.literature=Literature(
            id=1713040,
            links = [],
            metadata = metadata,
        )
        return super().setUp()

    def test_get_citation_count(self):
        self.assertEqual(self.literature.get_citation_count(), 26)

    def test_get_references_ids(self):
        self.assertSetEqual(
            set(self.literature.get_references_ids()),
            set(['3438',
             '537599',
             '1707528',
             '119084',
             '1334702',
             '1334702',
             '1489868',
             '534214',
             '1702664',
             '1512593',
             '1685089',
             '1509929',
             '1391503',
             '1317641',
             '1596919',
             '1614158',
             '1628805',
             '1477399',
             '1697838',
             '1709994',
             '1665240',
             '1699990',
             '1712684',
             '1702624',
             '1257621',
             '922834',
             '912611',
             '1121392',
             '712925',
             '1244313',
             '796887',
             '1614097',
             '955176',
             '779080',
             '1500696',
             '1364506',
             '1500688',
             '1409104',
             '1603635',
             '1633591',
             '1094530',
             '1318669',
             '1114764',
             '1473822',
             '1208951',
             '1241586',
             '1307489',
             '918766',
             '918766',
             '1644387',
             '1335264',
             '1699055',
             '1468075'])
        )
