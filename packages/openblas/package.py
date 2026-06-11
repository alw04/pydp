from lib.build_systems.makefile import MakefilePackage


class Openblas(MakefilePackage):
    """OpenBLAS: An optimized BLAS library"""

    homepage = "https://www.openblas.net"
    url = "https://github.com/OpenMathLib/OpenBLAS/releases/download/v{version}/OpenBLAS-{version}.tar.gz"

    versions = [
        "0.3.30",
    ]

    def install_args(self):
        return [
            f"PREFIX={self.prefix}",
        ]
