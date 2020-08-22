frog = '''
       .---.`               `.---.       
    `/syhhhyso-           -osyhhhys/`    
   .syNMdhNNhss/``.---.``/sshNNhdMNys.   
   +sdMh.`+MNsssssssssssssssNM+`.hMds+   
   :syNNdhNNhssssssssssssssshNNhdNNys:   
    /ssyhhhysssssssssssssssssyhhhyss/    
    .ossssssssssssssssssssssssssssso.    
   :sssssssssssssssssssssssssssssssss:   
  /sssssssssssssssssssssssssssssssssss/  
 :sssssssssssssoosssssssoosssssssssssss: 
 osssssssssssssoosssssssoossssssssssssso 
 osssssssssssyyyyhhhhhhhyyyyssssssssssso 
 /yyyyyyhhdmmmmNNNNNNNNNNNmmmmdhhyyyyyy/ 
  smmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmms  
   /dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd/   
    `:sdNNNNNNNNNNNNNNNNNNNNNNNNNds:`    
       `-+shdNNNNNNNNNNNNNNNdhs+-`       
             `.-:///////:-.`   
'''

CEND = "\033[0m"
CRED = "\033[91m"
CBLUE = "\33[34m"
CGREEN = "\33[32m"

riesi_ = "riesi"
not_riesi_ = "not " + riesi_ + "!!"


def riesi(riesi):
    if riesi_ in riesi:
        return CBLUE + riesi_ + CEND
    else:
        return CRED + not_riesi_ + CEND

if __name__ == "__main__":
    print(CGREEN, frog, CEND)
    frog_input = input("> ").lower()
    print(riesi(frog_input))
