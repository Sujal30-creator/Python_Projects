if __name__ == '__main__':
    s = input()
    count=1
    if len(s)>0 and len(s)<100:
        print(s.isalnum())
        for x in s:
            if x.isalpha() and count<2:
                print(x.isalpha())
                count+=1
    print(count)
        
                
                    
                    