# 専門用語自動抽出Pythonモジュールtermextract
(Original Implementation of TermExtract)

cf. http://gensen.dl.itc.u-tokyo.ac.jp/pytermextract/

## 左右名詞の接続頻度

- $`LN(N)`$：対象となる単名詞$`N`$の左辺に接続した名詞の出現頻度[の合計値]
- $`RN(N)`$：対象となる単名詞$`N`$の右辺に接続した名詞の出現頻度[の合計値]

## 左右名詞の接続種類数
- $`LDN(N)`$：対象となる単名詞$`N`$の左辺に接続した名詞の種類数
- $`RDN(N)`$：対象となる単名詞$`N`$の右辺に接続した名詞の種類数

## 複合語重要度スコア`LR`
複合名詞$`CN`$が単名詞$`N_1, N_2,\cdots, N_L`$順に接続した文字列とする。$`CN`$の重要度スコア$`LR`$は次のように求められる。

$$LR(CN)=\left( \Pi_{i=1}^L (LN(N_i)+1)(RN(N_i)+1)\right)^{\frac{1}{2L}}$$

## 出現頻度を考慮した複合語重要度スコア`FLR`
複合名詞$`CN`$が単名詞$`N_1, N_2,\cdots, N_L`$順に接続した文字列とする。出現頻度$`f(CN)`$を考慮した$`CN`$の重要度スコア$`FLR`$は次のように求められる。

$$FLR(CN)=f(CN) \times LR(CN)$$