学号：202410111420
#登陆邮箱：15181957072@163.com
#姓名：王庭宝
class Solution_line:
    def Return_num_solution(self,line_system):
        def Check_one(row: str):#检查每一行中有没有“1”
            if row.find('1') != -1:
                return True
            else:return False
        num_solution = 0
        perouves = 0
        for i, line in enumerate(line_system):
            if Check_one(line):
                new_num_one = line_system[i].count('1')#检查有“1”的行中1的数量
                num_solution += (perouves * new_num_one)#与上一行的1的数量相乘，乘积到num_solution里
                perouves = new_num_one
        return num_solution
a = ["000","111","000"]
h = Solution_line()
print(h.Return_num_solution(a))
