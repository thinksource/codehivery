import os

import unittest
import tempfile
import codecs
from main import create_app, loadjson
import json
from api import JSON_WRONGCOMP
# from api import api
class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        # self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()

        self.app = create_app()
        self.app.testing = True
        self.client=self.app.test_client()

    def test_empty(self):
        rv = self.client.get('/api/')
        assert b'The service is working' in rv.data

    def test_company1(self):
        rv = self.client.get('/api/company/NETBOOK')
        assert len(json.loads(rv.data)) == 0

    def test_company2(self):
        rv = self.client.get('/api/company/EARGO')
        jdata=json.loads(rv.data)
        assert len(jdata) == 13
        assert jdata[1]['email'] == "evangelinasharp@earthmark.com"

    def test_company3(self):
        rv = self.client.get('/api/company/EARGO11')
        jdata=json.loads(rv.data)
        assert len(jdata) == 1
        assert jdata == JSON_WRONGCOMP

    def test_commonid(self):
        rv = self.client.get('/api/commonid/0/3')
        jdata=json.loads(rv.data)
        assert len(jdata) == 1
        assert jdata[0] == "Decker Mckenzie"

    def test_user1(self):
        rv=self.client.get('/api/user/Decker%20Mckenzie')
        jdata=json.loads(rv.data)
        assert len(jdata['fruits']) == 0
        assert len(jdata['vegetables']) ==4

    def test_common(self):
        jsonreq=loadjson(self.app, 'samplerequest2.json')
        rv=self.client.post('/api/common', data=json.dumps(jsonreq),content_type='application/json')
        jdata=json.loads(rv.data)
        assert len(jdata) == 2
        assert jdata[0]['email'] == "deckermckenzie@earthmark.com"
        assert jdata[1]['email'] =="mindybeasley@earthmark.com"

def runtest():
    unittest.main()

if __name__ == '__main__':
    runtest()
