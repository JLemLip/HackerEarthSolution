import numpy as np

def array_queries (N, M, A, B, Q, queries):
    # Write your code here
    ret = []
    ret.append(fun(A, B))
    current_val = ret[0]
    new_val = 0
    diff = 0
    for query in queries:
        A, B, diff = address_query(A, B, query)
        new_val = current_val - diff
        ret.append(new_val)
        current_val = new_val
    return ret

def address_query(A, B, query):
    X, Y = np.array(A), np.array(B)
    diff = 0
    old_val = 0
    new_val = 0
    operation = query[0]
    i = query[1] - 1
    j = query[2] - 1
    if operation == 1:
        old_val = X[i]*(np.sum(Y * np.array(list(range(i+2,i+2+len(Y))))))
        old_val += Y[j]*(np.sum(X * np.array(list(range(j+2,j+2+len(X))))))
        X[i], Y[j] = Y[j], X[i]
        new_val = X[i]*(np.sum(Y * np.array(list(range(i+2,i+2+len(Y))))))
        new_val += Y[j]*(np.sum(X * np.array(list(range(j+2,j+2+len(X))))))
    elif operation == 2:
        old_val = X[i]*(np.sum(Y * np.array(list(range(i+2,i+2+len(Y))))))
        old_val += X[j]*(np.sum(Y * np.array(list(range(j+2,j+2+len(Y))))))
        X[i], X[j] = X[j], X[i]
        new_val = X[i]*(np.sum(Y * np.array(list(range(i+2,i+2+len(Y))))))
        new_val += X[j]*(np.sum(Y * np.array(list(range(j+2,j+2+len(Y))))))
    elif operation == 3:
        old_val = Y[i]*(np.sum(X * np.array(list(range(i+2,i+2+len(X))))))
        old_val += Y[j]*(np.sum(X * np.array(list(range(j+2,j+2+len(X))))))
        Y[i], Y[j] = Y[j], Y[i]
        new_val = Y[i]*(np.sum(X * np.array(list(range(i+2,i+2+len(X))))))
        new_val += Y[j]*(np.sum(X * np.array(list(range(j+2,j+2+len(X))))))
    else:
        pass
    diff = old_val - new_val
    np.array(X).tolist()
    np.array(Y).tolist()
    return X, Y, diff

def fun(A, B):
    A = np.array(A)
    B = np.array(B)
    ret = 0
    
    for i in range(len(A)):
        np_arr = np.array(list(range(i + 2, i + 2 + len(B))))
        ret += A[i]*(np.sum(B * np_arr))

        if ret >= 998244353:
            ret -= 998244353
    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for i in range(Q)]

    out_ = array_queries(N, M, A, B, Q, queries)
    print (' '.join(map(str, out_)))
