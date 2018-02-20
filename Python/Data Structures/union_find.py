class Subset:
    parent = None
    rank = 0

class UnionFind(object):

    def find(self, subset, index):
        if (subset[index].parent != index):
            subset[index].parent = self.find(subset, subset[index].parent)

        return subset[index].parent

    def union(self, subset, first, second):
        first_root = self.find(subset, first)
        second_root = self.find(subset, second)

        if subset[first_root].rank < subset[second_root].rank:
            subset[first_root].parent = second_root
        elif subset[second_root].rank < subset[first_root].rank:
            subset[second_root].parent = first_root
        else:
            subset[first_root].parent = second_root
            subset[first_root].rank += 1

        return

