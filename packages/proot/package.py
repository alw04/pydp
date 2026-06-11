from lib.package import Package


class Proot(Package):
    """PRoot is a user-space implementation of chroot, mount --bind, and binfmt_misc.
    This means that users don't need any privileges or setup to do things like using
    an arbitrary directory as the new root filesystem, making files accessible somewhere
    else in the filesystem hierarchy, or executing programs built for another
    CPU architecture transparently through QEMU user-mode.
    """

    homepage = "https://proot-me.github.io/"
    url = "https://github.com/proot-me/proot/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "5.4.0",
    ]

    def configure(self):
        self.run_cmd(["make", "-C", "src", "loader.elf", "loader-m32.elf", "build.h"], cwd=self.build_dir)

    def build(self):
        self.run_cmd(["make", "-C", "src", "proot"], cwd=self.build_dir)

    def install(self):
        self.install_binary(self.build_dir / "src" / "proot")
