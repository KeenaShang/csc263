"""
    Implementation of an data structure that can return or remove
     the median from a collection of orderable elements. Data structure
     also allows insertion.
"""


def insert(collection, x):
    """ Add element x to collection """
    # make deep copy of collection
    min_heap = build_min_heap(collection)
    min_heap.append(x)
    return min_heapify(collection)


def median(collection):
    """ Return the median of collection """

    return None


def extract_med(collection):
    """ Remove the median of collection and return its value"""

    return None



#============= HELPER FUNCTIONS =================

def build_min_heap(collection):
    """Returns a min heap

    Precondition: items in collection can be ordered

    """
    num_elements = len(collection)

    if num_elements < 2:
        return collection
    elif num_elements == 2:
        if collection[0] > collection[1]:
            temp = collection[0]
            collection[0] = collection[1]
            collection[1] = temp
        return collection
    else:                # choose root
        if collection[1] <= collection[2]:
            temp = collection[1]
            collection[1] = collection[2]
            collection[2] = temp
        else:
            temp = collection[0]
            collection[0] = collection[2]
            collection[2] = temp

    # build left and right subtrees
    left_subtree = [collection[1]]
    right_subtree = [collection[2]]

    i = 1
    while (2 * i + 4 < num_elements) and (i < num_elements):
        left_subtree.append(collection[2 * i + 1])
        left_subtree.append(collection[2 * i + 2])
        right_subtree.append(collection[2 * i + 3])
        right_subtree.append(collection[2 * i + 4])
        i += 2

    # recursively build min heap subtrees
    left_min_heap = build_min_heap(left_subtree)
    right_min_heap = build_min_heap(right_subtree)

    # reassemble subtrees with root
    almost_min_heap = [collection[0], left_min_heap[0], right_min_heap[0]]

    i = 1
    while (2 * i + 2 < min(len(left_min_heap), len(right_min_heap)))\
            and (i < min(len(left_min_heap), len(right_min_heap))):
        almost_min_heap.append(left_min_heap[2 * i + 1])
        almost_min_heap.append(left_min_heap[2 * i + 2])
        almost_min_heap.append(right_min_heap[2 * i + 2])
        almost_min_heap.append(right_min_heap[2 * i + 2])
        i += 2

    # min_heap = min_heapify(almost_min_heap)

    return almost_min_heap


def min_heapify(collection):
    """Returns a min heap

    Precondition: the left and right subtrees of collection
    must be min heaps

    """
    num_elements = len(collection)
    is_left = False

    if num_elements < 1:
        return collection
    elif num_elements == 2:
        if collection[0] > collection[1]:
            temp = collection[0]
            collection[0] = collection[1]
            collection[1] = temp
    elif (collection[0] >= collection[1]) and (collection[0] >= collection[2]):
        pass
    else:  # swap with largest child
        if collection[1] <= collection[2]:
            temp = collection[2]
            collection[2] = collection[0]
            collection[0] = temp
        else:
            temp = collection[1]
            collection[1] = collection[0]
            collection[0] = temp
            is_left = True

    if is_left:
        # build left subtree and recurse
        left_subtree = [collection[1]]

        bleh

        left_min_heap = min_heapify(left_subtree)

    else:
        # build right subtree and recurse
        right_subtree = [collection[2]]

        right_min_heap = min_heapify(right_subtree)

    min_heap = [collection[0]]


    # reassemble

def extract_min(collection):
    """Removes the minimum value from collection

    Precondition: collection must be a min heap

    """
