import datetime
def replace_note(note):
    note=note.replace("C#","c")
    note=note.replace("D#","d")
    note=note.replace("F#","f")
    note=note.replace("G#","g")
    note=note.replace("A#","a")
    return note
def solution(m, musicinfos):
    answer = ''
    candidate=[]
    tb=dict()
    m=replace_note(m)
    for i,music_info in enumerate(musicinfos):
        #parse time
        start,end,title,notes=music_info.split(",")
        start_time=datetime.datetime.strptime(start,"%H:%M")
        end_time=datetime.datetime.strptime(end,"%H:%M")
        play_time=((end_time-start_time).seconds)//60
        #make total play_note
        notes=replace_note(notes)
        if play_time<=len(notes):
            play_note=notes[:play_time+1]
        else:
            tmp=notes*(play_time//len(notes)+1)
            play_note=tmp[:play_time+1]
        if m in play_note:
            candidate.append(title)
            tb[title]=[play_time,i]
    if not candidate:
        return "(None)"
    else:
        candidate.sort(key=lambda x:(-tb[x][0],tb[x][1]))
        return candidate[0]

if __name__ == '__main__':
    m=	"CC#BCC#BCC#BCC#B"
    music_infos= ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    solution(m,music_infos)
    