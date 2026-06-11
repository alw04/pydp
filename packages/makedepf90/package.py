from lib.build_systems.autotools import AutotoolsPackage


class Makedepf90(AutotoolsPackage):
    """Makedepf90 is a program for automatic creation of Makefile-style dependency lists for
    Fortran source code."""

    homepage = "https://salsa.debian.org/science-team/makedepf90"
    url = "https://deb.debian.org/debian/pool/main/m/makedepf90/makedepf90_{version}.orig.tar.xz"

    versions = [
        "3.0.1",
    ]
