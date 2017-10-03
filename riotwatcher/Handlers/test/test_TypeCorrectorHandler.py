
import unittest

from .. import TypeCorrectorHandler


class TypeCorrectorHandlerTestCase(unittest.TestCase):
    def test_bool_remapped_to_string(self):
        corrector = TypeCorrectorHandler()

        query_params = {
            'a': 'test',
            'b': 123,
            'c': True,
            'd': False,
            'e': ['first', 'test'],
            'f': [123, 456],
            'g': [True, False],
            'h': ['hard', 2, True, False],
        }

        corrector.preview_request(None, None, None, query_params)

        self.assertEquals('test', query_params['a'])
        self.assertEquals(123, query_params['b'])
        self.assertEquals('true', query_params['c'])
        self.assertEquals('false', query_params['d'])
        self.assertEquals(['first', 'test'], query_params['e'])
        self.assertEquals([123, 456], query_params['f'])
        self.assertEquals(['true', 'false'], query_params['g'])
        self.assertEquals(['hard', 2, 'true', 'false'], query_params['h'])
