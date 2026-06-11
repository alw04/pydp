from lib.build_systems.autotools import AutotoolsPackage


class Pcre(AutotoolsPackage):
    """The PCRE package contains Perl Compatible Regular Expression
    libraries. These are useful for implementing regular expression
    pattern matching using the same syntax and semantics as Perl 5."""

    homepage = "https://www.pcre.org"
    url = "https://sourceforge.net/projects/pcre/files/pcre/{version}/pcre-{version}.tar.bz2"

    versions = [
        "8.45",
    ]
