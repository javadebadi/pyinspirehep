"""Client to use Inspirehep API.

The client.py moducle contains the base class `Client` which can be used to
get data from Inspirehep API.

"""

import requests
from pyinspirehep.exception import (
    InspirehepPIDDoesNotExistError,
    InspirehepTooManyRequestsError,
)
import time
from pyinspirehep.data_models import SingleRecordResponse


class Client:
    """Client to use Inspirehep API.
    """

    REST_API_URL = 'https://inspirehep.net/api/'

    SEARCH_RESULT_KEY = 'hits'

    IDENTIFIER_TYPES = [
        'literature',
        'authors',
        'institutions',
        'conferences',
        'seminars',
        'journals',
        'jobs',
        'experiments',
        'data',
        ]

    EXTERNAL_IDENTIFIER_TYPES = [
        'doi',
        'arxiv',
        'orcid',
        ]

    LIMIT_TIME = 5
    

    def __init__(self) -> None:
        self.session = self._init_session()

    def _init_session(self) -> requests.session:
        """Initialize session.
        """

        session = requests.session()
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'pyinspirehep',
            'Content-Type': 'application/json',
            }
        session.headers.update(headers)
        return session

    def wait_429(self) -> None:
        """
        Use to wait `LIMIT_TIME` seconds before sending new requests.
        """
        time.sleep(self.LIMIT_TIME)

    def _get(self, *args, **kwargs) -> dict:
        """Sends a GET request and returns json data.

        This method uses `requests.get` method to get data from API and
        and returns data as json.

        Parameters
        ----------
        *args :
            
        **kwargs :
            

        Returns
        -------
        dict
            Result of json data will be returned as Python dict.

        Raises
        ------
        InspirehepPIDDoesNotExistError
            When the requested object was not found
        InspirehepTooManyRequestsError
            When because of too many request the IP is blocked for
            a few seconds.

        """
        response = requests.get(*args, **kwargs)
        data = response.json()
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise InspirehepPIDDoesNotExistError(
                data.get('message', '404 status code'),
                )
        elif response.status_code == 429:
            raise InspirehepTooManyRequestsError(
                data.get('message', '429 status code'),
                )

    def _get_record(
        self,
        identifier_type: str,
        identifier_value: str,
        ) -> dict:
        """

        Parameters
        ----------
        identifier_type : str
            The `identifier-value` is a number identifying the given record
            in the INSPIRE database (also called record ID or recid)
            
        identifier_value : str


        Returns
        -------
        dict

        """
        args = [self.REST_API_URL, identifier_type, identifier_value]
        return self._get(Client._create_uri(*args))

    def _create_q(
        metadata_field: str,
        nested_key: str = None,
        value: str = "",
        ) -> str:
        """Creates query to use in URL for a field

        Parameters
        ----------
        metadata_field : str
            
        nested_key : str
             (Default value = None)
        value : str
             (Default value = "")

        Returns
        -------
        str

        """
        if nested_key is None:
            return f"{metadata_field}:{value}"
        else:
            return f"{metadata_field}.{nested_key}:{value}"

    def _search(
        self,
        identifier_type: str,
        **kwargs,
        ) -> dict:
        """

        Parameters
        ----------
        identifier_type : str
            
        **kwargs :
            

        Returns
        -------

        """
        args = [self.REST_API_URL, identifier_type]
        return self._get(
            Client._create_uri(*args),
            params=Client._create_params(**kwargs),
            )

    def _get_record_object(
        self,
        identifier_type: str,
        identifier_value: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        identifier_type : str
            
        identifier_value : str
            

        Returns
        -------
        SingleRecrodResponse

        """
        return SingleRecordResponse.from_response(
            self._get_record(identifier_type, identifier_value),
            )

    @staticmethod
    def _create_params(
        sorting: str = None,
        page: str = None,
        size: str = None,
        q: str = None,
        fields: str = None,
        ) -> dict:
        """

        Parameters
        ----------
        sorting : str
            (Default value = None). Determines the sort roder of objects
            in response.
        page : str
            (Default value = None). The page number to get in query.
        size : str
            (Default value = None). The number of records in page.
        q : str
            (Default value = None). The search query.
        fields : str
            (Default value = None). The field in the metadata to be
            included in respone.

        Returns
        -------
        dict

        """
        params = {}
        if sorting is not None:
            params['sort'] = sorting  # The sort order
        if page is not None:
            params['page'] = page  # The page number
        if size is not None:
            params['size'] = size  # The number of results returned per page
        if q is not None:
            params['q'] = q  # The search query
        if fields is not None:
            params['fields'] = fields  # The fields in the metadata to be returned
        return params

    @staticmethod
    def _create_uri(*args, end: str = "") -> str:
        """

        Parameters
        ----------
        *args :
            
        end : str
            (Default value = "")

        Returns
        -------
        str

        """
        assert end in ("", "/")
        return "/".join(args) + end

    def get_literature(
        self,
        literature_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        literature_id : str
            

        Returns
        -------
        dict


        >>> client = Client()
        >>> paper = client.get_literature("451647")
        >>> paper["metadata"]["titles"][0]["title"]
        'The Large N limit of superconformal field theories and supergravity'
        """
        return self._get_record('literature', literature_id)

    def get_literature_object(
        self,
        literature_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        literature_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_literature(literature_id),
            )

    def get_author(
        self,
        author_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        author_id : str
            

        Returns
        -------
        dict

        """
        return self._get_record('authors', author_id)

    def get_author_object(
        self,
        author_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        author_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self._get_author(author_id),
            )

    def search_authors(
        self,
        sorting='bestmatch',
        size=1,
        page=1,
        fields=None,
        *,
        q=None,
        name=None,
        ) -> dict:
        """

        Parameters
        ----------
        sorting :
             (Default value = 'bestmatch')
        size :
             (Default value = 1)
        page :
             (Default value = 1)
        fields:
            (Default value = None)
        q :
             (Default value = None)
        name :
             (Default value = None)

        Returns
        -------
        dict

        """
        if name is not None:
            q = Client._create_q('name', 'value', name)
        return self._search(
            'authors',
            sorting=sorting,
            size=size,
            page=page,
            q=q,
            fields=fields,
            )

    def get_institution(
        self,
        institution_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        institution_id : str
            

        Returns
        -------
        dict

        """
        return self._get_record('authors', institution_id)

    def get_institution_object(
        self,
        institution_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        institution_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self._get_author(institution_id),
            )

    def get_conference(
        self,
        conference_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        conference_id : str
            

        Returns
        -------
        dict

        """
        return self._get_record('conferences', conference_id)

    def get_conference_object(
        self,
        conference_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        conference_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_conference(conference_id),
            )

    def get_seminar(
        self,
        seminar_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        seminar_id : str
            

        Returns
        -------
        dict

        """
        return self._get_record('seminars', seminar_id)

    def get_seminar_object(
        self,
        seminar_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        seminar_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_seminar(seminar_id),
            )

    def get_journal(
        self,
        journal_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        journal_id : str
            

        Returns
        -------
        dict

        """
        return self._get_record('journals', journal_id)

    def get_journal_object(
        self,
        journal_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        journal_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_journal_object(journal_id),
            )

    def get_job(
        self,
        job_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        job_id : str
            

        Returns
        -------
        dict

        """
        return self._get_record('jobs', job_id)

    def get_job_object(
        self,
        job_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        job_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_job(job_id)
            )

    def get_experiment(
        self,
        experiment_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        experiment_id : str
            

        Returns
        -------
        dict

        """
        return self._get_record('experiments', experiment_id)

    def get_experiment_object(
        self,
        experiment_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        experiment_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_experiment(experiment_id),
            )

    def get_data(
        self,
        data_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        data_id : str
            

        Returns
        -------
        dict

        """
        return self._get_record('data', data_id)

    def get_data_object(
        self,
        data_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        data_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_data(data_id),
            )

    def get_doi(
        self,
        doi_identifier: str,
        ) -> dict:
        """

        Parameters
        ----------
        doi_identifier : str
            

        Returns
        -------
        dict

        >>> client = Client()
        >>> literature_record = client.get_doi("10.1103/PhysRevLett.19.1264")
        >>> literature_record["metadata"]["titles"][-1]["title"]
        'A Model of Leptons'
        """
        return self._get_record('doi', doi_identifier)

    def get_doi_object(
        self,
        doi_identifier: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        doi_identifier : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_doi(doi_identifier),
            )

    def get_arxiv(
        self,
        arxiv_identifier: str,
        ) -> dict:
        """

        Parameters
        ----------
        arxiv_identifier : str
            

        Returns
        -------
        dict

        >>> client = Client()
        >>> literature_record = client.get_arxiv("1207.7214")
        >>> literature_record["metadata"]['titles'][-1]['title']
        'Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC'
        >>> literature_record["metadata"]['titles'][-1]['source']
        'arXiv'
        >>> literature_record = client.get_arxiv("hep-ph/0603175")
        >>> literature_record["metadata"]['titles'][-1]['source']
        'arXiv'
        """
        return self._get_record('arxiv', arxiv_identifier)

    def get_arxiv_object(
        self,
        arxiv_identifier: str,
        ) -> dict:
        """

        Parameters
        ----------
        arxiv_identifier : str
            

        Returns
        -------
        SingleRecordResponse
        
        """
        return SingleRecordResponse.from_response(
            self.get_arxiv(arxiv_identifier),
            )

    def get_orcid(
        self,
        orcid_id: str,
        ) -> dict:
        """

        Parameters
        ----------
        orcid_id : str
            

        Returns
        -------
        dict


        >>> client = Client()
        >>> author_record = client.get_orcid("0000-0003-3897-046X")
        >>> author_record["metadata"]["name"]["value"]
        'Seiberg, Nathan'
        """
        return self._get_record('orcid', orcid_id)

    def get_orcid_object(
        self,
        orcid_id: str,
        ) -> SingleRecordResponse:
        """

        Parameters
        ----------
        orcid_id : str
            

        Returns
        -------
        SingleRecordResponse

        """
        return SingleRecordResponse.from_response(
            self.get_orcid(orcid_id),
            )


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
