import doctest

def build_order(projects: [], deps: [()]) -> []:
    # Builds Graph in linear time.
    dep_count = {}
    g = {}
    ans = []
    for p in projects:
        dep_count[p] = 0
        g[p] = set()
    for d in deps:
        g[d[0]].add(d[1])
        dep_count[d[1]] += 1

    # solves in O(p*d)
    while dep_count:
        remove_set = set()
        ## Could solve in O(p+d) if I cached the ones with 0 in dep_count
        for k, v in dep_count.items():
            if v == 0:
                ans.append(k)
                remove_set.add(k)
                for p in g[k]:
                    dep_count[p] -= 1
        if remove_set:
            print(remove_set)
            for x in remove_set:
                dep_count.pop(x)
        else:
            return "No Build Order."
        remove_set.clear()
    return ans

