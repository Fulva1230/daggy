---
title: "統計問題：會佔幾張桌子？"
date: 2022-01-13T20:59:42+08:00
draft: false
---
# 問題描述
*N*個人參加一個晚宴，他們依隨機的順序分別抵達晚宴會場，他們任一人到達晚宴時，會尋找他們是否有朋友已待在晚宴裡，如果有，就會與朋友共桌，如果沒有，則會自己坐一張還未有人佔的桌子邊。假設在這*N*個人中隨機挑兩人，會有*p*的機率兩人是朋友。問在*N*個人抵達會場後，會場被他們佔用的桌子數的期望值是多少。[^1]

# 解
{{< rawhtml >}}
這個問題只需要知道桌子數的期望值，所以比起用占用的桌子數當作隨機變數，可以用虛擬變量(Dummy variable) \(X_i\) ，定義為第 \(i\) 個抵達的人是否開新桌，是的話為1，不是則為0。因為第 \(i\) 個人要開新桌的條件為第 \(1..i-1\) 個人皆不是他朋友，它的Probability mass function就是
\[
p_{X_{i}}\left(x\right)=\begin{cases}
\left(1-p\right)^{i-1} & x=1\\
1-\left(1-p\right)^{i-1} & x=0\\
0 & \text{otherwise}
\end{cases},\text{for }i=1,2,...,N
\]
{{< /rawhtml >}}
這樣答案就會是
{{< rawhtml >}}
\begin{align*}
E\left[\sum_{i=1}^{N}X_{i}\right] & =\sum_{i=1}^{N}E\left[X_{i}\right]\\
 & =\sum_{i=1}^{N}\left(1-p\right)^{i-1}\\
 & =\frac{1-\left(1-p\right)^{N}}{1-\left(1-p\right)}\\
 & =\frac{1-\left(1-p\right)^{N}}{p}
\end{align*}
{{< /rawhtml >}}

[^1]: 來自 Ross, S. M. (2014). A first course in probability. Pearson P.373 Problem 7.8.