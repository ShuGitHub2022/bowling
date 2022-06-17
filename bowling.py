def score(throws, frame=1,total=0):
    """
    recursively calculate total score of the game one frame at a time
    and return total score
    """
    # exit case (frame 10 calculated or incomplete game)
    if frame > 10 or not throws:
        return total
    # strike
    elif throws[0] == 10:
        # bonus = next two throws following current frame
        bonus = 0
        # edge case logic for incomplete game
        if len(throws) >= 3:
            bonus = sum(throws[1:3])
        elif len(throws) > 1:
            bonus = throws[1]
        # pop off first index, increment frame count, update total
        return score(throws[1:], frame + 1, total + 10 + bonus)
    # spare
    elif sum(throws[0:2]) == 10:
        # bonus = next throw following current frame
        bonus = 0
        # edge case logic for incomplete game
        if len(throws) >= 3:
            bonus = throws[2]
        # pop off first two indexes, increment frame count, update total
        return score(throws[2:], frame + 1, total + 10 + bonus)
    # closed frame
    else:
        total += sum(throws[0:2])
        # pop off first two indexes, increment frame count, update total
        return score(throws[2:], frame + 1, total)

def total_score(number_list):
    return "The total score is {}".format(score(number_list))

inputs = []
while True:
    if len(inputs) != 0:
        print("Numbers so far:")
        for input_value in inputs:
            print(input_value)
    print("Enter a score here, or just hit return to calculate:")
    value=""

    if value == "":
        break
    try:
        inputs.append(int(value))
    except:
        print("{} is not a number")

print(total_score(inputs))

