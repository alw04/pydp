from lib.build_systems.autotools import AutotoolsPackage


class Libgd(AutotoolsPackage):
    """GD is an open source code library for the dynamic creation of images
    by programmers. GD is written in C, and "wrappers" are available
    for Perl, PHP and other languages. GD creates PNG, JPEG, GIF,
    WebP, XPM, BMP images, among other formats. GD is commonly used to
    generate charts, graphics, thumbnails, and most anything else, on
    the fly. While not restricted to use on the web, the most common
    applications of GD involve website development.
    """

    homepage = "https://github.com/libgd/libgd"
    url = "https://github.com/libgd/libgd/releases/download/gd-{version}/libgd-{version}.tar.gz"

    versions = [
        "2.3.3",
    ]
