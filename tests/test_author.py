import datetime
from unittest import TestCase
from pyinspirehep.data_models import Author, AuthorMetadata


class AuthorTest(TestCase):

    def setUp(self) -> None:
        metadata = AuthorMetadata(
            project_membership=[
                {
                    'name': 'CERN-LHC-cMS',
                    'record': {'$ref': 'https://inspirehep.net/api/experiments/1108642'},
                    'current': False,
                    'curated_relation': True},
                ],
            positions=[
                {
                    'record': {'$ref': 'https://inspirehep.net/api/institutions/906446'},
                    'current': True,
                    'start_date': '2015',
                    'institution': 'IPM, Tehran',
                    'curated_relation': True,
                    },
                {
                    'record': {'$ref': 'https://inspirehep.net/api/institutions/904894'},
                    'end_date': '2015',
                    'start_date': '2013',
                    'institution': 'Sharif U. of Tech.',
                    'curated_relation': True,
                    }
                ],
            advisors=[
                {
                    'ids': [
                        {'value': 'INSPIRE-00048278',
                        'schema': 'INSPIRE ID'}
                        ],
                    'name': 'Mohammadi Najafabadi, Mojtaba',
                    'record': {'$ref': 'https://inspirehep.net/api/authors/1023812'},
                    'degree_type': 'phd',
                    }
                    ],
            email_addresses=[
                {'value': 'javadebadi@ipm.ir', 'current': True},
                ],
            ids=[
                {'value': '0000-0002-4600-8310', 'schema': 'ORCID'},
                {'value': 'CERN-838837', 'schema': 'CERN'},
                {'value': 'J.Ebadi.1', 'schema': 'INSPIRE BAI'},
                {'value': 'INSPIRE-00682582', 'schema': 'INSPIRE ID'},
                {'value': 'javad-ebadi-3629a481', 'schema': 'LINKEDIN'},
                ],
            name={
                'value': 'Ebadi, Javad',
                'native_names': ['جواد عبادی'],
                'preferred_name': 'Javad Ebadi',
                },
            stub=False,
            status='active',
            schema='https://inspirehep.net/schemas/records/authors.json',
            deleted=False,
            control_number=1679997,
            legacy_version='20190412203308.0',
            arxiv_categories=['hep-ph'],
            legacy_creation_date=datetime.date(2018, 6, 28)
            )
        self.author = Author(
            id=1679997,
            links=[],
            metadata=metadata,
            )
        return super().setUp()


    def test_get_name(self):
        self.assertEqual(self.author.get_name(), "Ebadi, Javad")

    def test_get_name_preferred(self):
        self.assertEqual(self.author.get_name_preferred(), "Javad Ebadi")

    def test_get_name_native(self):
        self.assertEqual(self.author.get_names_native(), ['جواد عبادی'])

    def test_get_email_addressess(self):
        self.assertEqual(
            self.author.get_email_addresses(),
            ['javadebadi@ipm.ir'],
            )

    def test_get_email_current(self):
        self.assertEqual(
            self.author.get_email_current(),
            'javadebadi@ipm.ir',
            )

    def test_get_id_orcid(self):
        self.assertEqual(
            self.author.get_id_orcid(),
            '0000-0002-4600-8310',
        )

    def test_get_id_cern(self):
        self.assertEqual(
            self.author.get_id_cern(),
            'CERN-838837',
        )

    def test_get_id_linkedin(self):
        self.assertEqual(
            self.author.get_id_linkedin(),
            'javad-ebadi-3629a481',
        )

    def test_get_id_inspire_bai(self):
        self.assertEqual(
            self.author.get_id_inspire_bai(),
            'J.Ebadi.1',
        )

    def test_get_id_inspire_id(self):
        self.assertEqual(
            self.author.get_id_inspire_id(),
            'INSPIRE-00682582',
        )

    def test_get_arxiv_categories(self):
        self.assertEqual(
            self.author.get_arxiv_categories(),
            ['hep-ph'],
        )

    def test_get_id(self):
        self.assertEqual(
            self.author.get_id(),
            '1679997',
        )
        self.assertEqual(
            self.author.get_id(as_int=True),
            1679997,
        )

    def test_get_project_memberships(self):
        self.assertEqual(
            self.author.get_project_memberships(),
            ['CERN-LHC-cMS']
        )
        self.assertEqual(
            self.author.get_project_memberships(current=True),
            None,
        )

    def test_get_project_memberships_ids(self):
        self.assertEqual(
            self.author.get_project_memberships_ids(),
            ['1108642']
        )
        self.assertEqual(
            self.author.get_project_memberships_ids(current=True),
            None,
        )

    def test_get_advisors(self):
        self.assertEqual(
            self.author.get_advisors(),
            ['Mohammadi Najafabadi, Mojtaba']
        )

    def test_get_advisors_id(self):
        self.assertEqual(
            self.author.get_advisors_id(),
            ['1023812']
        )

    def test_get_institutions(self):
        self.assertEqual(
            self.author.get_institutions(),
            ['IPM, Tehran', 'Sharif U. of Tech.']
        )

    def test_get_institutions_ids(self):
        self.assertEqual(
            self.author.get_institutions_ids(),
            ['906446', '904894'],
        )

    def test_get_positions(self):
        self.assertEqual(
            self.author.get_positions(),
            [
                {
                    'record': {'$ref': 'https://inspirehep.net/api/institutions/906446'},
                    'current': True,
                    'start_date': '2015',
                    'institution': 'IPM, Tehran',
                    'curated_relation': True,
                },
                {
                    'record': {'$ref': 'https://inspirehep.net/api/institutions/904894'},
                    'end_date': '2015',
                    'start_date': '2013',
                    'institution': 'Sharif U. of Tech.',
                    'curated_relation': True,
                }
            ]
        )

        
        
