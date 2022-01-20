#include "sort.h"
/**
 * merge_sort - sort an array using the algo merge sort
 * @array: The array to sort
 * @size: The size of the array
 */
void merge_sort(int *array, size_t size)
{
	int *copy;
	size_t i = 0;

	copy = malloc(sizeof(int) * size);

	for (i = 0; i < size; i++)
		copy[i] = array[i];

	split(array, 0, size, copy);
	free(copy);
}
/**
 *split - split an array
 *@array: array to sort
 *@copy: copy of the array to sort
 *@start: starting index of the array
 *@end: ending index of the array
 */
void split(int *array, int start, int end, int *copy)
{
	int middle = (start + end) / 2;
	int pointer = 0;

	if (end - start <= 1)
		return;

	split(copy, start, middle, array);
	split(copy, middle, end, array);
	printf("Merging...\n");

	printf("[left]: ");
	for (pointer = start; pointer < middle; pointer++)
	{
		printf("%d", copy[pointer]);
		if (pointer < middle - 1)
			printf(", ");
	}

	printf("\n[right]: ");
	for (pointer = middle; pointer < end; pointer++)
	{
		printf("%d", copy[pointer]);
		if (pointer < end - 1)
			printf(", ");
	}

	merge(array, start, middle, end, copy);

	printf("\n");
	printf("[Done]: ");
	for (pointer = start; pointer < end; pointer++)
	{
		printf("%d", array[pointer]);
		if (pointer < end - 1)
			printf(", ");
	}
	printf("\n");
}
/**
 * merge - merge two arrays
 * @array: the array to sort
 * @copy: copy of the array to sort
 * @start: starting index
 * @end:  ending index
 * @mid: middle index
 */
void merge(int *array, int start, int mid, int end, int *copy)
{
	int s = start;
	int m = mid;
	int pointer = 0;

	for (pointer = start; pointer < end; pointer++)
	{

		if (s < mid && (m >= end || copy[s] <= copy[m]))
		{
			array[pointer] = copy[s];
			s = s + 1;
		}
		else
		{
			array[pointer] = copy[m];
			m = m + 1;
		}
	}
}
