#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main()
{
    int pid = fork();

    if (pid == 0)
    {
        printf("Soy el proceso hijo\n");
        // execl("/workspace/TC1004B.514/hola", "hola", NULL);
        execlp("hola", "hola", NULL);
        sleep(5);
        printf("Nunca nunca nunca\n");
    }
    else
    {
        printf("Soy el proceso padre\n");
        wait(NULL);
    }

    return 0;
}