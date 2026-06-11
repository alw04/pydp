from lib.build_systems.autotools import AutotoolsPackage


class Jemalloc(AutotoolsPackage):
    """jemalloc is a general purpose malloc(3) implementation that emphasizes
    fragmentation avoidance and scalable concurrency support."""

    homepage = "http://jemalloc.net/"
    url = "https://github.com/jemalloc/jemalloc/releases/download/{version}/jemalloc-{version}.tar.bz2"

    versions = [
        "5.3.0",
    ]
