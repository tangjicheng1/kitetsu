cmake_minimum_required(VERSION 3.20)

project(kitetsu_impl)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_BUILD_TYPE "Release")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static-libstdc++ -static-libgcc ")

find_package(Python 3.8...<4.0 COMPONENTS Interpreter Development.Module REQUIRED)

execute_process(
  COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE 
  OUTPUT_VARIABLE nanobind_ROOT
)

find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(replacesoh_impl src/replacesoh_impl.cpp)
