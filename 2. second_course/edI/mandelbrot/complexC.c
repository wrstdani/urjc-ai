//
// Created by ddeln on 26/09/2023.
//

#include "complexC.h"

// (* constructoras generadoras *)
tComplejo complexCreate(double re1, double im1) {
    tComplejo c;
    c.re = re1;
    c.im = im1;
    return c;
}

// (* observadoras selectoras *)
double complexObtenerReal(tComplejo c1) {
    return c1.re;
}
double complexObtenerImaginaria(tComplejo c1) {
    return c1.im;
}

// (* observadoras no selectoras *)
double complexModulo(tComplejo c1) {
    double real = c1.re;
    double imag = c1.im;
    double modulo = sqrt(pow(real, 2)+pow(imag, 2));
    return modulo;
}

// (* constructoras no generadoras *)
tComplejo complexConjugado(tComplejo c1) {
    c1.im = -(c1.im);
    return c1;
}
tComplejo complexSuma(tComplejo c1, tComplejo c2) {
    tComplejo c3;
    c3.re = c1.re + c2.re;
    c3.im = c1.im + c2.im;
    return c3;
}

tComplejo complexResta(tComplejo c1, tComplejo c2) {
    tComplejo c3;
    c3.re = c1.re - c2.re;
    c3.im = c1.im - c2.im;
    return c3;
}

tComplejo complexMultiplicacion(tComplejo c1, tComplejo c2) {
    tComplejo c3;
    c3.re = (c1.re * c2.re) - (c1.im * c2.im);
    c3.im = (c1.re * c2.im) + (c1.im * c2.re);
    return c3;
}
tComplejo complexDivision(tComplejo c1, tComplejo c2) {
    tComplejo c3;
    if (complexObtenerReal(c2) != 0 || complexObtenerImaginaria(c2) != 0) {
        c3.re = ((c1.re * c2.re) + (c1.im * c2.im)) / (pow(c2.re, 2) + pow(c2.im, 2));
        c3.im = ((c1.re * c2.im) - (c1.im * c2.re)) / (pow(c2.re, 2) + pow(c2.im, 2));
    } else {
        perror("\nHas intentado realizar una división entre 0.\n");
        c3.re = 0;
        c3.im = 0;
    }
    return c3;
}