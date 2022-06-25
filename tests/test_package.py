# -*- coding: utf-8 -*-

"""
Test the project as a package e.g. check the version, style etc.
"""

import pytest

from cro.geneea.sdk import __version__


@pytest.mark.package
def test_package_version_is_correct():
    assert __version__ == "0.6.0"


# test_package_version_in_readme_file_is_correct

# test_package_license_in_readme_file_is_correct

# test_package_manifest_file_is_correct

# test_package_documentation (?)


