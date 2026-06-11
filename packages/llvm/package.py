from lib.build_systems.cmake import CMakePackage


class Llvm(CMakePackage):
    """The LLVM Project is a collection of modular and reusable compiler and
    toolchain technologies. Despite its name, LLVM has little to do
    with traditional virtual machines, though it does provide helpful
    libraries that can be used to build them. The name "LLVM" itself
    is not an acronym; it is the full name of the project.
    """

    homepage = "https://llvm.org/"
    url = "https://github.com/llvm/llvm-project/archive/llvmorg-{version}.tar.gz"

    versions = [
        "20.1.8",
    ]

    source_subdir = "llvm"

    def cmake_args(self):
        return ["-DCMAKE_BUILD_TYPE=Release"]
