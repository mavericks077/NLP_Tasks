import  numpy as np

if __name__ == '__main__':

    f = open('input_1.txt', 'r')
    edges = [line.strip('\n').split(' ')for line in f]
    print(edges)

    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])
        print(nodes)

        N = len(nodes)

    #将节点符号映射成阿拉伯数字，便于后面生成A/S矩阵
    i = 0
    node_to_num = {}
    for node in nodes:
        node_to_num[node] = i
        i += 1
    for edge in edges:
        edge[0] = node_to_num[edge[0]]
        edge[1] = node_to_num[edge[1]]
    print(edges)

    S = np.zeros([N, N])
    for edge in edges:
        S[edge[1], edge[0]] = 1
    print(S)

    #算法核心，包括PR计算和归一化处理
    for j in range(N):
        sum_of_col = sum(S[:,j])
        for i in range(N):
            S[i, j] /= sum_of_col
    print(S)

    alpha = 0.85
    A = alpha*S +(1-alpha) / N * np.ones([N,N])
    print(A)

    p_n = np.ones(N) / N
    p_n1 = np.zeros(N)

    e = 100000
    k = 0
    print('loop...')

    while e > 0.0000001:
        p_n1 = np.dot(A, p_n)
        e = p_n1 - p_n
        e = max(map(abs, e))
        p_n = p_n1
        k = k+1
        print('iteration %s:' %str(k), p_n1)

    print('final result: ', p_n)

    #最后还可以可视化一下这个有向图
    import networkx as nx
    import matplotlib.pyplot as plt

    if __name__ == '__main__':

        # 读入有向图，存储边
        f = open('input_1.txt', 'r')
        edges = [line.strip('\n').split(' ') for line in f]

        G = nx.DiGraph()
        for edge in edges:
            G.add_edge(edge[0], edge[1])
        nx.draw(G, with_labels=True)
        plt.show()
