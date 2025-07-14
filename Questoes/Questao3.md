
# 879. Profitable Schemes

**Difficulty**: Hard  
**Topics**: Dynamic Programming  
**Links**: [Questão 3](https://leetcode.com/problems/profitable-schemes/description/)  

There is a group of `n` members, and a list of various crimes they could commit. The `i`th crime generates a `profit[i]` and requires `group[i]` members to participate in it.  
If a member participates in one crime, that member can't participate in another crime.

A **profitable scheme** is any subset of these crimes that:
- Generates **at least** `minProfit` profit, and
- Uses **at most** `n` members.

Return the **number of schemes** that can be chosen. Since the answer may be very large, return it modulo `10⁹ + 7`.

---

### 🧪 Examples

#### Example 1:
```
Input: 
n = 5, minProfit = 3, 
group = [2, 2], profit = [2, 3]

Output: 
2
```
**Explanation**:  
To make a profit of at least 3, the group could:
- Commit crimes 0 and 1, or  
- Just crime 1.

In total, there are 2 valid schemes.

---

#### Example 2:
```
Input: 
n = 10, minProfit = 5, 
group = [2, 3, 5], profit = [6, 7, 8]

Output: 
7
```
**Explanation**:  
To make a profit of at least 5, the group could commit any of the crimes individually or in combination:  
- (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2)

Total: 7 valid schemes.

---

### 🔒 Constraints

- `1 <= n <= 100`
- `0 <= minProfit <= 100`
- `1 <= group.length <= 100`
- `1 <= group[i] <= 100`
- `profit.length == group.length`
- `0 <= profit[i] <= 100`
