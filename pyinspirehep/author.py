"""
Module for authors repsone of Inspirehep

The moduel provided a data class with serveral get methods
to make it easy to get authors information from the response of 
a request to Inspire hep API for author record.

"""

import datetime
from dataclasses import dataclass
from typing import List
from pyinspirehep.utils import (
    convert_json_timestamp,
    convert_to_bool,
    convert_to_date,
)
from .data_models import SingleRecordResponse


@dataclass
class AuthorMetadata:
    """Author Metadata according to Inspirehep API.
    """
    project_membership: List[dict] = None
    positions: List[dict] = None
    advisors: List[dict] = None
    email_addresses: List[dict] = None
    ids: List[dict] = None
    name: dict = None
    stub: bool = None
    status: str = None
    schema: str = None
    deleted: bool = None
    control_number: int = None
    legacy_version: str = None
    arxiv_categories: List[str] = None
    legacy_creation_date: datetime.datetime = None

    @classmethod
    def from_dict(cls, metadata: dict = None):
        if metadata is None:
            return AuthorMetadata()
        legacy_creation_date = convert_to_date(
            metadata.get("legacy_creation_date", None),
        )
        return AuthorMetadata(
            project_membership=metadata.get("project_membership", None),
            positions=metadata.get("positions", None),
            advisors=metadata.get("advisors", None),
            email_addresses=metadata.get("email_addresses", None),
            ids=metadata.get("ids", None),
            name=metadata.get("name", None),
            stub=convert_to_bool(metadata.get("stub", None)),
            status=metadata.get("status", None),
            schema=metadata.get("$schema", None),
            deleted=convert_to_bool(metadata.get("deleted", None)),
            control_number=int(metadata.get("control_number", None)),
            legacy_version=metadata.get("legacy_version", None),
            arxiv_categories=metadata.get("arxiv_categories", None),
            legacy_creation_date=legacy_creation_date,
        )


@dataclass
class Author(SingleRecordResponse):
    """Class to contain Inspirehep API single record response for Author.

    Attribtes
    ---------
    id : str
        The unique identifier of the object.

    created : datetime.datetime
        The UTC timestamp when object was created.

    updated : datetime.datetime
        The UTC timestamp when object was las updated.

    links : dict
        List of related links to current object.

    metadata : AuthorMetadata
        Information about the Author which is an instance AuthorMetadata object.

    """
    id: str
    created: datetime.datetime = None
    updated: datetime.datetime = None
    links: dict = None
    metadata: AuthorMetadata = None

    @classmethod
    def from_response(cls, respone: dict):
        """

        Parameters
        ----------
        respone : dict
            

        Returns
        -------
        SingleRecordResponse

        """
        id = respone.get("id", None)
        created = convert_json_timestamp(
            respone.get("created", None),
        )
        updated = convert_json_timestamp(
            respone.get("updated", None),
        )
        links = respone.get("links", {})
        metadata = respone.get("metadata", {})
        metadata = AuthorMetadata.from_dict(metadata)
        return Author(
            id=id,
            created=created,
            updated=updated,
            links=links,
            metadata=metadata,
        )

    @property
    def name(self):
        """Returns then `name` dict of `self.metadata`

        """
        return self.metadata.name

    @property
    def positions(self):
        """Returns the `positions` list of `self.metadata`

        """
        return self.metadata.positions

    def get_name(self):
        """Returns full name of the author.
        
        """
        return self.name.get("value", None)

    def get_names_native(self):
        """Returns the native name of the author if exists.
        
        """
        return self.name.get("native_names", None)

    def get_name_preferred(self):
        """Returns the preferred name of the author if exists.
        
        """
        return self.name.get("preferred_name", None)

    def get_number_of_positions(self):
        """Returns number of all of the positions the author has had.

        """
        if self.positions:
            return len(self.positions)
        else:
            return 0

    @property
    def email_addresses(self):
        return self.metadata.email_addresses

    def get_email_addresses(self):
        """Returns list of all email address of the author.
        
        """
        if self.email_addresses:
            return [email_info.get("value", None) for email_info in self.email_addresses]
        else:
            return None

    def get_email_current(self):
        """Returns the current email address
        
        Warning:
        The function will return the first email address which has current: True.

        """
        for email in self.email_addresses:
            if email.get("current", None):
                return email.get("value", None)
        return None

    @property
    def ids(self):
        return self.metadata.ids

    def get_id_orcid(self):
        """Returns orcid id of the author if exists
        
        """
        for id_ in self.ids:
            if id_.get('schema', None).upper() == 'ORCID':
                return id_.get("value", None)
        return None

    def get_id_cern(self):
        """Returns CERN id of the author if exists
        
        """
        for id_ in self.ids:
            if id_.get('schema', None).upper() == 'CERN':
                return id_.get("value", None)
        return None

    def get_id_linkedin(self):
        """Returns Linkedin id of the author if exists
        
        """
        for id_ in self.ids:
            if id_.get('schema', None).upper() == 'LINKEDIN':
                return id_.get("value", None)
        return None

    def get_id_linkedin(self):
        """Returns Linkedin id of the author if exists
        
        """
        for id_ in self.ids:
            if id_.get('schema', None).upper() == 'LINKEDIN':
                return id_.get("value", None)
        return None

    def get_id_inspire_bai(self):
        """Returns INSPIRE BAI of the author if exists
        
        """
        for id_ in self.ids:
            if id_.get('schema', None).upper() == 'INSPIRE BAI':
                return id_.get("value", None)
        return None

    def get_id_inspire_id(self):
        """Returns INSPIRE ID of the author if exists
        
        """
        for id_ in self.ids:
            if id_.get('schema', None).upper() == 'INSPIRE ID':
                return id_.get("value", None)
        return None

    @property
    def arxiv_categories(self):
        """Returns the `arxiv_categories` list of `self.metadata`

        """
        return self.metadata.arxiv_categories

    def get_arxiv_categories(self):
        """Returns list of arxiv categories of the author

        """
        return self.arxiv_categories

    @property
    def control_number(self):
        """Returns the `control_number` of `self.metadata`
        
        """
        return self.metadata.control_number

    def get_id(self, as_int=False):
        """Returns the author id in INSPIRE HEP
        
        """
        return self.control_number if as_int else str(self.control_number)

    @property
    def project_membereship(self):
        """Returns the 'proejct_membership' of `self.metadata`
        
        """
        return self.metadata.project_membership

    def get_project_memberships(self, current=False):
        """Returns the project memberships of the authors.
        

        Parameters
        ----------
        current : bool
            If current is True only current project memberships will be 
            returned. Else, all project memeberships will be returned.
        
        
        Returns
        -------
        list
            list of string which shows the proejct memberships.
        
        """
        if current:
            memberships = [project["name"]
                           for project in self.project_membereship if project['current'] == True]
        else:
            memberships = [project["name"]
                           for project in self.project_membereship]
        return memberships if memberships else None

    def get_project_memberships_ids(self, current=False):
        """Returns the project memberships ids of the authors.
        

        Parameters
        ----------
        current : bool
            If current is True only current project memberships will be 
            returned. Else, all project memeberships will be returned.
        

        Returns
        -------
        list
            list of string which shows the proejct memberships.
        
        """
        if current:
            memberships = [project["record"]['$ref'].split(
                "/")[-1] for project in self.project_membereship if project['current'] == True]
        else:
            memberships = [project["record"]['$ref'].split(
                "/")[-1] for project in self.project_membereship]
        return memberships if memberships else None

    @property
    def advisors(self):
        """Returns the `advisors` of `self.metadata`
        
        """
        return self.metadata.advisors

    def get_advisors(self):
        """Returns the advisors of the authors
        
        """
        return [advisor['name'] for advisor in self.advisors]

    def get_advisors_id(self):
        """Returns the inspire hep if of advisors of the author
        
        """
        return [advisor['record']['$ref'].split("/")[-1] for advisor in self.advisors]

    @property
    def positions(self):
        """Returns 'position' attribute of `self.metadata`

        """
        return self.metadata.positions

    def get_institutions(self):
        """Returns name of institutions of the author

        """
        return [position.get("institution", None) for position in self.positions]

    def get_institutions_ids(self):
        """Returns ids of institutions of the author

        """
        return [position["record"]["$ref"].split("/")[-1] for position in self.positions]

    def get_positions(self):
        """Returns dict of positions of the authors
        """
        return self.positions
