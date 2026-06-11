from lib.build_systems.cmake import CMakePackage


class Libcerf(CMakePackage):
    """A self-contained C library providing complex error functions, based
    on Faddeeva's plasma dispersion function w(z). Also provides Dawson's
    integral and Voigt's convolution of a Gaussian and a Lorentzian"""

    homepage = "https://jugit.fz-juelich.de/mlz/libcerf/"
    url = "https://jugit.fz-juelich.de/mlz/libcerf/-/archive/v{version}/libcerf-v{version}.tar.gz"

    versions = [
        "2.4",
    ]
