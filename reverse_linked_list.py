class Node(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def add(self, node):
        pass

    def reverse(self):
        pass

    def __repr__(self):
        result = str(self.val)
        next_elem = self.next
        while next_elem:
            result += (" " + str(next.elem))
            next_elem = next_elem.next



