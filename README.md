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
The rationale behind subtracting minimum liquidity upon initial liquidity minting is to prevent users from creating liquidity pairs with very small amounts of liquidity. By requiring a minimum amount of liquidity to be provided, Uniswap V2 ensures that the liquidity pool is sufficiently deep to accommodate trading without excessive slippage.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?
**********************************************************************************************************************
> 
The intention behind using a specific formula to calculate liquidity when depositing tokens (not for the first time) is to incentivize liquidity providers to deposit their assets in a balanced manner. By requiring a specific ratio of tokens to be deposited relative to the existing pool reserves, Uniswap V2 encourages liquidity providers to maintain the stability and efficiency of the liquidity pool.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?
**********************************************************************************************************************
> 
A sandwich attack is a form of front-running where an attacker inserts their own transaction between two other transactions to exploit price differences. In the context of initiating a swap, a sandwich attack can lead to significant slippage and result in the trader receiving fewer tokens than expected. This can erode the profitability of the trade and potentially lead to financial losses for the trader.

