#include "alloc.h"

void alloc_measure(unsigned VSIZE_RANGE, unsigned REPEAT, std::map<unsigned, float>& m) {
    ClockCounter time;
    float val;
    for (unsigned i = 0; i < VSIZE_RANGE; i++) {
        val = 0;
        for (unsigned j = 0; j < REPEAT; j++) {
            time.start();
            int* arr = new int[i + 1]; 
            val += time.stop();
            delete[] arr;
        }
        val = val / REPEAT;
        m[i] = val;
    }
}
