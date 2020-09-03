#include <stdio.h>

// Gabriel Facco de Arruda 31/08/2020

// 2.11) Faça um algoritmo que receba a quantidade de dinheiro em
// reais e converta esse valor em dólar, marco alemão e libras
// esterlinas. Pesquise o valor das cotações. Os valores convertidos
// devem ser formatados com 2 casas decimais e alinhados a
// direita.

void main()
{
    float real, dolar, marcoale, libraest;

    printf("Informe a quantidade de reais que deseja converter e pressione enter: ");
    scanf("%f", &real);

    dolar = real / 5.39;

    marcoale = real / 3.33;

    libraest = real / 7.20;

    printf("Quantidade de reais em Dolares: US$%.2f, em Marco Alemao: DEM%.2f, em Libra Esterlina: £%.2f.", dolar, marcoale, libraest);

}
