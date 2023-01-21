# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/


def cal_point(ops) -> int:
    ot = []
    for op in ops:
        try:
            int(op)
            ot.append(int(op))
        except ValueError as e:
            match op:
                case "+":
                    ot.append(ot[-1] + ot[-2])
                case "D":
                    ot.append(2 * ot[-1])
                case "C":
                    ot.pop()
    return sum(ot)


print(cal_point(['5', '2', 'C', 'D', '+']))
print(cal_point(["5","-2", "4", "C", "D", "9", "+", "+"]))
print(cal_point(["1"]))
