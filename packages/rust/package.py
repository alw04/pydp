from lib.dependency import Dependency
from lib.package import Package


class Rust(Package):
    """The Rust programming language toolchain."""

    homepage = "https://www.rust-lang.org"
    url = "https://static.rust-lang.org/dist/rustc-{version}-src.tar.gz"

    versions = [
        "1.85.0",
    ]

    depends_on = [
        Dependency("python", type="build"),
    ]

    def configure(self):
        config_path = self.build_dir / "config.toml"

        if config_path.exists():
            config_path.unlink()

        self.run_cmd(
            [
                str(self.build_dir / "configure"),
                "--set",
                f"install.prefix={self.prefix}",
                "--set",
                f"install.sysconfdir={self.prefix}/etc",
            ],
            cwd=self.build_dir,
        )

    def build(self):
        self.run_cmd([str(self.build_dir / "x.py"), "build"], cwd=self.build_dir)

    def install(self):
        self.run_cmd([str(self.build_dir / "x.py"), "install"], cwd=self.build_dir)
