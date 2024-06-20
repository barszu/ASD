# parzyste stopnie kazdego wierzcholka

# visited -> krawedzie

def find_euler_cycle_non_rek(G):
    cycle = []
    stack = [0]
    
    while stack:
        u = stack[-1]
        if len(G[u]) > 0: #idz du dzieciom priorytetowo
            v = G[u].pop() #usuniecie krawedzi, jesli ide nia
            stack.append(v)
        else: #bez dzieci wiec uselless
            cycle.append(u)
            stack.pop()
            
    return cycle[::-1]