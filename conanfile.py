from conans import ConanFile, CMake, tools


class UwebsocketsConan(ConanFile):
    name = "uWebSockets"
    version = "0.14.6"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Uwebsockets here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "OpenSSL/1.1.0g@conan/stable", "zlib/1.2.8@conan/stable", "libuv/1.15.0@bincrafters/stable"
    exports_sources = "*"

    def source(self):
        self.run("git clone https://github.com/uNetworking/uWebSockets")
        self.run("cd uWebSockets && git checkout v0.14.6")
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cmake")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include/uWS", src="uWebSockets/src")
        self.copy("*uWS.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["uWS"]
