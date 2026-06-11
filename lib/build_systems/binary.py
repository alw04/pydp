from lib.package import Package


class BinaryPackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "install",
    )

    def install(self):
        self.install_directory(self.build_dir, self.prefix)
