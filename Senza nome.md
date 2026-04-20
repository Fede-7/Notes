With functionplot Block
```functionplot
---
title: string
xLabel: string
yLabel: string
bounds: array[min x, max x, min y, max y]
disableZoom: boolean
grid: boolean
---
<name>(variable)=<expression>
```
Example:

```functionplot
---
title: The random graph
xLabel: Time
yLabel: Cost
bounds: [0, 10, 0, 50]
disbaleZoom: 1
grid: true
---
g(x)=x^PI
f(x)=E+log(x)*2
```

