T = int(input())

for i in range(T):
    N = int(input())
    tree = [int(num) for num in input().split(&#x27; &#x27;)]

    #case 1 If path ends and starts at the same node, count that node only once.
    max_number = max(tree[len(tree)//2:])
   
    while len(tree) &gt; 3:
        n = len(tree) // 2 - 1

        for i in range(n // 2 + 1):
            #case 2 path doesn&#x27;t include the root
            temp_max = tree[n - i] + tree[(n + 1 - i) * 2] + tree[(n + 1 - i) * 2 - 1]
            max_number = temp_max if temp_max &gt; max_number else max_number

            #case 3 path includes the root
            tree[n - i] += max(tree[(n + 1 - i) * 2], tree[(n + 1 - i) * 2 - 1])

        tree = tree[:n + 1]

    print(max(sum(tree), max_number))
