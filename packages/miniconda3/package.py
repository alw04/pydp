from pathlib import Path

from lib.package import Package


class Miniconda3(Package):
    """The minimalist bootstrap toolset for conda and Python3."""

    homepage = "https://docs.anaconda.com/miniconda/"

    urls_by_version = {
        "25.5.1": "https://repo.anaconda.com/miniconda/Miniconda3-py313_25.5.1-1-Linux-x86_64.sh",
    }

    versions = [
        "25.5.1",
    ]

    conflicts = [
        "python",
    ]

    phases = (
        "download",
        "install",
    )

    @property
    def condarc_source(self):
        return Path(__file__).with_name("condarc")

    def install(self):
        installer = self.download_file

        installer.chmod(0o755)

        self.run_cmd([str(installer), "-b", "-p", str(self.prefix), "-u"])

        conda = self.prefix / "bin" / "conda"

        condarc_dest = self.prefix / ".condarc"

        self.atomic_write(condarc_dest, self.condarc_source.read_text())

        self.run_cmd([str(conda), "install", "-y", "-n", "base", "-c", "conda-forge", "mamba", "conda-libmamba-solver"])
