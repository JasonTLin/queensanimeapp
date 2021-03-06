import requests
from ..errors import *
from .helpers import SearchWrapper


class KitsuManga:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def get(self, aid):
        """
        Get manga information by id.

        :param int aid: ID of the manga.
        :return: Dictionary or None (for not found)
        :rtype: Dictionary or None
        :raises: :class:`Pymoe.errors.ServerError`
        """
        r = requests.get(self.apiurl + "/manga/{}".format(aid), headers=self.header)

        if r.status_code != 200:
            if r.status_code == 404:
                return None
            else:
                raise ServerError

        return r.json()

    def search(self, term):
        """
        Search for manga by term.

        :param str term: What to search for.
        :return: The results as a SearchWrapper iterator.
        :rtype: SearchWrapper
        """
        r = requests.get(self.apiurl + "/manga", params={"filter[text]": term}, headers=self.header)
        
        if r.status_code != 200:
            raise ServerError
        
        jsd = r.json()

        if jsd['meta']['count']:
            return SearchWrapper(jsd['data'], jsd['links']['next'] if 'next' in jsd['links'] else None, self.header)
        else:
            return None