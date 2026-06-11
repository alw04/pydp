from lib.build_systems.cmake import CMakePackage


class Mariadb(CMakePackage):
    """MariaDB Server is one of the most popular database servers
    in the world.

    MariaDB turns data into structured information in a wide array of
    applications, ranging from banking to websites. It is an enhanced, drop-in
    replacement for MySQL. MariaDB is used because it is fast, scalable and
    robust, with a rich ecosystem of storage engines, plugins and many other
    tools make it very versatile for a wide variety of use cases.
    """

    homepage = "https://mariadb.org/about/"
    url = "https://archive.mariadb.org/mariadb-{version}/source/mariadb-{version}.tar.gz"

    versions = [
        "12.1.1",
    ]
