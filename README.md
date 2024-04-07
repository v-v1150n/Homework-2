# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Profitable Path: 'tokenB' -> 'tokenA' -> 'tokenE' -> 'tokenD' -> 'tokenC' -> 'tokenB'
AmountIn and AmountOut for each swap:
Swap 1: 'tokenB' -> 'tokenA': AmountIn = 5 ether, AmountOutMin = 5.655321988655322 ether
Swap 2: 'tokenA' -> 'tokenE': AmountIn = 5.655321988655322 ether, AmountOutMin = 1.0583153138066885 ether
Swap 3: 'tokenE' -> 'tokenD': AmountIn = 1.0583153138066885 ether, AmountOutMin = 2.429786260142227 ether
Swap 4: 'tokenD' -> 'tokenC': AmountIn = 2.429786260142227 ether, AmountOutMin = 5.038996197252911 ether
Swap 5: 'tokenC' -> 'tokenB': AmountIn = 5.038996197252911 ether, AmountOutMin = 20.042339589188174 ether
Final Reward (tokenB balance): 20042339589188176107

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Slippage in AMM refers to the difference between the expected price of a trade and the price at which the trade is executed. It occurs due to the dynamic nature of liquidity pools in AMMs, where larger trades can cause the price of a token to shift.
Uniswap V2 addresses this issue by using a mechanism called the Constant Product Market Maker Model. In this model, the product of the reserves of two tokens in a liquidity pool remains constant. When a trade occurs, it causes the reserves to rebalance in a way that the product remains the same. This ensures that the price impact of a trade is proportional to the trade size, mitigating slippage.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> The rationale behind subtracting minimum liquidity upon initial liquidity minting is to prevent users from creating liquidity pairs with very small amounts of liquidity. By requiring a minimum amount of liquidity to be provided, Uniswap V2 ensures that the liquidity pool is sufficiently deep to accommodate trading without excessive slippage.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> The intention behind using a specific formula to calculate liquidity when depositing tokens (not for the first time) is to incentivize liquidity providers to deposit their assets in a balanced manner. By requiring a specific ratio of tokens to be deposited relative to the existing pool reserves, Uniswap V2 encourages liquidity providers to maintain the stability and efficiency of the liquidity pool.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> A sandwich attack is a form of front-running where an attacker inserts their own transaction between two other transactions to exploit price differences. In the context of initiating a swap, a sandwich attack can lead to significant slippage and result in the trader receiving fewer tokens than expected. This can erode the profitability of the trade and potentially lead to financial losses for the trader.

