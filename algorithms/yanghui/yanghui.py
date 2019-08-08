# astr = """
# Select count(Ssex) as 男生人数 from Student group by Ssex having Ssex='男';
#     Select count(Ssex) as 女生人数 from Student group by Ssex having Ssex='女';
#
# """
#
#
#
# print(astr.lower().replace('#', 'id'))


def yanghui_issue(level=1):

    def get_value(x, y):

        assert  x<=y

        if x==1:
            # left border
            return 1
        elif x==y:
            # right border
            return 1
        else:
            return get_value(x-1, y-1) + get_value(x, y-1)


    for row in range(1, level+1):
        line_result = ''
        for col in range(1, row+1):
            line_result += str(get_value(col, row)) + ' '
        print(line_result)



yanghui_issue(5)


def yanghui_list(level):

    yanghui_list = []

    for row in range(0, level):
        yanghui_list.append([])
        for col in range(0, row+1):
            if col == 0:
                yanghui_list[row].append(1)
            elif col == row:
                yanghui_list[row].append(1)
            else:
                left_child = yanghui_list[row - 1][col -1]
                mid_child = yanghui_list[row - 1 ][col]
                yanghui_list[row].append(   left_child+mid_child )
    return yanghui_list
print (yanghui_list(8))


