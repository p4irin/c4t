import unittest
import os
import time
from shutil import rmtree
from selenium.webdriver import ChromeOptions, ChromeService, Chrome
import c4t

__author__ = 'p4irin'
__email__ = '139928764+p4irin@users.noreply.github.com'
__version__ = '1.0.2'


class C4tTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_001_installation_of_default_latest_stable_version(self):
        assets_dir = './assets'
        rmtree(assets_dir) if os.path.exists(assets_dir) else None
            
        assets = c4t.Assets()
        self.assertTrue(os.path.isdir('./assets'))
        assets.install()
        self.assertTrue(type(assets.active_version) == str)
        self.assertTrue(
            os.path.exists(
                f'{assets_dir}/{assets.active_version}/chrome-linux64/chrome'
            )
        )
        self.assertTrue(
            os.path.exists(
                f'{assets_dir}/{assets.active_version}/chromedriver-linux64'
                + '/chromedriver'
            )
        )        

    def test_002_use_c4t_with_selenium(self):
        options = ChromeOptions()
        options.binary_location = c4t.location.chrome
        service = ChromeService(executable_path=c4t.location.chromedriver)
        browser = Chrome(options=options, service=service)
        browser.get('http://pypi.org/user/p4irin')
        self.assertTrue(browser.title == 'Profile of p4irin · PyPI')
        time.sleep(5)
        browser.quit()
