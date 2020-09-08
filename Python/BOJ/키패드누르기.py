def dist(num,left,right):
    value=[
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']
    ]
    for row in range(len(value)):
        for col in range(len(value[0])):
            if value[row][col]==num:
                num_co = (row,col)
            if value[row][col]==left:
                left_co = (row,col)
            if value[row][col]==right:
                right_co = (row,col)
    return (abs(num_co[0]-left_co[0])+abs(num_co[1]-left_co[1]), abs(num_co[0]-right_co[0])+abs(num_co[1]-right_co[1]))
def solution(numbers, hand):
    answer = ''
    left,right='*','#'
    for num in numbers:
        if num in [1,4,7]:
            left=num
            answer+='L'
        elif num in [3,6,9]:
            right=num
            answer+='R'
        else:
            left_dist,right_dist = dist(num,left,right)
            if left_dist<right_dist or (left_dist==right_dist and hand=="left"):
                answer+='L'
                left=num
            elif left_dist>right_dist or (left_dist==right_dist and hand=="right"):
                answer+='R'
                right=num
                    
    return answer
if __name__ == "__main__":
    numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand="right"
    solution(numbers,hand)