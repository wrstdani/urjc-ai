cmake_minimum_required(VERSION 3.26)
project(mandelbrot C)

set(CMAKE_C_STANDARD 99)

add_executable(mandelbrot Bitmap.c Bitmap.h colourScale.h complexC.c complexC.h main.c)
