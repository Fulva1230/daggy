---
title: "Max Min Expectation"
date: 2022-02-27T12:13:46+00:00
draft: false
format:
  hugo:
    html-math-method: mathjax
---



## Question

If $X_{1},X_{2},...X_{n}$ are independent and identically distributed
random variables having uniform distributions over $(0,1)$, find

(a). $E\left[\max\left(X_{1},...,X_{n}\right)\right]$;

(b). $E\left[\min\left(X_{1},...,X_{n}\right)\right]$

## Answer

### a.

The joint probability density function is
<p>
$$
f_{X_{1},X_{2},...,X_{n}}\left(x_{1},x_{2},...,x_{n}\right)=\begin{cases}
1 & \text{if }x_{1},x_{2},...,x_{n}\in[0,1]\\
0 & \text{otherwise}.
\end{cases}
$$
</p>
The re-ordered joint probability density function is
<p>
<span id="eq-new-pdf">$$
f_{\hat{X}_{1},\hat{X}_{2},...,\hat{X}_{n}}\left(x_{1},x_{2},...,x_{n}\right)=\begin{cases}
n! &amp; \text{if }0&lt;x_{1}&lt;x_{2}&lt;,...,&lt;x_{n}&lt;1\\
0 &amp; \text{otherwise}
\end{cases}
 \qquad(1)$$</span>
</p>

We can make use of the new pdf given in [Equation 1](#eq-new-pdf),
considering

<p>
$$
\begin{align*}
E\left[\max\left(X_{1},...,X_{n}\right)\right] & =E\left[\hat{X}_{n}\right]\\
 & =\int_{0}^{1}\int_{0}^{x_{n}}\int_{0}^{x_{n-1}}...\int_{0}^{x_{2}}x_{n}f_{\hat{X}_{1},\hat{X}_{2},...,\hat{X}_{n}}\left(x_{1},x_{2},...,x_{n}\right)dx_{1}...dx_{n-2}dx_{n-1}dx_{n}\\
 & =\int_{0}^{1}\int_{0}^{x_{n}}\int_{0}^{x_{n-1}}...\int_{0}^{x_{2}}x_{n}n!dx_{1}...dx_{n-2}dx_{n-1}dx_{n}\\
 & =\int_{0}^{1}x_{n}n!\frac{x_{n}^{n-1}}{\left(n-1\right)!}dx_{n}=\int_{0}^{1}nx^{n}dx_{n}=\frac{n}{n+1}
\end{align*}
$$
</p>

Then we find the answer.

### b.

For the expection of the minimum, considering
<p>
$$
\begin{align*}
E\left[\min\left(X_{1},...,X_{n}\right)\right] & =E\left[\hat{X}_{1}\right]\\
 & =\int_{0}^{1}\int_{0}^{x_{n}}\int_{0}^{x_{n-1}}...\int_{0}^{x_{2}}x_{1}f_{\hat{X}_{1},\hat{X}_{2},...,\hat{X}_{n}}\left(x_{1},x_{2},...,x_{n}\right)dx_{1}...dx_{n-2}dx_{n-1}dx_{n}\\
 & =n!\int_{0}^{1}\int_{0}^{x_{n}}\int_{0}^{x_{n-1}}...\int_{0}^{x_{2}}x_{1}dx_{1}...dx_{n-2}dx_{n-1}dx_{n}\\
 & =n!\frac{1}{\left(n+1\right)!}\\
 & =\frac{1}{n+1}
\end{align*}
$$
</p>
