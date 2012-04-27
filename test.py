import unittest

import bottle

import bottle_agamemnon
from agamemnon.factory import DataStore
class AgamemnonPluginTest(unittest.TestCase):

    def setUp(self):
        self.app = bottle.Bottle(catchall=False)


    def test_with_keyword(self):
        self.plugin = self.app.install(bottle_agamemnon.Plugin())

        @self.app.get('/')
        def test(agadb):
            self.assertEqual(type(agadb), DataStore)
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)

    def test_without_keyword(self):
        self.plugin = self.app.install(bottle_agamemnon.Plugin())

        @self.app.get('/')
        def test():
            pass
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)

        @self.app.get('/2')
        def test_kw(**kw):
            self.assertFalse('agadb' in kw)
        self.app({'PATH_INFO':'/2', 'REQUEST_METHOD':'GET'}, lambda x, y: None)

if __name__ == '__main__':
    unittest.main()
