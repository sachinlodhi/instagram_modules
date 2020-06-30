import csv

def pre_Process(filepath):
    u_list=[]
    with open(str(filepath),'r',encoding='utf-8-sig') as f: #data.csv contains usernames
        data = csv.reader(f)
        for row in data:
            try:
                u_list.append(row[0])
            except:
                continue
    return u_list


'''if __name__ == '__main__':
    ulist = pre_Process("/home/sachin/Desktop/instagram_modules/username.csv")
    for i in ulist:
        print(i)
        '''