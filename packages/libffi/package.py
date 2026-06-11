from lib.build_systems.autotools import AutotoolsPackage


class Libffi(AutotoolsPackage):
    """The libffi library provides a portable, high level programming
    interface to various calling conventions. This allows a programmer
    to call any function specified by a call interface description at
    run time."""

    homepage = "https://sourceware.org/libffi/"
    url = "https://github.com/libffi/libffi/releases/download/v{version}/libffi-{version}.tar.gz"

    versions = [
        "3.4.8",
    ]
