project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(uWS
    uWebSockets/src/Extensions.cpp
	uWebSockets/src/Group.cpp
	uWebSockets/src/Networking.cpp
	uWebSockets/src/Hub.cpp
	uWebSockets/src/Node.cpp
	uWebSockets/src/WebSocket.cpp
	uWebSockets/src/HTTPSocket.cpp
	uWebSockets/src/Socket.cpp
	uWebSockets/src/Epoll.cpp
)
target_include_directories(uWS PRIVATE
    uWebSockets
)
target_link_libraries(uWS ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
