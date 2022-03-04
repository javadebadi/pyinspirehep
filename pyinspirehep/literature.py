"""
Module for literature repsone of Inspirehep

The moduel provided a data class with serveral get methods
to make it easy to get literature information from the response of 
a request to Inspire hep API for literature record and
resulf of literature search.

"""

import datetime
from dataclasses import dataclass
from datetime import date
from typing import List
from pyinspirehep.utils import (
    convert_json_timestamp,
    convert_to_bool,
    convert_to_date,
)
from .data_models import SingleRecordResponse


@dataclass
class LiteratureMetadata:
    control_number: str
    abstracts: List[dict] = None
    arxiv_eprints: List[dict] = None
    authors: List[dict] = None
    author_count: int = None
    earliest_date: date = None
    citation_count: int = 0
    citation_count_without_self_citations: int = 0
    citeable: bool = None
    copyright: List[dict] = None
    core: bool = None
    curated: bool = None
    documents: List[dict] = None
    document_type: List[str] = None
    dois: List[dict] = None
    facet_author_name: List[str] = None
    figures: List[dict] = None
    first_author: List[dict] = None
    imprints: List[dict] = None
    inspire_categories: List[dict] = None
    keywords: List[dict] = None
    legacy_version: str = None
    legacy_creation_date: date = None
    license: List[dict] = None
    number_of_pages: int = 0
    preprint_date: date = None
    primary_arxiv_category: List[str] = None
    public_notes: List[dict] = None
    publication_info: List[dict] = None
    referenced_authors_bais: List[str] = None
    references: List[dict] = None
    refereed: bool = None
    schema: str = None
    texkeys: List[str] = None
    titles: List[dict] = None

    @classmethod
    def from_dict(cls, metadata: dict = None):
        if metadata is None:
            return LiteratureMetadata()
        legacy_creation_date = convert_to_date(
            metadata.get("legacy_creation_date", None),
        )
        earliest_date = convert_to_date(
            metadata.get("earliest_date", None)
        )
        preprint_date = convert_to_date(
            metadata.get("preprint_date", None)
        )
        return LiteratureMetadata(
            control_number=metadata["control_number"],
            abstracts=metadata.get("abstracts", None),
            arxiv_eprints=metadata.get("arxiv_eprints", None),
            authors=metadata.get("authors", None),
            author_count=metadata.get("author_count", None),
            earliest_date=earliest_date,
            citation_count=int(metadata.get("citation_count", 0)),
            citation_count_without_self_citations=metadata.get(
                "citation_count_without_self_citations", 0),
            citeable=convert_to_bool(metadata.get("citeable", None)),
            copyright=metadata.get("copyright", None),
            core=convert_to_bool(metadata.get("core", None)),
            curated=convert_to_bool(metadata.get("curated", None)),
            documents=metadata.get("documents", None),
            document_type=metadata.get("document_type", None),
            dois=metadata.get("dois", None),
            facet_author_name=metadata.get("facet_author_name", None),
            figures=metadata.get("figures", None),
            first_author=metadata.get("first_author", None),
            imprints=metadata.get("imprints", None),
            inspire_categories=metadata.get("inspire_categories", None),
            keywords=metadata.get("keywords", None),
            legacy_version=metadata.get("legacy_version", None),
            legacy_creation_date=legacy_creation_date,
            license=metadata.get("license", None),
            number_of_pages=metadata.get("number_of_pages", 0),
            preprint_date=preprint_date,
            primary_arxiv_category=metadata.get("primary_arxiv_category", 0),
            public_notes=metadata.get("public_notes", 0),
            publication_info=metadata.get("publication_info", 0),
            referenced_authors_bais=metadata.get("referenced_authors_bais", 0),
            references=metadata.get("references", 0),
            refereed=convert_to_bool(metadata.get("refereed", None)),
            schema=metadata.get("$schema", None),
            texkeys=metadata.get("texkeys", 0),
            titles=metadata.get("titles", 0),
        )


@dataclass
class Literature(SingleRecordResponse):
    """Class to contain Inspirehep API single record response for Literature.

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

    metadata : LiteratureMetadata
        Information about the Literature which is an instance LiteratureMetadata object.

    """
    id: str
    created: datetime.datetime = None
    updated: datetime.datetime = None
    links: dict = None
    metadata: LiteratureMetadata = None

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
        metadata = LiteratureMetadata.from_dict(metadata)
        return Literature(
            id=id,
            created=created,
            updated=updated,
            links=links,
            metadata=metadata,
        )

    def get_citation_count(self):
        return self.metadata.citation_count

    def get_references_ids(self):
        ids = []
        if self.metadata.references:
            for item in self.metadata.references:
                ids.append(item['record']['$ref'].split("/")[-1])
        return ids

