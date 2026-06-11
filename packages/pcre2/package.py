from lib.build_systems.autotools import AutotoolsPackage


class Pcre2(AutotoolsPackage):
    """The PCRE2 package contains Perl Compatible Regular Expression
    libraries. These are useful for implementing regular expression
    pattern matching using the same syntax and semantics as Perl 5."""

    homepage = "https://www.pcre.org"
    url = "https://github.com/PCRE2Project/pcre2/releases/download/pcre2-{version}/pcre2-{version}.tar.bz2"

    versions = [
        "10.44",
    ]
