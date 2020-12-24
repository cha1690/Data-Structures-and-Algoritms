def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if len(gas)==0 or len(cost)==0 or sum(gas) < sum(cost):
        return -1
    position=balance=0
    for i in range(len(gas)):
        balance += gas[i]-cost[i]
        if balance<0:
            balance=0
            position=i+1
    return position