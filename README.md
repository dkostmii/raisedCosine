raisedCosine
============

Take a look how beautiful raised cosine is 😍

![Example plot](./img/example-screenshot.png)

**Red** - using implemented function value distribution

**Blue** - using exponent of time or `exp(-tt)` in project code

Initially the idea of project was to just plot the cardinal sine function.

But then I watched the [Solving the heat equation | DE3](https://youtu.be/ToIXSwZ1pJU) video from **3Blue1Brown** channel
and this inspired me to plot the graph of function value distribution through time.

This algorithm works fine for _non-symmetrical_ ranges, but for _symmetrical_ one it's just distributing straight
to the median value (because median in scope of this implemetation is the **fixed point**).

![Example showing distribution to the median](./img/disadvantage-screenshot.png)
