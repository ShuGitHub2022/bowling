#following cases are outside of the scope of the current exercise:
#-Provide any intermediate scores-it only has the final scores
import re
import sys

print("""
    This is a bowling exercise. Please enter scores by frame.Use comma( , )
    to separate each frame.
    Each game has no more than 21 inputs.Each input must be
    positive and no greater than 10. We will calculate
    final score at the end. Enjoy!

    Input example:'23,5/,78,0/, X, X,7/,90,88,X, XX' will return:
    [2,3,5,5,7,8,0,10,10,10,7,3,9,0,8,8,10,10,10].

    The 10th frame is a bit different:
    If you roll a strike in the first shot of the 10th frame, you get 2 more shots.
    If you roll a spare in the first two shots of the 10th frame, you get 1 more shot.
    If you leave the 10th frame open after two shots, the game is over and you do not get an additional shot.
""")

#inputs=input("Please input score(0-9) by frame one by one seperated by space(no more than 21 inputs,X means strike,/ means a spare): ")
throws=[]
#print(inputs)

def total_score(input):
    """
    Parses a user input string and calculate the total score of the submitted
    bowling game.
    @type input: str
    @param input: String representing the throws of a single bowling gae(
    split into frames). Eg. " 12, 60, 82, X, 25, 5/, 5/, 81. 33". imcompleete games are fine
    @return type: int
    @return: total calculated score.
    """
    if input==None:
        return 0
    return score(parse_score(input))

def parse_score(input):
    """
    Transforms an input string into a list of integers that
    represent each throws taken in a single game. It will filter
    out non-numeric and invaid characters( anything other then '/' or 'X').
    """
    throws_list=list(re.sub(r'[^\d/X]','',input))
    print(throws_list)
    throws=[10 - int(throws_list[idx - 1]) if val is '/' else 10 if val is 'X' else
            int(val) for idx, val in enumerate(throws_list)]
    print(throws)
    return throws

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

if __name__=="__main__":
    """
     Entry point. It accepts a list of string inputs separated by comma ,
    """
    for input in sys.argv[1:]:
        print("Input: %s Total score is: %d" % (input,total_score(input)))
