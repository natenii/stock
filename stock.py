def three_days(data):
    trade = [0]
    count_buy = 0
    count_not_buy = 0
    for number in range(0, len(data)-1):
        previous_num = data[number]
        reference = data[number+1] - previous_num
        if reference > 0:
            count_buy += 1
            if count_buy >= 3:
                trade.append(1)
            else:
                trade.append(0)
        elif reference < 0:
            count_not_buy += 1
            if count_not_buy >= 3:
                trade.append(-1)
            else:
                trade.append(0)
    return trade


data = [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368]
print(three_days(data))