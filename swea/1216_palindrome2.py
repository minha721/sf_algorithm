for test_case in range(10):
    T = int(input())

    def find_max_len(arr):
        cur_max = 0
        for start in range(100):
            for end in range(start + 1, 100):
                s = arr[start:end + 1]
                if s == s[::-1]:
                    cur_max = max(cur_max, len(s))

        return cur_max


    graph = []
    for i in range(100):
        row = input()
        graph.append(list(row))
    col_graph = list(map(list, zip(*graph)))

    res = -1

    for i in range(100):
        res = max(res, find_max_len(graph[i]))
        res = max(res, find_max_len(col_graph[i]))

    print("#{} {}".format(T, res))