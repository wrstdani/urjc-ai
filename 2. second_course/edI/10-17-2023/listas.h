//
// Created by Daniel del Nuevo Montero on 18/10/23.
//

#ifndef INC_10_17_2023_LISTAS_H
#define INC_10_17_2023_LISTAS_H

#include <stdio.h>

typedef struct {
    char name[20];
    int age;
} tElemento;

typedef struct {
    tElemento info;
    int sig;
} tNodo;

typedef struct {
    tNodo almacen[100];
    int primOcupada;
    int primLibre;
} tLista;

void mostrarElemento(tElemento info);
void imprimirLista(tLista lista);
void asignarElemento(tElemento info, tElemento e);
void construir(tLista *lista, tElemento e);
void crearVacia(tLista *lista, int max);

#endif //INC_10_17_2023_LISTAS_H
