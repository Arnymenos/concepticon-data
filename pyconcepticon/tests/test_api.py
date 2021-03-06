# coding: utf8
from __future__ import unicode_literals, print_function, division

from clldutils.testing import capture

from pyconcepticon.tests.util import TestWithFixture


class Tests(TestWithFixture):
    def test_Concept(self):
        from pyconcepticon.api import Concept

        d = {f: '' for f in Concept.public_fields()}
        with self.assertRaises(ValueError):
            Concept(**d)

        d['id'] = 'i'
        with self.assertRaises(ValueError):
            Concept(**d)

        d['number'] = 'i'
        with self.assertRaises(ValueError):
            Concept(**d)

        d['number'] = '1b'
        with self.assertRaises(ValueError):
            Concept(**d)

        d['gloss'] = 'g'
        Concept(**d)

    def test_Conceptset(self):
        from pyconcepticon.api import Conceptset

        d = {a: '' for a in Conceptset.public_fields()}
        d['semanticfield'] = 'xx'
        with self.assertRaises(ValueError):
            Conceptset(**d)

    def test_map(self):
        from pyconcepticon.api import Concepticon

        api = Concepticon()
        if api.repos.exists():
            with capture(api.map, self.fixture_path('conceptlist.tsv')) as out:
                self.assertIn('CONCEPTICON_ID', out)

            self.assertGreater(len(api.conceptsets['217'].concepts), 8)

    def test_Conceptlist(self):
        from pyconcepticon.api import Conceptlist

        clist = Conceptlist.from_file(self.fixture_path('conceptlist.tsv'))
        self.assertEqual(len(clist.concepts), 1)

    def test_Reference(self):
        from pyconcepticon.api import Reference

        with self.assertRaises(ValueError):
            Reference(id=1, type='misc', record={})

        Reference(id=1, type='misc', record={'author': 'a', 'title': 't', 'year': 'y'})

    def test_Concepticon(self):
        from pyconcepticon.api import Concepticon
        con = Concepticon()
        assert len(con.frequencies) <= len(con.conceptsets)
