import sys

def get_neighbors(graph: {}, u):
  if u in graph:
    return [x for x in graph[u]]
  return []


def get_neighbors_from_pairs(pairs: [], u):
    neighbors = []
    for pair in pairs:
        pair = pair[:]
        if u in pair:
            pair.remove(u)
            neighbors.append(pair[0])
    neighbors.sort()
    return neighbors


def to_graph(pairs, graph):
    for pair in pairs:
        for peak in pair:
            if peak not in graph:
                graph[peak] = get_neighbors_from_pairs(pairs, peak)


def main():
    graph = {}
    pairs = [[int(peak) for peak in pair.split()] for pair in sys.stdin.read().split('\n')]
    to_graph(pairs, graph)

    stack = [1]
    neighbors = [1]
    while len(stack) != 0:
        print(*stack)
        is_new_peak = False
        for peak in get_neighbors(graph, stack[-1]):
            if peak not in neighbors and not is_new_peak:
                neighbors.append(peak)
                stack.append(peak)
                is_new_peak = True
        if not is_new_peak:
            stack.pop()


main()
