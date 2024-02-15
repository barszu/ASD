class IntervalNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

def build_interval_tree(intervals):
    def build_tree(intervals, start, end):
        if start > end:
            return None

        root = IntervalNode(start, end)

        if start == end:
            return root

        mid = (start + end) // 2
        root.left = build_tree(intervals, start, mid)
        root.right = build_tree(intervals, mid + 1, end)

        return root

    return build_tree(intervals, min(intervals), max(intervals))

def update_interval_tree(node, start, end, val):
    if start > end or not node:
        return

    if node.start == start and node.end == end:
        node.total += val
        return

    mid = (node.start + node.end) // 2

    if end <= mid:
        update_interval_tree(node.left, start, end, val)
    elif start > mid:
        update_interval_tree(node.right, start, end, val)
    else:
        update_interval_tree(node.left, start, mid, val)
        update_interval_tree(node.right, mid + 1, end, val)

    node.total = node.left.total + node.right.total

def query_interval_tree(node, start, end):
    if not node or start > end:
        return 0

    if node.start == start and node.end == end:
        return node.total

    mid = (node.start + node.end) // 2

    if end <= mid:
        return query_interval_tree(node.left, start, end)
    elif start > mid:
        return query_interval_tree(node.right, start, end)
    else:
        left_total = query_interval_tree(node.left, start, mid)
        right_total = query_interval_tree(node.right, mid + 1, end)
        return left_total + right_total

def update_interval_tree_add(node, start, end, val):
    if start > end or not node:
        return

    if node.start == start and node.end == end:
        node.total += val
        return

    mid = (node.start + node.end) // 2

    if end <= mid:
        update_interval_tree_add(node.left, start, end, val)
    elif start > mid:
        update_interval_tree_add(node.right, start, end, val)
    else:
        update_interval_tree_add(node.left, start, mid, val)
        update_interval_tree_add(node.right, mid + 1, end, val)

    node.total = node.left.total + node.right.total

intervals = [1, 5, 8, 12, 15] # 1->5->8->12->15 #[1-5] #musze tu miec wszystkie granice (starty) przedzialow
root = build_interval_tree(intervals)
update_interval_tree_add(root, 1, 5 , 12)
update_interval_tree_add(root, 1, 5 , 13)
update_interval_tree_add(root, 11, 15  , 100)
result = query_interval_tree(root, 1, 14.9)
print(result)  # Wyświetli sumę przedziału od 1 do 8