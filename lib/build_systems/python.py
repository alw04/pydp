import sysconfig
from pathlib import Path

from lib.dependency import Dependency
from lib.package import Package


class PythonPackage(Package):
    abstract = True

    phases = ("install",)

    depends_on = [
        Dependency("python", type="build"),  # runtime uses the package's own venv
    ]

    def extra_module_paths(self):
        site = sysconfig.get_path("purelib", vars={"base": str(self.prefix)})

        path = Path(site)
        if path.exists():
            return {"PYTHONPATH": [path]}

        return {}

    @property
    def venv_python(self) -> Path:
        return self.prefix / "bin" / "python"

    def create_venv(self):
        self.run_cmd(["python3", "-m", "venv", "--clear", str(self.prefix)])

        self.run_cmd([str(self.venv_python), "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

    def install(self):
        self.create_venv()

        self.run_cmd(
            [
                str(self.venv_python),
                "-m",
                "pip",
                "install",
                f"{self.name}=={self.version}",
                # "--no-deps",
            ]
        )
