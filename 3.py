def roman_to_int(a):#xi
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'d':500,'m':1000}
    int_form=0
    for i in range(len(a)):#2
        if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:#1<2 and 10<1
            int_form=roman[a[i]]
        else:
            int_form+=roman[a[i]]#0+10=10
            return int_form
        
a=input("enter a roman number ")
print("interger form of ",a,"is",roman_to_int(a))
           



















        
