from lib.build_systems.autotools import AutotoolsPackage


class Libevent(AutotoolsPackage):
    """The libevent API provides a mechanism to execute a callback function
    when a specific event occurs on a file descriptor or after a
    timeout has been reached. Furthermore, libevent also support
    callbacks due to signals or regular timeouts.
    """

    homepage = "https://libevent.org"
    url = "https://github.com/libevent/libevent/releases/download/release-{version}-stable/libevent-{version}-stable.tar.gz"

    versions = [
        "2.1.12",
    ]
