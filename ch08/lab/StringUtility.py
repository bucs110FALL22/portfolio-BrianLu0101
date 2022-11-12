class StringUtility:
    def __init__(self, str):
        self.str = str

    def __str__(self):
        return self.str

    def vowels(self):
        count=0
        for i in self.str:
            if i.lower() in 'aeiou':
                count+=1
            if count>=5:
                return 'many'
            else:
                count=count
        return str(count)

    def bothEnds(self):
        if len(self.str)>2:
            return self.str[0]+self.str[1]+self.str[-2]+self.str[-1]
        else:
            return ''
    
    def fixStart(self):
        if len(self.str)>1:
            newStr=self.str[1:]
            newStr=newStr.replace(self.str[0],'*')
            return self.str[0]+newStr
        else:
            return self.str

    def asciiSum(self):
        return sum(map(ord,self.str))

    def cipher(self):
        aftShift=''
        shift=len(self.str)

        for i in range(len(self.str)):
            if self.str[i].isupper():
                aftShift+=chr((ord(self.str[i])+shift-65)%26+65)
            elif self.str[i].islower():
                aftShift+=chr((ord(self.str[i])+shift-97)%26+97)
            else:
                aftShift+=self.str[i]
        return aftShift
