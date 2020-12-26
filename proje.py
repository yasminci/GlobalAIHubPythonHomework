#project
    
def dersal():
    dersler=[]
    i=0
    for i in range(1,7):
        i+=1
        if(i==7):
            print("5 dersten fazla ders aldığınız için sınıfta kaldınız.")
        else:
            ders=input("Seçmek istediğiniz dersi giriniz: ")
            dersler.append(ders)
            print(f"Aldığınız dersler: {dersler}")
            a=len(dersler)
            b=int(input("Ders seçimi yapmaya devam etmek için 1'e ders kaydını tamamlamak için 2'ye basın: "))
            if b==1:
                continue
            elif b==2:
                if(a<3):
                    raise ValueError("3 dersten daha az ders aldığınız için sınıfta kaldınız.")
                    break
                else:
                            ex=input("Sınava girmek için bir ders seçiniz: ")
                            
                            if (ex in dersler):
                                print(f"Sınava girmek için {ex} dersini seçtiniz.")
                                midterm=float(input("Arasınav notunu giriniz: "))
                                final=float(input("Final notunu giriniz: "))
                                project=float(input("Proje notunu giriniz: "))
                                bilgi={}
                                bilgi["midterm"]=midterm
                                bilgi["final"]=final
                                bilgi["project"]=project
                                print(f"{ex}= {bilgi}")
                                midterm=(midterm*30)/100
                                final=(final*50)/100
                                project=(final*20)/100
                                result=midterm+final+project
                                if (result>=90):
                                    print("Notunuz AA ")
                                    break
                                                        
                                elif (result>=70 and result<90):
                                    print("Notunuz BB")
                                    break
                                                        
                                elif (result>=50 and result<70):
                                    print("Notunuz CC")
                                    break
                                                        
                                elif (result>=30 and result<50):
                                    print("Notunuz DD")
                                    break
                                                        
                                                    
                                elif (result<30):
                                    print(" Notunuz FF ve sınıfta kaldınız.")
                                    break
                                    
                                 
                            else:
                                print("Böyle bir ders seçimi yapmadınız")
                                break

for x in range(1,4):
            x +=1
            name=input("Lütfen adınızı giriniz: ")
            surname=input("Lütfen soyadınızı giriniz: ")
            if (name.isalpha())and (surname.isalpha())==True:
                print(f"Hoşgeldiniz {name} {surname}")
                s=int(input("Ders seçimi yapmak için 1 i programdan çıkmak için 2 yi tıklayın:"))
                if (s==1):
                    dersal()
                    break
                else:
                     print("Programdan çıktınız.")
                     break
                
                   
            else:
                print("Lütfen doğru bir değer giriniz!!")
                if (x==4):
                    print("3'den fazla yanlış giriş yaptınız hesabınız bloke olmuştur.")



                     
    







