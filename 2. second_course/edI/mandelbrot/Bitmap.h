#include <stdio.h>
#include <stdlib.h>
#pragma once
typedef struct
{
	unsigned char * header;
	unsigned char* pixels;
	int width_;
	int height_;
	int rowSize_;
	int imgSize_;
	short colorDepth_;
	const char * bmpFileName;
} Bitmap;

Bitmap createBitmap(const char* fileName, int width, int height, short colorDepth);
Bitmap readBitmap(const char* fileName);
void saveBitmap(Bitmap* bmp);
void putPixelRGB(Bitmap* bmp, int x, int y, unsigned char R, unsigned char G, unsigned char B);
void putPixel(Bitmap* bmp, int x, int y, char i);
unsigned char* getPixel(Bitmap * bmp, int x, int y);