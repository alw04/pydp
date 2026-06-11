from lib.build_systems.cmake import CMakePackage


class Libssh(CMakePackage):
    """libssh: the SSH library"""

    homepage = "https://www.libssh.org"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2])
        return f"https://www.libssh.org/files/{major_minor}/libssh-{version}.tar.xz"

    versions = [
        "0.11.2",
    ]
