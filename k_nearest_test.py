# 自己的方法实现K最近邻分类
import numpy as np
import matplotlib.pyplot as plt

N = 50  # 数据个数
nums = np.arange(N)  # 数据集
sep = 4  # 分组个数
sep_nums = np.random.choice(N, sep, replace=False)  # 初始分组的中心
# sep_nums = np.array([3, 9, 7])
print('initial center:', sep_nums)


def classifyNum(nums, sep_nums):
    for i in nums:
        temp_sep = []  # 存放数据差
        for j in sep_nums:
            temp_sep.append(abs(i - j))

        min_temp = min(temp_sep)  # 数据差中的最小值
        idx = temp_sep.index(min_temp)  # 最小值的位置
        clusters[idx].append(i)  # 将数据i添加进分类中


if __name__ == '__main__':
    Round = 20  # 循环次数
    for r in range(Round):
        # plt.plot(sep_nums, 'ro')
        # plt.show()
        # 创建初始分组
        clusters = {}
        for i in range(sep):
            clusters[i] = []
        print('Round', r, '-' * 50)

        classifyNum(nums, sep_nums)

        for i in range(sep):
            print('cluster ', i, ':', clusters[i])

        for i in range(sep):
            sep_nums[i] = round(np.array(clusters[i]).mean())
            print('new center ', i, ': ', sep_nums[i])
