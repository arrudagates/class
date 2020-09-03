#include <stdio.h>

// Gabriel Facco de Arruda 31/08/2020

//2.13) Faça um algoritmo que receba uma temperatura e Celsius,
//calcule e mostre essa temperatura em Fahrenheit. Sabe-se que F
//= 180 (C + 32) / 100.

void main()
{
    float tempc, tempf;
    printf("Informe a temperatura e pressione enter para converter: ");
    scanf("%f", &tempc);

    tempf = (tempc / 100) * 180 + 32;
    printf("A conversao para Fahrenheit resulta em: %.2f °F.", tempf);
}
