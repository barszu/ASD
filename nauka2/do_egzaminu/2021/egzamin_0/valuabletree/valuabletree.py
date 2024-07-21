from zad2testy import runtests
from math import inf

class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane


def valuableTree(T, k):
    """
    Function to find the most valuable tree.

    Parameters:
    T (Node): Root of the tree.
    k (int): Number of edges to be considered.

    Returns:
    int: Maximum value of the tree considering k edges.
    """

    if k == 0: return 0
    if k < 0 or not T: return None

    def f(node, i):
        """
        Helper function to calculate the maximum value of the tree.

        Parameters:
        node (Node): Current node.
        i (int): Number of edges to be considered from the current node.

        Returns:
        int: Maximum value of the tree considering i edges from the current node.
        """

        nonlocal k
        if node is None:
            return -inf
        if i == 0:
            return 0
        if node.left is None and node.right is None and i != 0:
            return - inf
        if node.X is not None and node.X[i] is not None:
            return node.X[i]

        #max biorac lewe/prawe poddrzewo
        res = max(node.leftval + f(node.left, i-1), node.rightval + f(node.right, i-1))

        for j in range(i-1):
            # suma z lewego podrzewa , prawego poddrzewa (j zalezne od rozlozenia)
            res = max(res, node.leftval + node.rightval + f(node.left, j) + f(node.right, i-2-j))

        if node.X is None: node.X = [None]*(k+1)
        node.X[i] = res
        return node.X[i]

    def getSol(root, k):
        """
        Helper function to update the maximum value of the tree.

        Parameters:
        root (Node): Current root of the tree.
        k (int): Number of edges to be considered.

        """

        nonlocal sol
        res = f(root, k)
        sol = max(sol, res)
        if root.left is not None: getSol(root.left, k)
        if root.right is not None: getSol(root.right, k)

    sol = -inf
    getSol(T,k)
    return sol


runtests(valuableTree)