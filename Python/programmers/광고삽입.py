def timeToSec(time):
    H,M,S=int(time[:2]),int(time[3:5]),int(time[6:])
    return H*3600+M*60+S
def secToTime(sec):
    H=sec//3600
    sec-=H*3600
    M=sec//60
    sec-=M*60
    return ':'.join(map(lambda x: str(x) if len(str(x))==2 else '0'+str(x),[H,M,sec]))
def solution(play_time, adv_time, logs):
    play_sec = timeToSec(play_time)
    adv_sec = timeToSec(adv_time)
    startlogs=[]
    endlogs=[]
    for log in logs:
        startlogs.append(timeToSec(log[:8]))
        endlogs.append(timeToSec(log[9:]))
    total=[0]*(play_sec+1)
    for s in range(len(logs)):
        total[startlogs[s]]+=1
        total[endlogs[s]]-=1
    for s in range(1,play_sec):
        total[s]+=total[s-1]
    tmp=sum(total[:adv_sec])
    ans=[0,tmp]
    for s in range(1,play_sec-adv_sec+1):
        tmp=tmp-total[s-1]+total[s+adv_sec]
        if ans[1]<tmp:
            ans=[s,tmp]
    return secToTime(ans[0])

if __name__ == '__main__':
    play_time="02:03:55"
    adv_time="00:14:15"
    logs=["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    solution(play_time,adv_time,logs)
    