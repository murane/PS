
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
    
    startlogs.sort()
    endlogs.sort()

    lsc=0
    lec=0
    rsc=0
    rec=0
    inc,dec=0,0
    L=len(logs)
    inc_cnt,dec_cnt=0,0
    viewer_playing_time_tot=0
    
    while startlogs[lsc]==0:
        lsc+=1
    
    for sec in range(0,adv_sec):
        #지금까지의 시청자가 본 재생시간
        viewer_playing_time_tot+=inc_cnt
        #로그로 시청자수 조절
        while rsc<L and startlogs[rsc]<=sec:
            rsc+=1
        while rec<L and endlogs[rec]<=sec:
            rec+=1
        inc_cnt=rsc-rec
    
    ans=(0,viewer_playing_time_tot)
    view_cnt=0
    for sec in range(1,play_sec-adv_sec):
        l_sec=sec
        r_sec=sec+adv_sec
        
        viewer_playing_time_tot+=view_cnt
        
        if ans[1]<viewer_playing_time_tot:
            ans=(sec,viewer_playing_time_tot)
            # print(f'{secToTime(sec)} : {viewer_playing_time_tot}')
            # print(view_cnt)
        while lsc<L and startlogs[lsc]<=l_sec:
            lsc+=1
        while lec<L and endlogs[lec]<=l_sec:
            lec+=1
        while rsc<L and startlogs[rsc]<=r_sec:
            rsc+=1
        while rec<L and endlogs[rec]<=r_sec:
            rec+=1
        inc_cnt=rsc-rec
        dec_cnt=lsc-lec
        view_cnt=inc_cnt-dec_cnt
    
    return secToTime(ans[0])

if __name__ == '__main__':
    play_time="02:03:55"
    adv_time="00:14:15"
    logs=["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    solution(play_time,adv_time,logs)
    