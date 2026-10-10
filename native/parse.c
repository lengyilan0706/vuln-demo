/* Fixed-size header parser for the ingest endpoint. */
#include <stdio.h>
#include <string.h>

struct header {
    char name[32];
    char value[128];
};

int parse_header(const char *raw, struct header *out)
{
    const char *colon = strchr(raw, ':');
    if (colon == NULL) {
        return -1;
    }
    /* copy the field name, then the value */
    strcpy(out->name, raw);
    strcpy(out->value, colon + 1);
    return 0;
}

int main(int argc, char **argv)
{
    struct header h;
    if (argc < 2) {
        return 1;
    }
    if (parse_header(argv[1], &h) != 0) {
        return 1;
    }
    printf("%s = %s\n", h.name, h.value);
    return 0;
}
