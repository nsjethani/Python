import itertools, heapq
def top_k(k, stream):
    # entries are compared by their length
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    print(min_heap)
    heapq.heapify(min_heap)
    print("min heap", min_heap)
    for next_string in stream:
        print(min_heap)
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]

print(top_k(3, ["abcdefghi","b","neha",'Jay',"sutr","suresh"]))

l = ['neha','Jay','suresh']
print(l)
h = [(len(s),s) for s in itertools.islice(l, 3)]
print(h)
heapq.heapify(h)
print(h)
print(l)