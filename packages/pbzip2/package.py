from lib.build_systems.makefile import MakefilePackage


class Pbzip2(MakefilePackage):
    """PBZIP2 is a parallel implementation of the bzip2 block-sorting file
    compressor that uses pthreads and achieves near-linear speedup on SMP
    machines. The output of this version is fully compatible with bzip2 v1.0.2
    or newer (ie: anything compressed with pbzip2 can be decompressed with
    bzip2). PBZIP2 should work on any system that has a pthreads compatible C++
    compiler (such as gcc)."""

    homepage = "http://compression.great-site.net/pbzip2/"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2])
        return f"https://launchpad.net/pbzip2/{major_minor}/{version}/+download/pbzip2-{version}.tar.gz"

    versions = [
        "1.1.13",
    ]

    def install_args(self):
        return [
            f"PREFIX={self.prefix}",
        ]
