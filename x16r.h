#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

#ifdef _WIN32
void x16r_hash(char* input, char* output);
#else
void x16r_hash(void* input, void* output);
#endif

#ifdef __cplusplus
}
#endif
