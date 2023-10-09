cmake_minimum_required(VERSION 3.26)
project(circuitoC C)

set(CMAKE_C_STANDARD 99)

add_executable(circuitoC
        complexC.c
        complexC.h
        main.c
        circuitC.c
        circuitC.h)
