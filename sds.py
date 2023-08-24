from pythonping import ping
import threading

#objects
lt = []
ltf=[]
source = './subdomains_list.txt'

#opening
def intr():
    print('\033[31m*\033[m'*100)
    print('\033[37m                                       SUBDOMAIN SEARCHER\033[m')
    print('\033[31m*\033[m'*100)


#treating the target
def targ():
    target = input("enter the website's domain and top level domain: ")
    if target[:3] == 'www':
        target = target [3:]  
    else:
        target = '.' + target

    trdt(target,lt)

#treating the data to use
def trdt(target,lt):
    tmp = []
    with open (source,'r') as slist:
        text = slist.readlines() 

    for wfl in text:
        wfl = wfl[:-1]
        lt.append(wfl)
    for subw in lt: 
        tg = subw + target
        tmp.append(tg)
    lt.clear()
    lt = tmp[:]
    multitask(lt)

#the check
def icmp(subdomain):
        try:
            print(f"Testing the {subdomain}...")
            ping(subdomain, count = 1, timeout = 3, verbose = True)
            ltf.append(subdomain)
            print(f"{subdomain}: included.")
        except:
            print(f"{subdomain}: not included.")
    

# multithread approach
def multitask(lt):
    counter = 0
    while counter <= len(lt):
        try:
            thr1 = threading.Thread(target = icmp(lt[counter]))
            thr2 = threading.Thread(target = icmp(lt[counter+1]))
            thr3 = threading.Thread(target = icmp(lt[counter+2]))

            thr1.join()
            thr2.join()
            thr3.join()   

            counter += 3
        except:
            pass
        
    final(ltf)    
            

#the final result
def final(ltf):
    print('\033[31m*\033[m'*100)
    print('the valid one(s):')
    for ad in ltf:    
        print(ad)
    print('\033[31m*\033[m'*100)



if __name__ == '__main__':
    intr()
    targ()