import jieba
import jieba.posseg as pseg
 
import jieba.analyse
import xlwt 

def write(path,Mylist):
    word_dict= {}
    with open("./output/deal/"+path,'w',encoding = 'utf-8') as wf2: 
 
        for item in Mylist:
            if item not in word_dict: 
                word_dict[item] = 1
            else:
                word_dict[item] += 1
 
        orderList=list(word_dict.values())
        orderList.sort(reverse=True)
        for i in range(len(orderList)):
            for key in word_dict:
                if word_dict[key]==orderList[i]:
                    wf2.write(key+' '+str(word_dict[key])+'\n') 
                    key_list.append(key)
                    word_dict[key]=0 

if __name__=="__main__":
 
    wbk = xlwt.Workbook(encoding = 'ascii')
    sheet = wbk.add_sheet("wordCount")
    word_lst_v = []
    word_lst_a=[]
    word_lst_n=[]
    word_lst_other=[]
    key_list=[]
    for line in open("./output/rawfile/ribao_result.txt", 'r', encoding = 'utf-8'):#1.txt是需要分词统计的文档
        item = line.strip('\n\r').split('\t') #制表格切分
        tags = pseg.cut(item[0]) #jieba分词
        for t in tags:
            if t.flag=="a":
                word_lst_a.append(t.word)
            elif t.flag=='v':
                word_lst_v.append(t.word)
            elif t.flag=="n":
                word_lst_n.append(t.word)
            else:
                if(t.word=="gay"):
                    word_lst_other.append(t.word)
                '''
                for s in t.word:
                    if (s >= u'\u0041' and s<=u'\u005a') or (s >= u'\u0061' and s<=u'\u007a'):
                        word_lst_other.append(t.word)
                 '''
    
    jieba.add_word("gay")
    write("wordCount_a.txt",word_lst_a)
    write("wordCount_n.txt",word_lst_n)
    write("wordCount_v.txt",word_lst_v)
    write("wordCount_other.txt",word_lst_other)