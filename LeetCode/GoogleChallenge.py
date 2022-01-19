
def solution(s):
    solutes = 0
    minions = {">": [],
               "<": []}
    for i in range(len(s)):
        if s[i] == ">":
            minions[">"].append(i)
        if s[i] == "<":
            minions["<"].append(i)
    for position in minions[">"]:
        gt_not_found = True
        while gt_not_found:
            if position < minions["<"][0]:
                break
            minions["<"].pop(0)
        solutes += (2*len(minions["<"]))
    return solutes

                
    
            
    

print(solution(">----<"))