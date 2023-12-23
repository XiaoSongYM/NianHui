

import random
print("NianHui v3.0 Designed By XiaoSong_YM in 2023. Type 'help'/'?' for more infomation.")


def isEmpty(cstr):
    if len(cstr)==0:
        return True
    else:
        return False

def do(opt):
    if opt=="?" or opt=="help":
        return hlp()
    elif opt=='accumulate' or opt=='ac':
        return accumulate()
    elif opt=='test' or opt=='exam':
        return test()
    elif opt=="search" or opt=='s':
        return search()
    elif opt=="read" or opt=='list':
        return read()
    elif isEmpty(opt):
        return False
    else:
        print(" 未知命令'",opt,"' 请输入'?'或'help'查看帮助界面   Unknow Command! Type 'help'/'?' for more infomation.")
        return False

def hlp():
    print("-----HELP-----")
    print(" help/?          帮助，显示此页面")
    print(" accumulate/ac   积累单词")
    print(" test/exam       检测学习成果")
    print(" search/s        查询")
    print(" read/list       查看所有单词")
    print(" exit            退出本程序")
    return True

def accumulate():
    word=''
    trans=''
    while isEmpty(word):
        word=input(" 请输入单词 Enter the word : ")
    while isEmpty(trans):
        trans=input(" 请输入释义 Enter the trans : ")
    file = open("dictionary.txt", "a", encoding="utf-8")
    file.write(word+" "+trans+"\n")
    file.close()
    return True

def test():
    filec = open("dictionary.txt", "a", encoding="utf-8")
    filec.close()
    chinese=[]
    english=[]
    cando=0
    with open('dictionary.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split()  # 根据空格拆分字符串
            english.append(parts[0])
            chinese.append(parts[1])
            cando+=1
    print(" 已根据dictionary.txt文件加载",cando,"个单词 ",cando,"words available!")
    if cando==0:
        print(" 暂无词汇 请先积累词汇或导入dictonary.txt文件!")
        return False
    num_inp=input(" 请输入测试个数 Enter the num : ")
    try:
    	num = int(num_inp)
    except ValueError:
    	return False
    t=''
    while isEmpty(t):
        t=input(" 请输入测试类型(英-中:ec/中-英ce/随机r) Enter the type(ec/ce/r) : ")
    if t=='ec':
        for i in range(1,num+1):
            rand = random.randint(0, cando-1)
            yourans=''
            while isEmpty(yourans):
                yourans=input(' ('+str(i)+'/'+str(num)+') '+english[rand]+' ')
            if yourans==chinese[rand]:
                print("  答对. True.")
            else:
                print("  答错. False. 答案ans: ",chinese[rand])
        return True
    elif t=='ce':
        for i in range(1,num+1):
            rand = random.randint(0, cando-1)
            yourans=''
            while isEmpty(yourans):
                yourans=input('('+str(i)+'/'+str(num)+') '+chinese[rand]+' ')
            if yourans==english[rand]:
                print(" 答对. True.")
            else:
                print(" 答错. False. 答案ans: ",english[rand])
        return True
    elif t=='r':
        for i in range(1,num+1):
            randWordNum = random.randint(0, cando-1)
            yourans=''
            randType = random.randint(0,1)
            
            if randType==0: #ec
                while isEmpty(yourans):
                    yourans=input('('+str(i)+'/'+str(num)+') '+english[randWordNum]+' ')
                if yourans==chinese[randWordNum]:
                    print(" 答对. True.")
                else:
                    print(" 答错. False. 答案ans: ",chinese[randWordNum])
            else: #ce
                
                while isEmpty(yourans):
                    yourans=input('('+str(i)+'/'+str(num)+') '+chinese[randWordNum]+' ')
                if yourans==english[randWordNum]:
                    print(" 答对. True.")
                else:
                    print(" 答错. False. 答案ans: ",english[randWordNum])
                
        return True
    else:
        return False

def search():
    filec = open("dictionary.txt", "a", encoding="utf-8")
    filec.close()
    chinese=[]
    english=[]
    cando=0
    with open('dictionary.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split()  # 根据空格拆分字符串
            english.append(parts[0])
            chinese.append(parts[1])
            cando+=1
    if cando==0:
        print(" 无字典")
        return False
    s=''
    while isEmpty(s):
        s=input(" 查询目标 支持双语及局部查找:")
    ansNum=0
    ans=[] 
    for i in range(0,cando):
        if s in chinese[i] or s in english[i]:
            ans.append(english[i]+' '*(15-len(english[i]))+chinese[i])
            ansNum+=1
    
    print(" 共查询到",ansNum,"个结果 :")
    for i in range(ansNum):
        print(' ('+('0'*(len(str(ansNum))-len(str(i+1)))+str(i+1)+'/'+str(ansNum)+')'),ans[i])
    return False

def read():
    filec = open("dictionary.txt", "a", encoding="utf-8")
    filec.close()
    chinese=[]
    english=[]
    cando=0
    with open('dictionary.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split()  # 根据空格拆分字符串
            english.append(parts[0])
            chinese.append(parts[1])
            cando+=1
    cdLen=len(str(cando+1))
    for i in range(cando):
        print(' ('+('0'*(len(str(cando))-len(str(i+1)))+str(i+1)+'/'+str(cando)+')'),english[i],' '*(15-len(english[i])),chinese[i])
    return True



while True:
    i = input("NianHui> ")
    while isEmpty(i):
        i=input("      ~>")
    if i=="exit":
        print("Bye~")
        break
    if do(i):
        print("操作成功 Succeeded.")
    else:
        print("操作失败 Failed")
    
