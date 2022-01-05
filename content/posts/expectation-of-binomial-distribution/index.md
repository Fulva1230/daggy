---
title: "Expectation of Binomial Distribution"
date: 2022-01-05T20:23:55+08:00
draft: false
---

Consider a binomial distribution \\(X\\) with parameters \\(n\\) and \\(p\\). Its probability mass function is
$$
p\left(x\right)=\begin{cases}
\frac{n!}{\left(n-x\right)!x!}p^{x}\left(1-p\right)^{n-x} & 0\leq x\leq n\\\\
0 & \text{otherwise}.
\end{cases}
$$

It's expectation is given by
$$
\begin{align*}
E\left[X\right] & =\sum_{x=0}^{n}xp\left(x\right)\\\\
 & =\sum_{x=1}^{n}\frac{n!x}{\left(n-x\right)!x!}p^{x}\left(1-p\right)^{n-x}\\\\
 & =\sum_{x=1}^{n}np\frac{\left(n-1\right)!}{\left(n-x\right)!\left(x-1\right)!}p^{\left(x-1\right)}\left(1-p\right)^{n-x}\\\\
 & =np\sum_{x=1}^{n}\frac{\left(n-1\right)!}{\left(n-x\right)!\left(x-1\right)!}p^{\left(x-1\right)}\left(1-p\right)^{n-x}\\\\
 & =np.
\end{align*}
$$

Note that if \\(Y\\) is a binomial distribution with parameter \\(n-1\\)
and \\(p\\), it has probability mass function as
\\[
p_{Y}\left(y\right)=\begin{cases}
\frac{\left(n-1\right)!}{\left(n-y\right)!y!}p^{y}\left(1-p\right)^{\left(n-1\right)-y} & 0\leq y\leq n-1\\\\
0 & \text{otherwise}
\end{cases}
\\]

So
\begin{align*}
E\left[X\right] & =np\sum_{y=0}^{n-1}\frac{\left(n-1\right)!}{\left(n-y\right)!y!}p^{y}\left(1-p\right)^{\left(n-1\right)-y}\\\\
 & =np\sum_{y=0}^{n-1}p_{Y}\left(y\right)\\\\
 & =np.
\end{align*}
