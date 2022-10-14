#include <unistd.h>
#include <ctype.h>

int main()
{
    char c, may;
    int n;

    do
    {
        n = read(STDIN_FILENO, &c, 1);
        may = toupper(c);
        if (may == 'A' || may == 'E' || may == 'I' || may == 'O' || may == 'U')
        {
            c = '1';
        }
        write(STDOUT_FILENO, &c, 1);
    }
    while (n != 0);
    return 0;
}
