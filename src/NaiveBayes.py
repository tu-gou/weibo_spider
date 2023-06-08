import math
import numpy as np
import xlrd

data_list_list = [
    ['暴毙', '奴婢', '母狗', '卧槽', '傻逼', '煞笔'],
    ['爱国', '真诚', '人民', '服务', '奋斗', '青春', '支持'],
    ['尼玛', '绑架', '辱华', '卧槽', '我操', '奴婢'],
    ['狗屁', '去死', '贪污', '政党', '贪婪'],
    ['社会', '信仰', '红色', '传承', '为人', '幸福', '安居乐业', '征程', '初心'],
    ['生活', '提高', '安康', '安全', '国际', '舞台'],
    ['朋友', '家人', '友爱', '团结', '互助', '拥抱'],
    ['性交', '性爱', '双修', '做爱', '卖淫', '色情', '发骚'],
    ['黄色', '援交', '慰安', '性感', '床', '酒'],
    ['健康', '美丽', '爱', '幸福', '勇敢', '大方'],
    ['可爱', '迷人', '善良', '正直', '健身', '身材', '性感', '才华', '健康'],
    ['身材', '避孕套', '玩具', '美女', '卖吡', '多人'],
    ['朋友', '家人', '友爱', '团结', '互助', '拥抱'],
    ['殴打', '鞭尸', '分尸', '哭', '骂', '砍刀', '烧死'],
    ['血腥', '尸体', '暴毙', '辣椒', '斧头', '酒'],
    ['辣椒', '烤肉', '美食', '饱', '幸福', '大蒜'],
    ['可爱', '迷人', '善良', '哭', '健身', '身材', '性感', '才华', '健康'],
    ['仇', '魔鬼', '锤子', '滚', '群殴', '自残', '绑架'],
    ['朋友', '家人', '友爱', '团结', '互助', '拥抱'],
    ['自杀', '农药', '遗书', '收尸', '绝望', '自死', '朋友'],
    ['跳海', '跳楼', '安眠药', '再见', '世界', '煤气'],
    ['健康', '美丽', '爱', '朋友', '美丽', '告别'],
    ['焦虑', '迷人', '大海', '正直', '健身', '身材', '性感', '才华', '健康'],
    ['焦虑', '疾病', '自残', '自杀', '煤气', '毒药']
]

# 对应上述数据集，其中0代表无负面词汇，1代表辱骂，2代表色情，3代表暴力，4代表自杀
data_class = [1, 0, 1, 1, 0, 0, 0, 2, 2, 0, 0, 2, 0, 3, 3, 0, 0, 3, 0, 4, 4, 0, 0, 4]

# 获取上述数据集以及标记等价的一维列表，二者一一对应
workbook = xlrd.open_workbook('output.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
col = worksheet.ncols
row = worksheet.nrows
data_list = []
mark = []
for j in range(1, row):
    data_list.append(worksheet.cell_value(j, 0))
    mark.append(int(worksheet.cell_value(j, 1)))


# 将数据集转为词袋模型
def bag_of_words(data_list, sublist):
    vec = [0] * len(data_list)  # 特征向量长度等于词汇量长度
    for word in sublist:
        if word in data_list:
            vec[data_list.index(word)] += 1  # 出现即加1
        return vec


# 将数据集转为特征向量
def get_train_vec():
    train_vec = []
    for data in data_list_list:
        res = bag_of_words(data_list, data)
        train_vec.append(res)
    return train_vec


def train(train_vec):
    train_array = np.array(train_vec)  # 将列表转为数组，便于训练
    train_mark = np.array(data_class)
    array_num = len(train_array)  # 样本数量
    word_num = len(train_array[0])  # 样本特征数量

    # 在标记集中找到各个特征的概率，即求出五个类别的先验概率p0 p1 p2 p3 p4
    num0 = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0

    for i in train_mark:
        if i == 0:
            num0 += 1
        elif i == 1:
            num1 += 1
        elif i == 2:
            num2 += 1
        elif i == 3:
            num3 += 1
        else:
            num4 += 1

    p0 = num0 / float(array_num)
    p1 = num1 / float(array_num)
    p2 = num2 / float(array_num)
    p3 = num3 / float(array_num)
    p4 = num4 / float(array_num)

    # 对于word0_num 和 word0 的一系列初始化，采用拉普拉斯修正，防止分子分母出现0的情况
    word0_num = 2
    word1_num = 2
    word2_num = 2
    word3_num = 2
    word4_num = 2

    word0 = np.ones(word_num)
    word1 = np.ones(word_num)
    word2 = np.ones(word_num)
    word3 = np.ones(word_num)
    word4 = np.ones(word_num)

    # 获取不同类别的单词总数
    for i in range(array_num):
        if train_mark[i] == 0:
            for num in train_array[i]:
                word0_num += num
        elif train_mark[i] == 1:
            for num in train_array[i]:
                word1_num += num
        elif train_mark[i] == 2:
            for num in train_array[i]:
                word2_num += num
        elif train_mark[i] == 3:
            for num in train_array[i]:
                word3_num += num
        else:
            for num in train_array[i]:
                word4_num += num

    # 获取不同类别下，每个单词出现的次数
    for i in range(array_num):
        for k in range(word_num):
            if train_mark[i] == 0:
                word0[k] += train_vec[i][k]
            elif train_mark[i] == 1:
                word1[k] += train_vec[i][k]
            elif train_mark[i] == 2:
                word2[k] += train_vec[i][k]
            elif train_mark[i] == 3:
                word3[k] += train_vec[i][k]
            else:
                word4[k] += train_vec[i][k]

    # 计算条件概率
    p0_word = word0 / word0_num
    p1_word = word1 / word1_num
    p2_word = word2 / word2_num
    p3_word = word3 / word3_num
    p4_word = word4 / word4_num

    return p0, p1, p2, p3, p4, p0_word, p1_word, p2_word, p3_word, p4_word


def result(test_words, p0, p1, p2, p3, p4, p0_word, p1_word, p2_word, p3_word, p4_word):
    test0 = 0
    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    # 防止概率过小相乘造成下溢，在每个概率上先取对数再相加，可以有效避免上述问题
    # 寻找测试目标中每个单词的条件概率
    for word in test_words:
        test0 += math.log(p0_word[data_list.index(word)])
        test1 += math.log(p1_word[data_list.index(word)])
        test2 += math.log(p2_word[data_list.index(word)])
        test3 += math.log(p3_word[data_list.index(word)])
        test4 += math.log(p4_word[data_list.index(word)])
    # 与类别对应的先验概率对数相加，即概率相乘
    test0 += math.log(p0)
    test1 += math.log(p1)
    test2 += math.log(p2)
    test3 += math.log(p3)
    test4 += math.log(p4)
    with open('classify.txt', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write('无负面情绪的概率：' + str(test0) + '\n')
        f.write('有辱骂色彩的概率：' + str(test1) + '\n')
        f.write('有色情内容的概率：' + str(test2) + '\n')
        f.write('有危险活动的概率：' + str(test3) + '\n')
        f.write('有自杀倾向的概率：' + str(test4) + '\n')


def naive_bayes(test_words):
    train_vec = get_train_vec()
    p0, p1, p2, p3, p4, p0_word, p1_word, p2_word, p3_word, p4_word = train(train_vec)
    result(test_words, p0, p1, p2, p3, p4, p0_word, p1_word, p2_word, p3_word, p4_word)
