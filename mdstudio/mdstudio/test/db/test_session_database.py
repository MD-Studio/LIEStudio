# coding=utf-8
import unittest

from mock import mock

from mdstudio.db.session_database import SessionDatabaseWrapper
from mdstudio.db.sort_mode import SortMode


class SessionDatabaseWrapperTests(unittest.TestCase):

    def setUp(self):
        self.session = mock.Mock()
        self.session.component_info.get = mock.MagicMock(return_value='namespace')

        self.wrapper = SessionDatabaseWrapper(self.session)
        self.session.component_info.get.assert_called_once_with('namespace')

    def test_construction(self):

        self.assertEqual(self.wrapper.namespace, 'namespace')

    def test_more(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.more('123456')

        self.session.call.assert_called_once_with('mdstudio.db.more.namespace', {
            'cursorId': '123456'
        })

    def test_rewind(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.rewind('123456')

        self.session.call.assert_called_once_with('mdstudio.db.rewind.namespace', {
            'cursorId': '123456'
        })

    def test_insert_one(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.insert_one('col', {'test': 8})

        self.session.call.assert_called_once_with('mdstudio.db.insert_one.namespace', {
            'collection': 'col',
            'insert': {'test': 8}
        })

    def test_insert_one_date_fields(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.insert_one('col', {'test': 8}, ['field1', 'field2'])

        self.session.call.assert_called_once_with('mdstudio.db.insert_one.namespace', {
            'collection': 'col',
            'insert': {'test': 8},
            'fields': {
                'date': ['field1', 'field2']
            }
        })

    def test_insert_many(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.insert_many('col', [{'test': 8}, {'test4': 4}])

        self.session.call.assert_called_once_with('mdstudio.db.insert_many.namespace', {
            'collection': 'col',
            'insert': [{'test': 8}, {'test4': 4}]
        })

    def test_insert_many_date_fields(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.insert_many('col', [{'test': 8}, {'test4': 4}], ['field1', 'field2'])

        self.session.call.assert_called_once_with('mdstudio.db.insert_many.namespace', {
            'collection': 'col',
            'insert': [{'test': 8}, {'test4': 4}],
            'fields': {
                'date': ['field1', 'field2']
            }
        })

    def test_replace_one(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.replace_one('col', {'_id': 5}, {'test': 8})

        self.session.call.assert_called_once_with('mdstudio.db.replace_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 5},
            'replacement': {'test': 8},
            'upsert': False
        })

    def test_replace_one_upsert(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.replace_one('col', {'_id': 5}, {'test': 8}, upsert=True)

        self.session.call.assert_called_once_with('mdstudio.db.replace_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 5},
            'replacement': {'test': 8},
            'upsert': True
        })

    def test_replace_one_date_fields(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.replace_one('col', {'_id': 5}, {'test': 8}, date_fields=['field1', 'field2'])

        self.session.call.assert_called_once_with('mdstudio.db.replace_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 5},
            'replacement': {'test': 8},
            'upsert': False,
            'fields': {
                'date': ['field1', 'field2']
            }
        })

    def test_count(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.count('col')

        self.session.call.assert_called_once_with('mdstudio.db.count.namespace', {
            'collection': 'col'
        })

    def test_count_cursor_id(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.count('col', cursor_id='1234')

        self.session.call.assert_called_once_with('mdstudio.db.count.namespace', {
            'collection': 'col',
            'cursorId': '1234'
        })

    def test_count_cursor_id_with_skip_and_limit(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.count('col', cursor_id='1234', with_limit_and_skip=True)

        self.session.call.assert_called_once_with('mdstudio.db.count.namespace', {
            'collection': 'col',
            'cursorId': '1234',
            'withLimitAndSkip': True
        })

    def test_count_with_skip_and_limit(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.count('col', with_limit_and_skip=True)

        self.session.call.assert_called_once_with('mdstudio.db.count.namespace', {
            'collection': 'col'
        })

    def test_count_filter(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.count('col', filter={'_id': 5})

        self.session.call.assert_called_once_with('mdstudio.db.count.namespace', {
            'collection': 'col',
            'filter': {'_id': 5}
        })

    def test_count_skip(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.count('col', skip=10)

        self.session.call.assert_called_once_with('mdstudio.db.count.namespace', {
            'collection': 'col',
            'skip': 10
        })

    def test_count_limit(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.count('col', limit=10)

        self.session.call.assert_called_once_with('mdstudio.db.count.namespace', {
            'collection': 'col',
            'limit': 10
        })

    def test_update_one(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.update_one('col', {'_id': 50}, {'test': 11})

        self.session.call.assert_called_once_with('mdstudio.db.update_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 11}
        })

    def test_update_one_upsert(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.update_one('col', {'_id': 50}, {'test': 11}, upsert=True)

        self.session.call.assert_called_once_with('mdstudio.db.update_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 11},
            'upsert': True
        })

    def test_update_one_date_fields(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.update_one('col', {'_id': 50}, {'test': 11}, date_fields=['field1', 'field2'])

        self.session.call.assert_called_once_with('mdstudio.db.update_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 11},
            'fields': {
                'date': ['field1', 'field2']
            }
        })

    def test_update_many(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.update_many('col', {'_id': 50}, {'test': 11})

        self.session.call.assert_called_once_with('mdstudio.db.update_many.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 11}
        })

    def test_update_many_upsert(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.update_many('col', {'_id': 50}, {'test': 11}, upsert=True)

        self.session.call.assert_called_once_with('mdstudio.db.update_many.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 11},
            'upsert': True
        })

    def test_update_many_date_fields(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.update_many('col', {'_id': 50}, {'test': 11}, date_fields=['field1', 'field2'])

        self.session.call.assert_called_once_with('mdstudio.db.update_many.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 11},
            'fields': {
                'date': ['field1', 'field2']
            }
        })

    def test_find_one(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one('col', {'_id': 50})

        self.session.call.assert_called_once_with('mdstudio.db.find_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 50}
        })

    def test_find_one_projection(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one('col', {'_id': 50}, projection={'projection': 'yes'})

        self.session.call.assert_called_once_with('mdstudio.db.find_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'projection': {'projection': 'yes'}
        })

    def test_find_one_skip(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one('col', {'_id': 50}, skip=10)

        self.session.call.assert_called_once_with('mdstudio.db.find_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'skip': 10
        })

    def test_find_one_sort(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one('col', {'_id': 50}, sort=[('_id', SortMode.Asc)])

        self.session.call.assert_called_once_with('mdstudio.db.find_one.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'sort': [('_id', SortMode.Asc)]
        })

    def test_find_many(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_many('col', {'_id': 50})

        self.session.call.assert_called_once_with('mdstudio.db.find_many.namespace', {
            'collection': 'col',
            'filter': {'_id': 50}
        })

    def test_find_many_projection(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_many('col', {'_id': 50}, projection={'projection': 'yes'})

        self.session.call.assert_called_once_with('mdstudio.db.find_many.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'projection': {'projection': 'yes'}
        })

    def test_find_many_skip(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_many('col', {'_id': 50}, skip=10)

        self.session.call.assert_called_once_with('mdstudio.db.find_many.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'skip': 10
        })

    def test_find_many_limit(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_many('col', {'_id': 50}, limit=10)

        self.session.call.assert_called_once_with('mdstudio.db.find_many.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'limit': 10
        })

    def test_find_many_sort(self):

        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_many('col', {'_id': 50}, sort=[('_id', SortMode.Asc)])

        self.session.call.assert_called_once_with('mdstudio.db.find_many.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'sort': [('_id', SortMode.Asc)]
        })

    def test_find_one_and_update(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_update('col', {'_id': 50}, {'test': 80})

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_update.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 80},
            'returnUpdated': False,
            'upsert': False
        })

    def test_find_one_and_update_upsert(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_update('col', {'_id': 50}, {'test': 80}, upsert=True)

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_update.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 80},
            'returnUpdated': False,
            'upsert': True
        })

    def test_find_one_and_update_return_updated(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_update('col', {'_id': 50}, {'test': 80}, return_updated=True)

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_update.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 80},
            'returnUpdated': True,
            'upsert': False
        })

    def test_find_one_and_update_date_fields(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_update('col', {'_id': 50}, {'test': 80}, date_fields=['field1', 'field2'])

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_update.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 80},
            'fields': {
                'date': ['field1', 'field2']
            },
            'returnUpdated': False,
            'upsert': False
        })

    def test_find_one_and_update_projection(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_update('col', {'_id': 50}, {'test': 80}, projection={'projection': 'yes'})

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_update.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 80},
            'projection': {'projection': 'yes'},
            'returnUpdated': False,
            'upsert': False
        })

    def test_find_one_and_update_sort(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_update('col', {'_id': 50}, {'test': 80}, sort=[('_id', SortMode.Asc)])

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_update.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'update': {'test': 80},
            'sort': [('_id', SortMode.Asc)],
            'returnUpdated': False,
            'upsert': False
        })

    def test_find_one_and_replace(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_replace('col', {'_id': 50}, {'test': 80})

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_replace.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'replacement': {'test': 80},
            'returnUpdated': False,
            'upsert': False
        })

    def test_find_one_and_replace_upsert(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_replace('col', {'_id': 50}, {'test': 80}, upsert=True)

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_replace.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'replacement': {'test': 80},
            'returnUpdated': False,
            'upsert': True
        })

    def test_find_one_and_replace_return_updated(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_replace('col', {'_id': 50}, {'test': 80}, return_updated=True)

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_replace.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'replacement': {'test': 80},
            'returnUpdated': True,
            'upsert': False
        })

    def test_find_one_and_replace_date_fields(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_replace('col', {'_id': 50}, {'test': 80}, date_fields=['field1', 'field2'])

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_replace.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'replacement': {'test': 80},
            'fields': {
                'date': ['field1', 'field2']
            },
            'returnUpdated': False,
            'upsert': False
        })

    def test_find_one_and_replace_projection(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_replace('col', {'_id': 50}, {'test': 80}, projection={'projection': 'yes'})

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_replace.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'replacement': {'test': 80},
            'projection': {'projection': 'yes'},
            'returnUpdated': False,
            'upsert': False
        })

    def test_find_one_and_replace_sort(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_replace('col', {'_id': 50}, {'test': 80}, sort=[('_id', SortMode.Asc)])

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_replace.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'replacement': {'test': 80},
            'sort': [('_id', SortMode.Asc)],
            'returnUpdated': False,
            'upsert': False
        })

    def test_find_one_and_delete(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_delete('col', {'_id': 50})

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_delete.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
        })

    def test_find_one_and_delete_projection(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_delete('col', {'_id': 50}, projection={'projection': 'yes'})

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_delete.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'projection': {'projection': 'yes'},
        })

    def test_find_one_and_delete_sort(self):
        self.session.call = mock.MagicMock(return_value='namespace')
        self.wrapper.find_one_and_delete('col', {'_id': 50}, sort=[('_id', SortMode.Asc)])

        self.session.call.assert_called_once_with('mdstudio.db.find_one_and_delete.namespace', {
            'collection': 'col',
            'filter': {'_id': 50},
            'sort': [('_id', SortMode.Asc)],
        })