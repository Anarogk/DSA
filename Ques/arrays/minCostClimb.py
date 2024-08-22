

def minCostClimbingStairs(cost) -> int:
    end = len(cost)
    cost.extend([0,0]) # cost [1,100,1,1,1,100,1,1,100,1,0,0]
    for i in range(end):
        end -= 1 
        cost[end] = min(cost[end + 1],cost[end + 2]) + cost[end]
    return min(cost[0],cost[1])
            


# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

def main():
    cost = [10, 15, 20]
    cost_1 = [1,100,1,1,1,100,1,1,100,1]

    print("This is the min cost to climb stairs:",minCostClimbingStairs(cost))
    print("This is the min cost to climb stairs:",minCostClimbingStairs(cost_1))


if __name__ == "__main__":
    main()