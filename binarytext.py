import string


# very primitive binary to text converter (literally only words)
def bintext(binary):
    b = binary.replace(' ', '') # removes whitespace
    count = 0
    byte = ''
    binaryList = []
    for num in b: # makes a list with bytes
        byte = byte + num
        count += 1
        if count == 8:
            count=0
            binaryList.append(byte)
            byte = ''
    characters = []
    for bit in binaryList:
        caps = bit[:3][1:]
 
        if caps == '10': # figures out if it is cap, lower
            caps = True
        elif caps == '11':
            caps = False
##        else:
##            caps = 'punctuation'
        # gets the number and corresponding character
        
        chars = bit[3:]
        power = 4
        numberver = []
        
        
        for number in chars: # gets the numbers from the 5 possible
            if number == '1':
                numberver.append(pow(2,power))
            power -= 1
        index = sum(numberver) -1 # adds up the numbers and subtracts 1 because of the 0 index
        
            
        if caps == True:
            characters.append(string.ascii_uppercase[index])
        elif caps == False:
            characters.append(string.ascii_lowercase[index])
        elif bit == '00100000': # hard coded, ran out of time
            characters.append(' ')

        
        
        
                
        
                
            
            
            

        
        

    return ''.join(characters)



userInput = input('Enter binary to be converted to text (no punctuation)\n')
print(bintext(userInput))
        
