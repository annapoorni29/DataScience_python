import os
#Creating basedir
basedir= "Shrimad_Valmiki_Ramayan/"
section="_Kandam"
secnames = [
    "1_Bala",
    "2_Ayodhya",
    "3_Aranya",
    "4_Kishkindha",
    "5_Sundara",
    "6_Yuddha"
]
os.mkdir(basedir)

for name in secnames:
    os.mkdir(basedir+name+section)

#Bala_Kandam
bkdir= basedir+"/1_Bala_Kandam"
for x in range(1,78):
    #print(basedir + os.path.sep + "Sarga"+ str(x))
    os.mkdir(bkdir + os.path.sep + "Sarga"+ str(x))

#Ayodhya_Kandam
akdir= basedir+"/2_Ayodhya_Kandam"
for x in range(1,120):
    #print(basedir + os.path.sep + "Sarga"+ str(x))
    os.mkdir(akdir + os.path.sep + "Sarga"+ str(x))

#Aranya_Kandam
arkdir= basedir+"/3_Aranya_Kandam"
for x in range(1,76):
    #print(basedir + os.path.sep + "Sarga"+ str(x))
    os.mkdir(arkdir + os.path.sep + "Sarga"+ str(x))

#Kishkindha_Kandam
kkdir= basedir+"/4_Kishkindha_Kandam"
for x in range(1,68):
    #print(basedir + os.path.sep + "Sarga"+ str(x))
    os.mkdir(kkdir + os.path.sep + "Sarga"+ str(x))

#Sundara_Kandam
skdir= basedir+"/5_Sundara_Kandam"
for x in range(1,69):
    #print(basedir + os.path.sep + "Sarga"+ str(x))
    os.mkdir(skdir + os.path.sep + "Sarga"+ str(x))

#Yuddha_Kandam
ykdir= basedir+"/6_Yuddha_Kandam"
for x in range(1,129):
    #print(basedir + os.path.sep + "Sarga"+ str(x))
    os.mkdir(ykdir + os.path.sep + "Sarga"+ str(x))