from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])
def build_search_tree(nums, is_sorted=False):
    """Return a balanced binary search tree with the given nums
    at the leaves. is_sorted is True if nums already sorted.
    Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
    n = len(nums)
    if n == 1:
        tree = Node(nums[0], None, None) # A leaf
    else:
        mid = n // 2 # Halfway (approx)
        left = build_search_tree(nums[:mid], True)
        right = build_search_tree(nums[mid:], True)
        tree = Node(nums[mid - 1], left, right)
    return tree

print(build_search_tree([15, 3, 11, 21, 7, 0, 19, 33, 29, 4]))
print('\n')
print(sorted([15, 3, 11, 21, 7, 0, 19, 33, 29, 4]))