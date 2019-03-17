# 績效指標

## Higher Order omega
Higher Order omega(N-order Omega)

1. 由來和發明人:
Sharpe ratio雖然簡單易懂，但較適用於資產為常態分配型態，更無法描述投資者除了mean、variance(亦即一階、二階的性質)的偏好，如:skewness、kurtosis就沒被考量進去。學者逐漸考量更多資產分布的高階性質作為衡量好壞的依據。
指標的發明人：曾郁仁教授及其他台陸教授。

2. 依據何種財務理論
財務理論、想法依據:
* Omega--Keating and Shadwick (2002)
* 以目標報酬的資產來評價--Bernardo and Ledoit (2000)
* acceptance domain--Hart (2011)
* Nth-degree stochastic dominance (NSD)--Caballé and Pomansky (1996)
* almost Nth-degree stochastic dominance (ANSD) -- Tzeng et al. (2013)

a.Acceptance domain:
有兩個分配F、G，對特定的決策者群，若F優於G表示:只要拒絕F的情形下，鐵定會拒絕G。
理論探討決策者限於:風險趨避者。
b.NSD:
所有混合風險趨避的決策者會考量其資產的N階性質。
如果F以NSD優於G，代表在1至N階的G(x)的值皆大於同階的F(x)值。
c.Omega ratio:
最簡單的一階版本，應用Nth-degree stochastic dominance (NSD)的概念。Omega是以比例值衡量資產表現的指標，分子為超過目標資產的機率權重，分母為低於目標資產的機率權重。
d.ANSD:
兩個分配F、G比較轉為分別透過一個基準目標資產的比較而定。若F優於G，則可知在F劣於基準L時，G必定劣於L。

此指標以Hart (2011)角度出發，修改了比較兩資產的拒絕情形，轉為單一資產與簡單的常數報酬的目標資產去做比較(ANSD)。根據Bernardo and Ledoit (2000)和Tzeng et al. (2013)的論文觀點，在考慮非理性投資者的偏好下，很難找出衡量好壞的共同準則，因此指標排除非理智投資者的偏好習性去建立新的Acceptance domain。



3.內涵、如何計算
N-oreder Omega能以資產的高階性質去做好壞的分類，對於不同需求的投資者，可以衡量不同的階層的Omega。

直覺上:若微分，則兩資產的函數差異變化度會越微越接近(高次方降到低次)，而積分反其道而行，把變化的效果擴大。意即越高階的Omega，越敏感的看待兩函數機率累積函數的增長情形。

定義 Nth-Order Omega:






4.有哪些機構使用:
由於高階Omega論文還很新，目前找不到有機構使用。
但Omega ratio在避險基金及數學軟體說明書中已經有使用。(如:eVestment、Maple)


# 巴菲特指標

簡介
* https://statementdog.com/explain/BuffettIdx.html

* https://www.macromicro.me/collections/34/us-stock-relative/406/us-buffet-index-gspc
* https://wilshire.com/indexcalculator/index.html

