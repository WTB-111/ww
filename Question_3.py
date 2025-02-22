#学号：202410111420
#登陆邮箱：15181957072@163.com
#姓名：王庭宝
class Solution:
    def __init__(self):
        self.Plans = 0
        self.solutions = []

    def return_solution(self, n):
        Col = [i for i in range(n)]
        Exaple = [['.' for _ in range(n)] for _ in range(n)]#生成二维列表，用于下棋

        def Check(row, col):#检查斜线方向有没有“q”
            i = row - 1; j = col + 1

            while i >= 0 and j <= n - 1:
                if Exaple[i][j] == 'q':
                    return False
                i -= 1;j += 1
            i = row - 1;j = col - 1
            while i >= 0 and j >= 0:
                if Exaple[i][j] == 'q':
                    return False
                i -= 1;j -= 1
            return True
        def Main_Judge(Col, i):#主程序
            if i == n:#如果循环到最后，则添加案例到self.solutions
                solution=copy.deepcopy(Exaple)#深复制
                self.solutions.append(solution)
                self.Plans += 1
            else:
                for j in Col:#剩余的列，行中查看可不可以安放“q”，若可以，则将所占的列从列表中去掉，剩下的列下一行循环
                    New_Col = Col.copy()
                    if Check(i, j):
                        Exaple[i][j] = 'q'
                        New_Col.remove(j)
                        Main_Judge(New_Col, i + 1)
                    else:
                        continue
                    Exaple[i][j] = '.'

        Main_Judge(Col, 0)
        return self.Plans,self.solutions
a = Solution()
s,f=a.return_solution(5)
print(s,f)
