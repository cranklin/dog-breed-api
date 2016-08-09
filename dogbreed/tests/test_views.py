import os
import dogbreed
import unittest
import json
from mock import patch, Mock
from dogbreed.actions import Actions
from dogbreed.exceptions import *
from flask import render_template

class ViewsTest(unittest.TestCase):

    def setUp(self):
        self.app = dogbreed.app.test_client()

    def test_index(self):
        resp = self.app.get('/')
        self.assertEquals(resp.status_code, 200)

        resp = self.app.get('/index')
        self.assertEquals(resp.status_code, 200)

        resp = self.app.get('/api')
        self.assertEquals(resp.status_code, 200)

    def test_not_found_error(self):
        resp = self.app.get('/blahblah')
        self.assertEquals(resp.data, 'Not Found')
        self.assertEquals(resp.status, '404 NOT FOUND')
        self.assertEquals(resp.status_code, 404)

    def test_get_all_dogs(self):
        with patch.object(Actions, 'get_all_dogs', return_value=[]) as patched_get_all_dogs:
            resp = self.app.get('/api/dogs')

            patched_get_all_dogs.assert_called_once_with(order_by=None)

    def test_get_all_dogs_order_by_breed(self):
        with patch.object(Actions, 'get_all_dogs', return_value=[]) as patched_get_all_dogs:
            resp = self.app.get('/api/dogs?order_by=breed')

            patched_get_all_dogs.assert_called_once_with(order_by='breed')

    def test_get_all_dogs_order_by_votes(self):
        with patch.object(Actions, 'get_all_dogs', return_value=[]) as patched_get_all_dogs:
            resp = self.app.get('/api/dogs?order_by=votes')

            patched_get_all_dogs.assert_called_once_with(order_by='votes')

    def test_get_dog(self):
        with patch.object(Actions, 'get_dog', return_value=[]) as patched_get_dog:
            resp = self.app.get('/api/dogs/10')

            patched_get_dog.assert_called_once_with('10')

    def test_get_all_dog_breeds(self):
        with patch.object(Actions, 'get_all_breeds', return_value=[]) as patched_get_all_breeds:
            resp = self.app.get('/api/breeds')

            patched_get_all_breeds.assert_called_once()

    def test_get_all_breed(self):
        with patch.object(Actions, 'get_all_dogs_by_breed', return_value=[]) as patched_get_all_dogs_by_breed:
            resp = self.app.get('/api/breeds/2')

            patched_get_all_dogs_by_breed.assert_called_once_with('2')

    def test_post_dog_vote_success(self):
        with patch.object(Actions, 'submit_dog_vote', return_value={'vote': 1}) as patched_submit_dog_vote:
            resp = self.app.post('/api/dogs/vote', data=json.dumps(dict(dog=10)), content_type = 'application/json', headers={'User-Agent': 'fake_user_agent'})

            patched_submit_dog_vote.assert_called_once_with(10, 'fake_user_agent')
            self.assertEquals(resp.data, '{\n  "vote": 1\n}\n')
            self.assertEquals(resp.status_code, 201)

    def test_post_dog_vote_fail_one(self):
        with patch.object(Actions, 'submit_dog_vote', side_effect=NotAllowed("User already voted", status_code=403)) as patched_submit_dog_vote:
            resp = self.app.post('/api/dogs/vote', data=json.dumps(dict(dog=10)), content_type = 'application/json', headers={'User-Agent': 'fake_user_agent'})

            patched_submit_dog_vote.assert_called_once_with(10, 'fake_user_agent')
            self.assertEquals(resp.data, '{\n  "message": "User already voted"\n}\n')
            self.assertEquals(resp.status_code, 403)

    def test_post_dog_vote_fail_two(self):
        with patch.object(Actions, 'submit_dog_vote') as patched_submit_dog_vote:
            resp = self.app.post('/api/dogs/vote', data=json.dumps(dict()), content_type = 'application/json', headers={'User-Agent': 'fake_user_agent'})

            self.assertEquals(patched_submit_dog_vote.call_count, 0)
            self.assertEquals(resp.data, '{\n  "message": "Required parameter(s) missing: dog"\n}\n')
            self.assertEquals(resp.status_code, 400)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
