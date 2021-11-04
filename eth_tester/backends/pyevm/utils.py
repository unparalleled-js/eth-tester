from __future__ import absolute_import

import pkg_resources

from semantic_version import (
    Version,
)


def get_pyevm_version():
    try:
        base_version = pkg_resources.parse_version(
            pkg_resources.get_distribution("py-evm").version
        ).base_version
        return Version(base_version)
    except pkg_resources.DistributionNotFound:
        return None


def is_pyevm_available():
    version = get_pyevm_version()
    if not version:
        return False

    minimum_supported_version = Version("0.5.0")
    return version >= minimum_supported_version
