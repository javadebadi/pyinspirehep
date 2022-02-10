"""
A module to get all information from Inspirehep API.
"""

import os
import json
from tabnanny import verbose
from pyinspirehep.client import Client


class LiteratureClone:
    """Class to clone Literature Information.

    Example:
    >>> import os
    >>> from pathlib import Path
    >>> from pyinspirehep.contrib.clone import LiteratureClone
    >>> directory = os.path.join(Path.home(), "Desktop", "literature")
    >>> cloner = LiteratureClone(directory)
    >>> cloner.clone(0,1000,1000)
    current collection size = 478
    current collection size = 976
    ----------------------------------------------->
    Saving json file number = 1000
    -----------------------------------------------<
    >>> assert os.path.isfile(os.path.join(directory,"1000.json"))
    """

    def __init__(
        self,
        directory=None,
        record_numbers=500,
        verbose=2,
        ) -> None:
        """
        Parameters
        ----------
        directory : str or path
            Determines the directory to save the json files during clone
        record_numbers : int
            (Default value 500)
            The number of records per page
        verbose : int
            (Default value 2)
            Determines the amount of information to be printed during clone.
            When it is 2 the maximum inofrmation will be printed.
        """
        if directory is None:
            raise ValueError("You must determine the directory name to save cloned data")
        self.collection = []
        self.client = Client()
        self.record_numbers = record_numbers
        self.verbose = verbose
        self.directory = directory
        if os.path.isdir(self.directory):
            pass
        else:
            self.directory = os.makedirs(self.directory)

    def clean(self) -> None:
        self.collection = []

    def save(self, filename: str) -> None:
        """Writes content to json file.

        Parameters
        ----------
        filename : str
            (Default value = None)

        Returns
        -------
        None

        """
        filename = os.path.join(self.directory, filename)
        with open(filename, 'w') as f:
            json.dump(self.collection, f)

    def _get_by_control_number(self, start) -> list:
        """Gets literatures list by using control number field.

        Parameters
        ----------
        start : int

        Returns
        -------
        List
            list of all literatures by control_number between `start` and
            `start` + `self.record_number`.
        """
        return self.client.search_literature(
            q=f'control_number:{start}->{start+self.record_numbers}',
            size=self.record_numbers,
            )['hits']['hits']

    def clone(
        self,
        min_control_number=0,
        max_control_number=2000000,
        batch_record_number=10000,
        ):
        """Clones all literature data in given interval.

        Parameters
        ----------
        min_control_number : int
            The minimum control number to start cloning from
        max_control_number : int
            The maximum control number to stop further cloning
        batch_record_number : int
            (Default 10000)
            When the control numbers modolue to `batch_record_number`
            is 0 it will be saved in hard disc and the `self.collection`
            will be cleared.
        
        """
        for start in range(
            min_control_number,
            max_control_number,
            self.record_numbers
            ):
            current_records = self._get_by_control_number(start)
            self.collection.extend(current_records)
            if self.verbose >= 2:
                print(f"current collection size = {len(self.collection)}")
            if (start + self.record_numbers) % batch_record_number == 0:
                if self.verbose >=1:
                    print("----------------------------------------------->")
                    print(f"Saving json file number = {start + self.record_numbers}")
                self.save(str(start + self.record_numbers)+".json")
                if self.verbose >= 1:
                    print("-----------------------------------------------<")
                self.clean()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
