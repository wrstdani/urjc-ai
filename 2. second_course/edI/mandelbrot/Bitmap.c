#include "Bitmap.h"
#include "colourScale.h"
Bitmap createBitmap(const char* fileName, int width, int height, short colorDepth)
{
	Bitmap bmp;
	bmp.width_ = width;
	bmp.height_ = height;
	bmp.colorDepth_ = colorDepth;
	bmp.bmpFileName = fileName;
	bmp.rowSize_= ((colorDepth * 8 * width + 31) / 32) * 4;
	bmp.imgSize_ = bmp.rowSize_ * height;
	bmp.header = (unsigned char*)calloc(54, sizeof(unsigned char));
	bmp.pixels = (unsigned char*)calloc(bmp.imgSize_, sizeof(unsigned char));
	bmp.header[0] = 'B';
	bmp.header[1] = 'M';
	int* fileSize = (int*)&bmp.header[2];
	*fileSize = bmp.imgSize_ + 54;
	int* dataInit = (int*)&bmp.header[10];
	*dataInit = 54;
	int* headerSize = (int*)&bmp.header[14];
	*headerSize = 40;
	int* p_width = (int*)&bmp.header[18];
	*p_width = width;
	int* p_height = (int*)&bmp.header[22];
	*p_height = height;
	short* planeNumber = (short*)&bmp.header[26];
	*planeNumber = 1;
	short* p_colorDepth = (short*)&bmp.header[28];
	*p_colorDepth = colorDepth*8;
	return bmp;
}

Bitmap readBitmap(const char* fileName)
{
	Bitmap bmp;
	bmp.bmpFileName = fileName;
	bmp.header = (unsigned char*)calloc(54, sizeof(unsigned char));
	FILE* bmpFile = fopen(fileName, "rb");
	fread(bmp.header, sizeof(unsigned char), 54, bmpFile);
	bmp.width_ = *(int*)&bmp.header[18];
	bmp.height_ = *(int*)&bmp.header[22];
	bmp.colorDepth_ = *(short*)&bmp.header[28];
	bmp.rowSize_ = ((bmp.colorDepth_ * 8 * bmp.width_ + 31) / 32) * 4;
	bmp.imgSize_ = bmp.rowSize_ * bmp.height_;
	bmp.pixels = (unsigned char*)calloc(bmp.imgSize_, sizeof(unsigned char));
	fread(bmp.pixels, sizeof(unsigned char), bmp.imgSize_, bmpFile);
	fclose(bmpFile);
	return bmp;
}

void saveBitmap(Bitmap* bmp)
{
	FILE* bmpFile= fopen(bmp->bmpFileName, "wb");
	fwrite(bmp->header, sizeof(unsigned char), 54, bmpFile);
	fwrite(bmp->pixels, sizeof(unsigned char), bmp->imgSize_, bmpFile);
	fclose(bmpFile);
}

void putPixelRGB(Bitmap* bmp, int x, int y, unsigned char R, unsigned char G, unsigned char B)
{
	unsigned char* pixel = getPixel(bmp, x, y);
	pixel[0] = B;
	pixel[1] = G;
	pixel[2] = R;
}
void putPixel(Bitmap* bmp, int x, int y, char i)
{
	if(i<65) {
		putPixelRGB(bmp, x, y, Rs[i], Gs[i], Bs[i]);
	}
	else {
		putPixelRGB(bmp, x, y, 0, 0, 0);
	}
}

unsigned char* getPixel(Bitmap* bmp, int x, int y)
{
	return bmp->pixels + ((bmp->height_ - 1 - y) * bmp->rowSize_ + bmp->colorDepth_ * x);
}
