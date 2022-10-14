#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int x = 1;

void hola(int signalNumb)
{
    printf("Recibi la senal %d\n", signalNumb);
}

void terminarWhile(int signalNumb)
{
    printf("Terminando while \n");
    x = 0;
}

int main()
{
    signal(12, terminarWhile);
    signal(2, hola);
    while (x == 1)
    {
        printf("Trabajando\n");
        sleep(1);
    }
    printf("Aqui nunca llega\n");
    return 0;
}
