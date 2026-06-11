from lib.build_systems.cmake import CMakePackage


class Hdf5(CMakePackage):
    """HDF5 is a data model, library, and file format for storing and managing
    data. It supports an unlimited variety of datatypes, and is designed for
    flexible and efficient I/O and for high volume and complex data.
    """

    homepage = "https://support.hdfgroup.org"

    def url_for_version(self, version):
        major, minor, patch = version.split(".")
        major_minor = "_".join([major, minor])
        version_underscored = "_".join([major, minor, patch])
        return f"https://support.hdfgroup.org/releases/hdf5/v{major_minor}/v{version_underscored}/downloads/hdf5-{version}.tar.gz"

    versions = [
        "1.14.6",
    ]
