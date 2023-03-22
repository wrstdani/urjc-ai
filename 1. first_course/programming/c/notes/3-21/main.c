#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 255

// Ponemos los "enum" arriba para que se puedan utilizar en las funciones
enum interruptor {
    ENCENDIDO,
    APAGADO
};
enum diasSemana {
    LUNES = 1,
    MARTES = 2,
    MIERCOLES = 3,
    JUEVES = 4,
    VIERNES = 5,
    SABADO = 6,
    DOMINGO = 7
};

struct tStudent {
    char nombre[MAX];
    int nExp;
    int notaMedia;
};

typedef struct date {
    unsigned short day;
    char month[20];
    unsigned short year;
} typeDate;

typedef struct alumno {
    char nombre[MAX];
    typeDate birthDate;
    unsigned long nExp;
} typeAlumno;

typedef struct {
    unsigned short x;
    unsigned short y;
    unsigned short z;
} typePunto;

void funInterruptor(enum interruptor varInterruptor);

void funStudent(struct tStudent student1);

void funDate(typeDate date1);

void funAlumno(typeAlumno alumnno1);

void funPunto(typePunto punto1);

void funArrPuntos(typePunto arrPuntos[]);

int main(int argc, char *argv[]) {
    enum interruptor varInterruptor;
    struct tStudent student1;
    typeDate date1;
    typeAlumno alumno1;
    typePunto punto1;

    if (argc < 2) printf("Dame argumentos. \n");

    else {
        switch (*argv[1]) {
            case '1':
                funInterruptor(varInterruptor);
                break;
            case '2':
                funStudent(student1);
                break;
            case '3':
                funDate(date1);
                break;
            case '4':
                funAlumno(alumno1);
                break;
            case '5':
                funPunto(punto1);
                break;
            case '6':

            default:
                printf("Me diste un argumento no valido. \n");
        }
    }

    return 0;
}

void funInterruptor(enum interruptor varInterruptor) {
    varInterruptor = APAGADO;

    printf("El interruptor esta %i.", varInterruptor);
}

void funStudent(struct tStudent student1) {
    char nameInput[MAX];
    int exp;
    int grade;

    printf("Escribe tu nombre:");
    gets(nameInput);
    printf("Escribe tu numero de expediente:");
    scanf("%i", &exp);
    printf("Escribe la nota media sobre 10:");
    scanf("%i", &grade);

    strcpy(student1.nombre, nameInput);
    student1.nExp = exp;
    student1.notaMedia = grade;

    printf("El/la estudiante %s con numero de expediente %i tiene una nota media de %i. \n", student1.nombre, student1.nExp, student1.notaMedia);
}

void funDate(typeDate date1) {
    date1.day = 25;
    strcpy(date1.month, "Junio");
    date1.year = 2004;

    printf("%i de %s de %i. \n", date1.day, date1.month, date1.year);
}

void funAlumno(typeAlumno alumno1) {
    printf("Nombre del alumno:");
    gets(alumno1.nombre);
    printf("Fecha de nacimiento (separar por espacios, mes con letra):");
    scanf("%hi %s %hi", &alumno1.birthDate.day, alumno1.birthDate.month, &alumno1.birthDate.year);
    printf("Numero de expediente:");
    scanf("%lu", &alumno1.nExp);

    printf("Nombre: %s\n", alumno1.nombre);
    printf("Fecha de nacimiento: %hi de %s de %hi\n", alumno1.birthDate.day, alumno1.birthDate.month, alumno1.birthDate.year);
    printf("N. expediente: %lu\n", alumno1.nExp);
}

void funPunto(typePunto punto1) {
    printf("Coordenada X:");
    scanf("%hi", &punto1.x);
    printf("Coordenada Y:");
    scanf("%hi", &punto1.y);
    printf("Coordenada Z:");
    scanf("%hi", &punto1.z);

    printf("Punto 1: (%hi, %hi, %hi)", punto1.x, punto1.y, punto1.z);
}

void funArrPuntos(typePunto arrPuntos[int x]) {

}