import re
def p(s):
    if len(s)<2: return
    names=None
    status=None
    people=None
    
    names=re.findall(r'【.+?】',s)
    try:
        status_r=re.search(r'已..',s)
        if status_r is None:
            status_r=re.search(r'派件中',s)
        status=status_r.group()
    except Exception as e :
        print(e)
        #raise e
    people_r=re.search(r'(..人:)(\s{0,1})[\u4e00-\u9fa5]{2,4}\s',s,re.U)
    if people_r is not None:
        people=people_r.group()
    print(names,status,people)
if __name__=='__main__':
    with open('i.txt') as f:
        for l in f.readlines():
            p(l)
