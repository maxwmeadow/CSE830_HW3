from q5.insertion_sort import insertion_sort
from q5.merge_sort import merge

def hybrid_sort(collection: list, k: int) -> list:
    if len(collection) <= max(k, 1):
        return insertion_sort(collection)

    mid = len(collection) // 2
    left = hybrid_sort(collection[:mid], k)
    right = hybrid_sort(collection[mid:], k)
    return merge(left, right)