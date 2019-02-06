# Закодируйте любую строку из трех слов по алгоритму Хаффмана.

print('Тестовая строка:')
s = "code me please"
print(s)


class HNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def leaf(self):
        return (self.left, self.right)


def huffmantree(node, left=True, nodestr=""):
    if type(node) is str: # если не пустой
        return {node: nodestr}
    (left, right) = node.leaf()
    d = dict()
    d.update(huffmantree(left, True, nodestr + "0"))
    d.update(huffmantree(right, False, nodestr + "1"))
    return d


def huffmanencodes(str, d):
    word = ""
    for i in str:
        word += (d[i])
    return word

freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Сортировка будущего словаря
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq

while len(nodes) > 1:
    k1, c1 = nodes[-1]
    k2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = HNode(k1, k2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)


code_dict = huffmantree(nodes[0][0])
print(f"\nФраза в закодированнов виде:\n{huffmanencodes(s,code_dict)}")
print(f"\nСловарь для кодирования по Хаффману:\n{code_dict}")
