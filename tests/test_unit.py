import os
import unittest
from importlib import reload
import shutil
import c4t

__author__ = 'p4irin'
__email__ = '139928764+p4irin@users.noreply.github.com'
__version__ = '1.6.0'


class C4tAssetsUnitTests(unittest.TestCase):

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

    def test_001__create_default_assets_dir(self) -> None:
        c4t.Assets() # calls c4t.Assets()._create_assets_dir()
        self.assertTrue(os.path.exists(c4t.path_to_assets))
        self.assertTrue(os.path.isdir(c4t.path_to_assets))
        self.assertEqual(c4t.location.chrome, f'{c4t.path_to_assets}/chrome')
        self.assertEqual(
            c4t.location.chromedriver, f'{c4t.path_to_assets}/chromedriver'
            )
        
    def test_002__create_default_assets_dir_again(self) -> None:
        try:
            c4t.Assets()
        except Exception as e:
            self.fail(
                f'Calling Assets()._create_assets_dir() again should not raise {type(e).__name__}'
                )
    
    def test_003__create_assets_dir_from_environment_variable(self) -> None:
        assets_dir = f'{os.getenv("HOME")}/.c4t-assets-test'
        os.environ['C4T_PATH_TO_ASSETS'] = assets_dir
        reload(c4t)
        c4t.Assets()
        self.assertEqual(c4t.path_to_assets, assets_dir)
        self.assertTrue(os.path.exists(assets_dir))
        self.assertTrue(os.path.isdir(assets_dir))
        self.assertEqual(c4t.location.chrome, f'{assets_dir}/chrome')
        self.assertEqual(
            c4t.location.chromedriver, f'{assets_dir}/chromedriver'
            )
        # Clean up
        del os.environ['C4T_PATH_TO_ASSETS']
        reload(c4t)
        self.assertEqual(c4t.path_to_assets, c4t._default_path_to_assets)
        os.rmdir(assets_dir)

    def test_004__installation_path_of(self) -> None:
        assets = c4t.Assets()
        assets._download_dir = f'{c4t.path_to_assets}/version'
        assets._platform = 'linux64'
        installation_path_of_chrome = assets._installation_path_of('chrome')
        self.assertIsInstance(installation_path_of_chrome, str)
        self.assertEqual(
            installation_path_of_chrome,
            f'{assets._download_dir}/chrome-{assets._platform}'
            )
        installation_path_of_chromedriver = assets._installation_path_of(
            'chromedriver'
            )
        self.assertIsInstance(installation_path_of_chromedriver, str)
        self.assertEqual(
            installation_path_of_chromedriver,
            f'{assets._download_dir}/chromedriver-{assets._platform}'
            )
        
    def test_004__create_symlink(self) -> None:
        assets = c4t.Assets()
        assets._create_symlink(
            to_binary='chrome', version='bogus_version', for_platform='linux64'
            )
        symlink_to_binary = f'{assets.path}/chrome'
        self.assertEqual(
            os.readlink(symlink_to_binary),
            './bogus_version/chrome-linux64/chrome'
        )

    def test_005_active_version_is_bogus_version(self) -> None:
        # The active version is 'bogus_version' set in previous test
        assets = c4t.Assets()
        active_version = assets.active_version
        self.assertIsInstance(active_version, str)
        self.assertEqual(
            active_version, 'bogus_version'
        )
        shutil.rmtree(assets.path)

    def test_006_active_version_not_found(self) -> None:
        assets = c4t.Assets()
        active_version = assets.active_version
        self.assertFalse(active_version)

    def test_007_path(self) -> None:
        assets = c4t.Assets()
        self.assertEqual(assets.path, c4t._default_path_to_assets)

    def test_008_installed(self) -> None:
        assets = c4t.Assets()
        versions = assets.installed(output=False)
        self.assertIsInstance(versions, list)

    def test_008_last_known_good_versions(self) -> None:
        assets = c4t.Assets()
        versions = assets.last_known_good_versions()
        self.assertIsInstance(versions, list)
