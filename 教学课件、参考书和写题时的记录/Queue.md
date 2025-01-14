```python
n=int(input())
t=[int(i) for i in input().split()]
t.sort()
wait=0
ans=0
for i in range(n):
    if t[i]>=wait:
        wait+=t[i]
        ans+=1

print(ans)
```



为什么可以直接这么写？按顺序排列后即使该人排队不满意，他所服务的时间也不需要算在整体服务事件中。

因为贪心算法，我们发现该人即使排在前面，依然不能让他满意，反而徒增时间，故在心里将其排到后面去，不用占用时间，而这个考虑没有在算法编辑上体现