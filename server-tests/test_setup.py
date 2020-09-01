import sys
import webtest
import unittest
import os
from google.appengine.ext import testbed
from main import app
import dev_appserver
dev_appserver.fix_sys_path()


# sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine')
# sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine/lib/yaml/lib')
# sys.path.insert(1, 'server/lib')

import logging

logging.basicConfig(level=logging.INFO)


class UnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a WSGI application.
        cls.testapp = webtest.TestApp(app)
        # First, create an instance of the Testbed class.
        cls.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        cls.testbed.activate()
        # Ref: https://cloud.google.com/appengine/docs/standard/python/refdocs/modules/google/appengine/ext/testbed#Testbed.setup_env
        cls.testbed.setup_env()
        # allows you to test your datastore code without making any requests to the real datastore.
        # Any entity stored during a datastore unit test is held in memory
        # and is deleted after the test run. You can run small
        # cls.testbed.init_search_stub()
        # cls.testbed.init_datastore_v3_stub()
        # cls.testbed.init_memcache_stub()
        # cls.testbed.init_urlfetch_stub()


if __name__ == '__main__':
    unittest.main()
