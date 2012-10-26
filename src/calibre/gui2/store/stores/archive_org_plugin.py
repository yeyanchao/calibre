# -*- coding: utf-8 -*-

from __future__ import (unicode_literals, division, absolute_import, print_function)

__license__ = 'GPL 3'
__copyright__ = '2011, John Schember <john@nachtimwald.com>'
__docformat__ = 'restructuredtext en'

from calibre.gui2.store.basic_config import BasicStoreConfig
from calibre.gui2.store.opensearch_store import OpenSearchOPDSStore
from calibre.gui2.store.search_result import SearchResult

class ArchiveOrgStore(BasicStoreConfig, OpenSearchOPDSStore):

    open_search_url = 'http://bookserver.archive.org/catalog/opensearch.xml'
    web_url = 'http://www.archive.org/details/texts'

    # http://bookserver.archive.org/catalog/

    def search(self, query, max_results=10, timeout=60):
        for s in OpenSearchOPDSStore.search(self, query, max_results, timeout):
            s.detail_item = 'http://www.archive.org/details/' + s.detail_item.split(':')[-1]
            s.price = '$0.00'
            s.drm = SearchResult.DRM_UNLOCKED
            yield s

    def get_details(self, search_result, timeout):
        '''
        The opensearch feed only returns a subset of formats that are available.
        We want to get a list of all formats that the user can get.
        '''
        from calibre import browser
        from contextlib import closing
        from lxml import html

        br = browser()
        with closing(br.open(search_result.detail_item, timeout=timeout)) as nf:
            idata = html.fromstring(nf.read())
            formats = ', '.join(idata.xpath('//p[@id="dl" and @class="content"]//a/text()'))
            search_result.formats = formats.upper()

        return True
