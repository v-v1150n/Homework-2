
def calculate(liquidity, initiontoken, path):
    token = initiontoken
    gasfee = 997
    gasnoo = 1000
    
    for i in range(len(path) - 1):
        token_from = path[i]
        token_to = path[i + 1]
        
        liq_from_to = liquidity.get((token_from, token_to))
        liq_to_from = liquidity.get((token_to, token_from))
        
        if liq_from_to and liq_to_from:
            token_to = (gasfee * token * liq_from_to[1]) / (gasfee * token + gasnoo * liq_from_to[0])
            token = token_to

    return token


def find_best_path(liquidity, initiontoken, target_tokenB):
    gasfee = 997
    gasnoo = 1000
    stack = [(["tokenB"], initiontoken)]
    while stack:
        path, current_tokenB = stack.pop()
        if current_tokenB >= target_tokenB:
            return path
        for (token_from, token_to), (liq1, liq2) in liquidity.items():
            if token_from == path[-1]:
                next_token = (gasfee * current_tokenB * liq2) / (gasfee * current_tokenB + gasnoo * liq1)
                stack.append((path + [token_to], next_token))
    return []


liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),

    ("tokenB", "tokenA"): (10, 17),
    ("tokenC", "tokenA"): (7, 11),
    ("tokenD", "tokenA"): (9, 15),
    ("tokenE", "tokenA"): (5, 21),
    ("tokenC", "tokenB"): (4, 36),
    ("tokenD", "tokenB"): (6, 13),
    ("tokenE", "tokenB"): (3, 25),
    ("tokenD", "tokenC"): (12, 30),
    ("tokenE", "tokenC"): (8, 10),
    ("tokenE", "tokenD"): (25, 60),
}

initiontoken = 5
target_tokenB = 20

best_path = find_best_path(liquidity, initiontoken, target_tokenB)
answer = calculate(liquidity, initiontoken, best_path)

print("Best path:", best_path)
print("Final tokenB:", answer)
