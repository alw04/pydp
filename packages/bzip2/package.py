from lib.build_systems.makefile import MakefilePackage


class Bzip2(MakefilePackage):
    """bzip2 is a freely available, patent free high-quality data
    compressor. It typically compresses files to within 10% to 15%
    of the best available techniques (the PPM family of statistical
    compressors), whilst being around twice as fast at compression
    and six times faster at decompression."""

    homepage = "https://sourceware.org/bzip2/"
    url = "https://sourceware.org/pub/bzip2/bzip2-{version}.tar.gz"

    versions = [
        "1.0.8",
    ]

    def make_args(self):
        return [
            "CFLAGS=-fPIC",
        ]

    def install_args(self):
        return [
            f"PREFIX={self.prefix}",
        ]

    def build(self):
        super().build()

        self.run_cmd(["make", "CFLAGS=-fPIC", "-f", "Makefile-libbz2_so"], cwd=self.build_dir)

    def install(self):
        super().install()

        soname = f"libbz2.so.{self.version}"

        self.install_file(self.build_dir / soname, self.prefix / "lib" / soname, mode=0o755)
        self.install_symlink(soname, self.prefix / "lib" / "libbz2.so")
        self.install_symlink(soname, self.prefix / "lib" / "libbz2.so.1")
        self.install_symlink(soname, self.prefix / "lib" / "libbz2.so.1")
        self.install_symlink(soname, self.prefix / "lib" / "libbz2.so.1.0")
