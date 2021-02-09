def timeToSec(time):
    H=int(time[0:2])
    M=int(time[3:5])
    S=int(time[6:8])
    return H*60*60+M*60+S
def secToTime(sec):
    H=sec//3600
    M=(sec%3600)//60
    S=(sec%3600)%60
    return ':'.join(map(lambda x: str(x) if len(str(x))==2 else '0'+str(x),[H,M,S]))
def solution(play_time, adv_time, logs):
    answer = ''
    start_time,end_time=[],[]
    for log in logs:
        start,end=log.split("-")
        start,end=timeToSec(start),timeToSec(end)
        start_time.append(start)
        end_time.append(end)
    #시작시간과 종료시간을 초로 변환하여 큐에 삽입
    start_time.sort()
    end_time.sort()
    end_time2=end_time[:]
    #시간순으로 정렬
    play_sec=timeToSec(play_time)
    adv_sec=timeToSec(adv_time)
    
    totalPlayingTime=0
    sCur=0
    eCur=0
    ans=(0,0)
    playingCnt=0
    for sec in range(adv_sec):
        while start_time[sCur]==sec:
            playingCnt+=1
            sCur+=1
        while end_time[eCur]==sec:
            playingCnt-=1
            eCur+=1
        totalPlayingTime+=playingCnt
    ans=(0,totalPlayingTime)
    #0초일때 삽입하면 얻는 총 재생시간 구하기
    for sec in range(1,play_sec-adv_sec):
        while sCur<len(start_time) and start_time[sCur]==sec+adv_time:
            playingCnt+=1
            sCur+=1
        while eCur<len(end_time) and end_time[eCur]==sec+adv_time:
            playingCnt-=1
            eCur+=1
        eCur2=0
        while eCur2<len(end_time2) and end_time2[eCur2]==sec:
            eCur2+=1
        totalPlayingTime+=playingCnt
        totalPlayingTime-=eCur2
        if ans[1]<totalPlayingTime:
            ans=(sec,totalPlayingTime)
    return secToTime(ans[1])

if __name__ == '__main__':
    play_time="02:03:55"
    adv_time="00:14:15"
    logs=["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    solution(play_time,adv_time,logs)
    