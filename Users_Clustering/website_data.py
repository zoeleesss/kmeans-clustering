# coding: utf-8
# 随机生成用户使用APP的数据
# 用户行为数据：用户ID 访问频率 访问时间间隔 平均停留时间 平均访问APP数
# 简化为：user_ID, used_time, app_num

import random
from random import choice

fi = open("web_data.txt", "w");

uid = []
users = 1000
for i in range(1, 1+users):
    uid.append(str(i))

fi.write('user_ID')
fi.write(', ')
fi.write('used_time')
fi.write(', ')
fi.write('app_num')
fi.write('\n')
for day in range(1, 31):
    fi.write("day")
    fi.write(str(day))
    fi.write('\n')
    for num in range(1, 1+users):
        fi.write(str(num))
        fi.write(', ')
        fi.write(str(random.randint(1, 100)))
        fi.write(', ')
        fi.write(str(random.randint(1, 50)))
        fi.write('\n')

fi.close()
