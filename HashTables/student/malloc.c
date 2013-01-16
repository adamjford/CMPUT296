#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <limits.h>

static size_t gnCurrentMemory = 0;
static size_t gnPeakMemory    = 0;

void *MemAlloc (size_t nSize)
{
  void *pMem = malloc(sizeof(size_t) + nSize);

  if (pMem)
  {
    size_t *pSize = (size_t *)pMem;

    memcpy(pSize, &nSize, sizeof(nSize));

    gnCurrentMemory += nSize;

    if (gnCurrentMemory > gnPeakMemory)
    {
      gnPeakMemory = gnCurrentMemory;
    }

    printf("PMemAlloc (%#X) - Size (%d), Current (%d), Peak (%d)\n",
        (unsigned int)pSize + 1, nSize, gnCurrentMemory, gnPeakMemory);

    return(pSize + 1);
  }

  return NULL;
}

void  MemFree (void *pMem)
{
  if(pMem)
  {
    size_t *pSize = (size_t *)pMem;

    // Get the size
    --pSize;

    assert(gnCurrentMemory >= *pSize);

    printf("PMemFree (%#X) - Size (%d), Current (%d), Peak (%d)\n",
        (unsigned int)pMem,  *pSize, gnCurrentMemory, gnPeakMemory);

    gnCurrentMemory -= *pSize;

    free(pSize);
  }
}
