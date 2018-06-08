from collections import deque


def search(lines, pattern, history=5):
    # 构建一个固定大小的队列。
    # 队列的大小由maxlen来控制，当队列满且有新元素加入时，最老的元素会被移除掉
    # 当未指定大小时，会得到一个无限大的队列
    # 队列的好处是，队列两端插入和删减时间复杂度时o(1),而list则是o(N)
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open(r'cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('_'*20)
