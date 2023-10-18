//
// Created by Daniel del Nuevo Montero on 18/10/23.
//

#include "listas.h"

void mostrarElemento(tElemento info) {
    printf("%s: %d\n", info.name, info.age);
}

void imprimirLista(tLista lista) {
    int pos = lista.primOcupada;
    while (pos != -1) {
        mostrarElemento(lista.almacen[pos].info);
        pos = lista.almacen[pos].sig;
    }
}

void construir(tLista *lista, tElemento e) {
    asignarElemento(&(lista -> almacen[lista -> primLibre].info), e);
    int aux = lista -> almacen[lista -> primLibre].sig;
    lista -> almacen[lista -> primLibre].sig = lista -> primOcupada;
    lista -> primOcupada = lista -> primLibre;
    lista -> primLibre = aux;
}

void crearVacia(tLista *lista, int max) {
    lista -> primLibre = 0;
    lista -> primOcupada = -1;
    for (int i = 0; i < max-1; ++i) {
        lista -> almacen[i].sig = i+1;
    }
    lista -> almacen[max-1].sig = -1;
}