cmake_minimum_required(VERSION 3.24)
project(LeetCodeAtlas VERSION 0.2.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")

option(ATLAS_SANITIZERS "Enable AddressSanitizer and UndefinedBehaviorSanitizer" OFF)

include(FetchContent)
include(CTest)

find_package(nlohmann_json 3.12.0 EXACT QUIET)
if(NOT nlohmann_json_FOUND)
    set(JSON_BuildTests OFF CACHE BOOL "" FORCE)
    FetchContent_Declare(
        nlohmann_json
        URL https://github.com/nlohmann/json/releases/download/v3.12.0/json.tar.xz
        URL_HASH SHA256=42f6e95cad6ec532fd372391373363b62a14af6d771056dbfc86160e6dfff7aa
        DOWNLOAD_EXTRACT_TIMESTAMP TRUE
    )
    FetchContent_MakeAvailable(nlohmann_json)
endif()

add_library(atlas_options INTERFACE)
target_compile_features(atlas_options INTERFACE cxx_std_23)
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(atlas_options INTERFACE -Wall -Wextra -Wpedantic -Werror)
    if(ATLAS_SANITIZERS)
        target_compile_options(atlas_options INTERFACE -fsanitize=address,undefined -fno-omit-frame-pointer)
        target_link_options(atlas_options INTERFACE -fsanitize=address,undefined)
    endif()
elseif(MSVC)
    target_compile_options(atlas_options INTERFACE /W4 /WX)
    if(ATLAS_SANITIZERS)
        message(FATAL_ERROR "ATLAS_SANITIZERS requires GCC or Clang")
    endif()
elseif(ATLAS_SANITIZERS)
    message(FATAL_ERROR "ATLAS_SANITIZERS requires GCC or Clang")
endif()

file(GLOB atlas_runners CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/problems/*/cpp_runner.cpp")
foreach(runner IN LISTS atlas_runners)
    get_filename_component(problem_directory "${runner}" DIRECTORY)
    get_filename_component(problem_slug "${problem_directory}" NAME)
    string(REPLACE "-" "_" target_suffix "${problem_slug}")
    set(target_name "atlas_${target_suffix}")
    add_executable("${target_name}" cpp/main.cpp "${runner}")
    target_include_directories("${target_name}" PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/cpp")
    target_link_libraries("${target_name}" PRIVATE atlas_options nlohmann_json::nlohmann_json)
endforeach()

if(BUILD_TESTING)
    find_package(Catch2 3.8.1 EXACT QUIET)
    if(NOT Catch2_FOUND)
        set(CATCH_BUILD_TESTING OFF CACHE BOOL "" FORCE)
        set(CATCH_INSTALL_DOCS OFF CACHE BOOL "" FORCE)
        FetchContent_Declare(
            Catch2
            URL https://github.com/catchorg/Catch2/archive/refs/tags/v3.8.1.tar.gz
            URL_HASH SHA256=18b3f70ac80fccc340d8c6ff0f339b2ae64944782f8d2fca2bd705cf47cadb79
            DOWNLOAD_EXTRACT_TIMESTAMP TRUE
        )
        FetchContent_MakeAvailable(Catch2)
    endif()
    add_executable(atlas_adapter_tests cpp/test_adapter.cpp)
    set_target_properties(atlas_adapter_tests PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/tests")
    target_include_directories(atlas_adapter_tests PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/cpp")
    target_link_libraries(
        atlas_adapter_tests PRIVATE atlas_options nlohmann_json::nlohmann_json Catch2::Catch2WithMain
    )
    add_test(NAME atlas_adapter COMMAND atlas_adapter_tests)
endif()
