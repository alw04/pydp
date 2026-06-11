from lib.build_systems.autotools import AutotoolsPackage


class Parallel(AutotoolsPackage):
    """GNU parallel is a shell tool for executing jobs in parallel using
    one or more computers. A job can be a single command or a small
    script that has to be run for each of the lines in the input.
    """

    homepage = "https://www.gnu.org/software/parallel/"
    url = "https://ftp.gnu.org/gnu/parallel/parallel-{version}.tar.bz2"

    versions = [
        "20240822",
    ]
