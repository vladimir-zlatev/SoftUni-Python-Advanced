n, m = [int(x) for x in input().split()]

n_set = set()
m_set = set()

for _ in range(n):
    number = int(input())
    n_set.add(number)

for _ in range(m):
    number = int(input())
    m_set.add(number)

intersection_n_m = n_set.intersection(m_set)

print(*intersection_n_m, sep="\n")