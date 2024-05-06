import unittest
import os
from selenium.webdriver import ChromeOptions, ChromeService, Chrome
import c4t

__author__ = 'p4irin'
__email__ = '139928764+p4irin@users.noreply.github.com'
__version__ = '1.6.0'


class C4tTests(unittest.TestCase):

    class _TestData:
        specific_version_of_assets = '116.0.5794.0'

    @classmethod
    def setUpClass(cls) -> None:
        cls.assets_dir = c4t.path_to_assets
        cls.assets = c4t.Assets()
        cls.chrome_options = ChromeOptions()
        cls.chrome_options.binary_location = c4t.location.chrome
        cls.chrome_options.add_argument('--no-sandbox')
        cls.chrome_options.add_argument('--headless')        
        cls.chrome_service = ChromeService(
            executable_path=c4t.location.chromedriver
        )

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
    
    def verify_chrome_for_testing_version_with_selenium(
            self, expected_version: str
        ):

        browser = Chrome(
            options=self.chrome_options, service=self.chrome_service
        )
        browser.get('http://pypi.org/user/p4irin')
        self.assertTrue(browser.title == 'Profile of p4irin · PyPI')
        self.assertTrue(
            browser.capabilities["browserVersion"] == expected_version
        )
        browser.quit()

    def test_001_default_path_to_assets(self):
        self.assertTrue(os.path.exists(f'{self.assets_dir}'))
        self.assertTrue(os.path.isdir(self.assets_dir))

    def test_002_installation_of_default_latest_stable_version(self):            
        assets = self.assets
        assets.install()
        self.assertTrue(isinstance(assets.active_version, str))
        self.assertTrue(
            os.path.exists(
                f'{self.assets_dir}/{assets.active_version}/chrome-linux64/chrome'
            )
        )
        self.assertTrue(
            os.path.exists(
                f'{self.assets_dir}/{assets.active_version}/chromedriver-linux64'
                + '/chromedriver'
            )
        )

        self.verify_chrome_for_testing_version_with_selenium(
            expected_version=assets.active_version
        )

    def test_003_installation_of_a_specific_version_of_assets(self):     
        assets = self.assets
        assets.install(self._TestData.specific_version_of_assets)
        self.assertTrue(
            assets.active_version == self._TestData.specific_version_of_assets)
        self.assertTrue(
            os.path.exists(
                f'{self.assets_dir}/{assets.active_version}/chrome-linux64/chrome'
            )
        )
        self.assertTrue(
            os.path.exists(
                f'{self.assets_dir}/{assets.active_version}/chromedriver-linux64'
                + '/chromedriver'
            )
        )

        self.verify_chrome_for_testing_version_with_selenium(
            expected_version=assets.active_version
        )