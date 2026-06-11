from lib.build_systems.cmake import CMakePackage


class Nlopt(CMakePackage):
    """NLopt is a free/open-source library for nonlinear optimization,
    providing a common interface for a number of different free optimization
    routines available online as well as original implementations of various
    other algorithms."""

    homepage = "https://nlopt.readthedocs.io"
    url = "https://github.com/stevengj/nlopt/archive/v{version}.tar.gz"

    versions = [
        "2.9.1",
    ]
