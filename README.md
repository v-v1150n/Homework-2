# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> 
    * Profitable Path: 'tokenB' -> 'tokenA' -> 'tokenE' -> 'tokenD' -> 'tokenC' -> 'tokenB'
    * AmountIn and AmountOut for each swap:
    * Swap 1: 'tokenB' -> 'tokenA': AmountIn = 5 ether, AmountOutMin = 5.655321988655322 ether
    * Swap 2: 'tokenA' -> 'tokenE': AmountIn = 5.655321988655322 ether, AmountOutMin = 1.0583153138066885 ether
    * Swap 3: 'tokenE' -> 'tokenD': AmountIn = 1.0583153138066885 ether, AmountOutMin = 2.429786260142227 ether
    * Swap 4: 'tokenD' -> 'tokenC': AmountIn = 2.429786260142227 ether, AmountOutMin = 5.038996197252911 ether
    * Swap 5: 'tokenC' -> 'tokenB': AmountIn = 5.038996197252911 ether, AmountOutMin = 20.042339589188174 ether
    * Final Reward (tokenB balance): 20.042339589188176107
*********************************************************************************************************************
## 3.4 Bonus
> 
    * Profitable Path: 'tokenB' -> 'tokenA' -> 'tokenE' -> 'tokenD' -> 'tokenC' -> 'tokenB' -> 'tokenA' -> 'tokenE' -> 'tokenD' -> 'tokenC' -> 'tokenB'
    * AmountIn and AmountOut for each swap:
    * Swap 1: 'tokenB' -> 'tokenA': AmountIn = 5 ether, AmountOutMin = 5.655321988655322 ether
    * Swap 2: 'tokenA' -> 'tokenE': AmountIn = 5.655321988655322 ether, AmountOutMin = 1.0583153138066885 ether
    * Swap 3: 'tokenE' -> 'tokenD': AmountIn = 1.0583153138066885 ether, AmountOutMin = 2.429786260142227 ether
    * Swap 4: 'tokenD' -> 'tokenC': AmountIn = 2.429786260142227 ether, AmountOutMin = 5.038996197252911 ether
    * Swap 5: 'tokenC' -> 'tokenB': AmountIn = 5.038996197252911 ether, AmountOutMin = 20.042339589188174 ether
    * Swap 6: 'tokenB' -> 'tokenA': AmountIn = 20.042339589188174 ether, AmountOutMin = 11.329971492240169 ether
    * Swap 7: 'tokenA' -> 'tokenE': AmountIn = 11.329971492240169 ether, AmountOutMin = 1.7488215291683533ether
    * Swap 9: 'tokenE' -> 'tokenD': AmountIn = 1.7488215291683533 ether, AmountOutMin = 3.9117621193960037 ether
    * Swap 10: 'tokenD' -> 'tokenC': AmountIn = 3.9117621193960037 ether, AmountOutMin = 7.358528776066261 ether
    * Swap 11: 'tokenC' -> 'tokenB': AmountIn = 7.358528776066261 ether, AmountOutMin = 23.297614378159203 ether
    * Final Reward (tokenB balance): 23.297614378159203



## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.
**********************************************************************************************************************
> 
Slippage in Automated Market Makers (AMM) refers to the difference between the expected price of a trade and the actual executed price. It occurs because the price of assets in an AMM is determined by the ratio of the asset reserves in the liquidity pool, and when a trade is executed, the pool's reserves change, causing the price to move.

Uniswap V2 addresses the slippage issue by implementing a mechanism called the constant product formula. This formula ensures that the product of the reserve amounts of the two tokens in a liquidity pool remains constant before and after a trade. As a result, the price of tokens adjusts dynamically based on the trade volume, minimizing slippage.

solidity
``` 
function swapExactTokensForTokens(
    uint amountIn, // The exact amount of input tokens to swap
    uint amountOutMin, // The minimum amount of output tokens expected
    address[] calldata path, // An array of token addresses representing the swap path
    address to, // The address to receive the output tokens
    uint deadline // The deadline for the swap to be executed
) external returns (uint[] memory amounts);
``` 
In this function:

`amountIn`  represents the exact amount of input tokens the user wants to swap.
`amountOutMin` specifies the minimum amount of output tokens that the user is willing to accept. This parameter helps protect users from excessive slippage.
`path` is an array of token addresses representing the swap path. For example, if swapping from token A to token B, the path would be `[tokenA, tokenB]`.
`to` is the address that will receive the output tokens after the swap.
`deadline` specifies the deadline for the swap to be executed. If the transaction is not confirmed before the deadline, it will revert.

By allowing users to specify a minimum output amount (amountOutMin), Uniswap V2 ensures that traders have control over the maximum slippage they are willing to accept. If the actual output amount is lower than the specified amountOutMin, the swap will revert, protecting the trader from excessive slippage.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?
**********************************************************************************************************************
> 
In the UniswapV2Pair contract, the mint function is used to create initial liquidity and issue LP tokens. During the creation of initial liquidity, a certain amount of minimum liquidity is subtracted from the accounts of each trading party.

The rationale behind this design is to ensure that liquidity providers bear a certain degree of responsibility and participation in the healthy operation of the liquidity pool. Without the requirement of minimum liquidity, certain liquidity providers might add liquidity to the pool just to extract one-time profits and then immediately withdraw their funds. This practice would adversely affect the stability and reliability of the liquidity pool.

Additionally, without minimum liquidity requirements, there might be an influx of meaningless liquidity provision, leading to instability and price fluctuations in the trading pair.

Therefore, by requiring liquidity providers to add at least a certain amount of minimum liquidity, the UniswapV2Pair contract ensures the stability and sustainability of the liquidity pool. Liquidity providers need to assume a certain level of risk while also benefiting from transaction fees, thereby incentivizing their long-term participation in liquidity provision.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?
**********************************************************************************************************************
> 
The intention behind the specific formula used in the minting function of the UniswapV2Pair contract for depositing tokens (not for the first time) is to ensure that the liquidity provided is proportional to the value of the tokens being deposited. This formula calculates the amount of LP tokens to be minted based on the amount of tokens deposited and the existing balances of tokens in the liquidity pool.

By using this formula, Uniswap V2 aims to maintain the balanced distribution of liquidity in the pool relative to the trading pair's token balances. This helps prevent potential manipulation or imbalance in the liquidity pool, which could lead to impermanent loss for liquidity providers and reduce the efficiency and effectiveness of the automated market maker (AMM) system.

Furthermore, this formula ensures that liquidity providers are incentivized to contribute liquidity in a way that reflects the actual market demand for the trading pair. It discourages excessive or arbitrary liquidity provision that could destabilize the pool and impact trading performance.

Overall, the intention behind using a specific formula for minting LP tokens during token deposits in the UniswapV2Pair contract is to maintain liquidity pool stability, efficiency, and fairness, ultimately benefiting both liquidity providers and traders using the Uniswap platform.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?
**********************************************************************************************************************
> 
A sandwich attack is a manipulation strategy aimed at decentralized exchanges (DEXs), designed to illicitly profit from traders. Attackers execute a series of rapid trades before and after a target transaction to exploit price fluctuations.

The general process of a sandwich attack includes:

* Observing Target Transaction: Attackers monitor an impending transaction, noting the tokens and quantities involved.

* Front-Running Trade: The attacker executes a trade before the target transaction, often in the same trading pair. This trade temporarily impacts the price, but the attacker can act swiftly before the target transaction occurs.

* Target Transaction: The attacker swiftly executes their own trade as the target transaction takes place, often at a more favorable price. Due to the influence of the front-running trade, the target transaction's price is affected, allowing the attacker to buy at a lower price or sell at a higher price.

*Back-Running Trade: After the target transaction concludes, the attacker executes another trade to correct the price back to its normal level. This maximizes the attacker's profit.

A sandwich attack can impact traders in the following ways:

* Increased Price Slippage: Rapid trades by attackers can cause significant price fluctuations in a short period, making it difficult for traders to execute transactions at their intended prices and increasing price slippage.

* Increased Trading Costs: Due to price volatility, traders may incur higher trading costs, especially in rapidly changing market conditions.

* Failed Transactions: In volatile price conditions, traders' orders may fail to execute as planned or execute at unfavorable price levels, leading to failed transactions or undesirable outcomes.

To mitigate the impact of sandwich attacks, decentralized exchanges may implement various measures, including increasing trading depth, implementing anti-manipulation measures, providing more liquidity, and improving trading algorithms. Additionally, traders can reduce the risk of being affected by attacks by choosing trading timeframes, using limit orders, and minimizing large trades.

