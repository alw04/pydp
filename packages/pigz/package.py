from lib.build_systems.makefile import MakefilePackage


class Pigz(MakefilePackage):
    """A parallel implementation of gzip for modern multi-processor,
    multi-core machines."""

    homepage = "https://zlib.net/pigz/"
    url = "https://github.com/madler/pigz/archive/v{version}.tar.gz"

    versions = [
        "2.8",
    ]

    def install(self):
        self.install_binary(self.build_dir / "pigz")
