import unittest
from mock import patch, Mock
from dogbreed.actions import Actions
from dogbreed.models import *
from dogbreed.exceptions import *

class ActionsTest(unittest.TestCase):

    def setUp(self):
        self.mock_db_query = Mock(name="query")
        self.mock_db_join = Mock(name="join")
        self.mock_db_outerjoin = Mock(name="outerjoin")
        self.mock_db_options = Mock(name="options")
        self.mock_db_filter_by = Mock(name="filter_by")
        self.mock_db_order_by = Mock(name="order_by")

    def test_get_all_dogs(self):
        mock_dog_one = Mock(Dog)
        mock_dog_one_data = {
            'date_modified': None,
            'dog_description': None,
            'breed_id': 1,
            'date_created': None,
            'dog_name': None,
            'id': 1,
            'photo_url': u'http://i.imgur.com/eE29vX4.png'
        }
        mock_dog_one.as_dict.return_value = mock_dog_one_data

        mock_dog_two = Mock(Dog)
        mock_dog_two_data = {
            'date_modified': None,
            'dog_description': None,
            'breed_id': 1,
            'date_created': None,
            'dog_name': None,
            'id': 2,
            'photo_url': u'http://i.imgur.com/xX2AeDR.png'
        }
        mock_dog_two.as_dict.return_value = mock_dog_two_data

        with patch.object(Dog, 'query', autospec=True) as patched_dog_query:
            patched_dog_query.all.return_value = [mock_dog_one, mock_dog_two]

            resp = Actions.get_all_dogs()

            patched_dog_query.all.assert_called_once()

            self.assertEquals(len(resp), 2)
            self.assertEquals(resp, [mock_dog_one_data, mock_dog_two_data])

    def test_get_all_dogs_grouped_by_breed(self):
        mock_dog_one = Mock(Dog)
        mock_dog_one_data = {
            'date_modified': None,
            'dog_description': None,
            'breed_id': 1,
            'date_created': None,
            'dog_name': None,
            'id': 1,
            'photo_url': u'http://i.imgur.com/eE29vX4.png'
        }
        mock_dog_one.as_dict.return_value = mock_dog_one_data

        mock_dog_two = Mock(Dog)
        mock_dog_two_data = {
	    "date_modified": None,
	    "dog_description": None,
            "breed_id": 4,
	    "date_created": None,
	    "dog_name": None,
	    "id": 90,
	    "photo_url": "http://i.imgur.com/qWLKy8a.jpg"
	}
        mock_dog_two.as_dict.return_value = mock_dog_two_data

        with patch.object(db.session, 'query', autospec=True) as patched_db_session_query:

            patched_db_session_query.return_value = self.mock_db_query
            self.mock_db_query.join.return_value = self.mock_db_join
            self.mock_db_join.outerjoin.return_value = self.mock_db_outerjoin
            self.mock_db_outerjoin.options.return_value = self.mock_db_options
            self.mock_db_options.order_by.return_value = self.mock_db_order_by
            self.mock_db_order_by.all.return_value = [mock_dog_one, mock_dog_two]

            resp = Actions.get_all_dogs(order_by='breed')

            patched_db_session_query.assert_called_once_with(Dog)
            self.mock_db_query.join.assert_called_once_with(Breed)
            self.mock_db_join.outerjoin.assert_called_once_with(Vote)
            self.mock_db_outerjoin.options.assert_called_once()
            self.mock_db_options.order_by.assert_called_once()
            self.mock_db_order_by.all.assert_called_once()

            self.assertEquals(len(resp), 2)
            self.assertEquals(resp, [mock_dog_one_data, mock_dog_two_data])

    def test_get_all_dogs_grouped_by_vote(self):
        mock_dog_one = Mock(Dog)
        mock_dog_one_data = {
            'date_modified': None,
            'dog_description': None,
            'breed_id': 1,
            'date_created': None,
            'dog_name': None,
            'id': 1,
            'photo_url': u'http://i.imgur.com/eE29vX4.png'
        }
        mock_dog_one.as_dict.return_value = mock_dog_one_data

        mock_dog_two = Mock(Dog)
        mock_dog_two_data = {
	    "date_modified": None,
	    "dog_description": None,
            "breed_id": 4,
	    "date_created": None,
	    "dog_name": None,
	    "id": 90,
	    "photo_url": "http://i.imgur.com/qWLKy8a.jpg"
	}
        mock_dog_two.as_dict.return_value = mock_dog_two_data

        with patch.object(db.session, 'query', autospec=True) as patched_db_session_query:

            patched_db_session_query.return_value = self.mock_db_query
            self.mock_db_query.join.return_value = self.mock_db_join
            self.mock_db_join.outerjoin.return_value = self.mock_db_outerjoin
            self.mock_db_outerjoin.options.return_value = self.mock_db_options
            self.mock_db_options.order_by.return_value = self.mock_db_order_by
            self.mock_db_order_by.all.return_value = [mock_dog_one, mock_dog_two]

            resp = Actions.get_all_dogs(order_by='votes')

            patched_db_session_query.assert_called_once_with(Dog)
            self.mock_db_query.join.assert_called_once_with(Breed)
            self.mock_db_join.outerjoin.assert_called_once_with(Vote)
            self.mock_db_outerjoin.options.assert_called_once()
            self.mock_db_options.order_by.assert_called_once()
            self.mock_db_order_by.all.assert_called_once()

            self.assertEquals(len(resp), 2)
            self.assertEquals(resp, [mock_dog_one_data, mock_dog_two_data])

    def test_get_dog_by_id(self):
        mock_dog_one = Mock(Dog)
        mock_dog_one_data = {
            'date_modified': None,
            'dog_description': None,
            'breed_id': 10,
            'date_created': None,
            'dog_name': None,
            'id': 1,
            'photo_url': u'http://i.imgur.com/eE29vX4.png'
        }
        mock_dog_one.as_dict.return_value = mock_dog_one_data

        with patch.object(Dog, 'query', autospec=True) as patched_dog_query:
            patched_dog_query.filter_by.return_value = self.mock_db_filter_by
            self.mock_db_filter_by.first.return_value = mock_dog_one

            resp = Actions.get_dog(10)

            patched_dog_query.filter_by.assert_called_once_with(id=10)
            self.mock_db_filter_by.first.assert_called_once()

            self.assertEquals(resp, mock_dog_one_data)

    def test_get_all_breeds(self):
        mock_breed_one = Mock(Breed)
        mock_breed_one_data = {
            "id": 1,
            "date_created": None,
            "dogs": None,
            "breed_name": "labrador",
            "date_modified": None
        }
        mock_breed_one.as_dict.return_value = mock_breed_one_data

        mock_breed_two = Mock(Breed)
        mock_breed_two_data = {
            "id": 2,
            "date_created": None,
            "dogs": None,
            "breed_name": "pug",
            "date_modified": None
        }
        mock_breed_two.as_dict.return_value = mock_breed_two_data

        with patch.object(Breed, 'query', autospec=True) as patched_breed_query:
            patched_breed_query.all.return_value = [mock_breed_one, mock_breed_two]

            resp = Actions.get_all_breeds()

            patched_breed_query.all.assert_called_once()

            self.assertEquals(len(resp), 2)
            self.assertEquals(resp, [mock_breed_one_data, mock_breed_two_data])

    def test_get_all_dogs_by_breeds(self):
        mock_dog_one = Mock(Dog)
        mock_dog_one_data = {
            'date_modified': None,
            'dog_description': None,
            'breed_id': 1,
            'date_created': None,
            'dog_name': None,
            'id': 1,
            'photo_url': u'http://i.imgur.com/eE29vX4.png'
        }
        mock_dog_one.as_dict.return_value = mock_dog_one_data

        mock_dog_two = Mock(Dog)
        mock_dog_two_data = {
            'date_modified': None,
            'dog_description': None,
            'breed_id': 1,
            'date_created': None,
            'dog_name': None,
            'id': 2,
            'photo_url': u'http://i.imgur.com/xX2AeDR.png'
        }
        mock_dog_two.as_dict.return_value = mock_dog_two_data

        with patch.object(Dog, 'query', autospec=True) as patched_dog_query:
            patched_dog_query.filter_by.return_value = self.mock_db_filter_by
            self.mock_db_filter_by.all.return_value = [mock_dog_one, mock_dog_two]

            resp = Actions.get_all_dogs_by_breed(1)

            patched_dog_query.filter_by.assert_called_once_with(breed_id=1)
            self.mock_db_filter_by.all.assert_called_once()

            self.assertEquals(len(resp), 2)
            self.assertEquals(resp, [mock_dog_one_data, mock_dog_two_data])

    def test_submit_dog_vote_success_one(self):
        with patch.object(Client, 'query', autospec=True) as patched_client_query, \
            patch.object(Vote, 'query', autospec=True) as patched_vote_query, \
            patch.object(db.session, 'add', autospec=True) as patched_db_session_add, \
            patch.object(db.session, 'commit', autospec=True) as patched_db_session_commit, \
            patch('dogbreed.db.Model', return_value=Mock()) as patched_db:

            patched_client_query.filter_by.return_value = self.mock_db_filter_by
            self.mock_db_filter_by.first.return_value = None
            patched_vote_query.filter_by.return_value = self.mock_db_filter_by

            resp = Actions.submit_dog_vote(1, "fake_user_agent")

            patched_client_query.filter_by.assert_called_once_with(client_name="fake_user_agent")
            self.assertEquals(self.mock_db_filter_by.first.call_count, 2)  # called for client and vote
            self.assertEquals(patched_db_session_add.call_count, 2)  # called for client and vote
            self.assertEquals(patched_db_session_commit.call_count, 2)  # called for client and vote

            self.assertEquals(resp, {'vote': 1})

    def test_submit_dog_vote_success_two(self):
        with patch.object(Client, 'query', autospec=True) as patched_client_query, \
            patch.object(Vote, 'query', autospec=True) as patched_vote_query, \
            patch.object(db.session, 'add', autospec=True) as patched_db_session_add, \
            patch.object(db.session, 'commit', autospec=True) as patched_db_session_commit, \
            patch('dogbreed.db.Model', return_value=Mock()) as patched_db:

            patched_client_query.filter_by.return_value = self.mock_db_filter_by
            vote_mock = Mock()
            vote_mock.counter = 5
            self.mock_db_filter_by.first.side_effect = [None, vote_mock]
            patched_vote_query.filter_by.return_value = self.mock_db_filter_by

            resp = Actions.submit_dog_vote(1, "fake_user_agent")

            patched_client_query.filter_by.assert_called_once_with(client_name="fake_user_agent")
            self.assertEquals(self.mock_db_filter_by.first.call_count, 2)  # called for client and vote
            self.assertEquals(patched_db_session_add.call_count, 1)  # called for client
            self.assertEquals(patched_db_session_commit.call_count, 2)  # called for client and vote

    def test_submit_dog_vote_failure(self):
        mock_client_one = Mock(Client)
        mock_client_one_data = {
            'date_modified': None,
            'date_created': None,
            'client_name': 'fake_user_agent',
            'id': 1
        }

        with patch.object(Client, 'query', autospec=True) as patched_client_query:
            patched_client_query.filter_by.return_value = self.mock_db_filter_by
            self.mock_db_filter_by.first.return_value = mock_client_one

            with self.assertRaises(NotAllowed):
                resp = Actions.submit_dog_vote(1, "fake_user_agent")

            patched_client_query.filter_by.assert_called_once_with(client_name="fake_user_agent")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
