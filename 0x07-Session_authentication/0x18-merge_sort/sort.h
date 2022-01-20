#ifndef _SORT_H_
#define _SORT_H_
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
void print_array(const int *array, size_t size);
void merge_sort(int *array, size_t size);
void merge(int *array, int start, int mid, int end, int *copy);
void split(int *array, int start, int end, int *copy);
#endif
