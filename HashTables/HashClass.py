
class hashTable():
    
    def __init__(self):
        self.arrayLengthPrime = 7
        self.array = [[None] for i in range(self.arrayLengthPrime)]
        self.maxKeyLength = 100
        
    def __isString(self, userInput: str) -> bool:
        ''' private helper method to determine if input is a string
            In: any input in question
            Out: bool True if input is string
        '''
        if(type(userInput) == str): return True
        else: return False
        
    def hashingFunction(self, key: str) -> int:
        ''' method to store an algorythm for hashing a key into a value within
            a given array length
            In: str key to convert
                int prime user defined maximum length of array
            Out: int mapped index from key            
        '''
        index = 0
        primeNumber = 31
        
        for char in key:
            order = ord(char)-96        #-96 to get the alphabetical order 'a'=1
            index = (index * primeNumber + order)
            index = index % self.arrayLengthPrime # modulus to make sure within length
            
        return index
    
    def insert(self, key: str, value: any) -> None:
        ''' method to position a key/value pair in the array and handle collisions
            In: str key to store less than maxKeyLength
                any value of the key
            Out: None||array  
        '''
        # validate string input and limit length of string to hash
        if(self.__isString(key) == False): return None
        if(len(key) > self.maxKeyLength): return None
        
        # hash the given key
        index = self.hashingFunction(key)
        
        # check that position is empty
        if(self.array[index][0]==None):
            self.array[index] = [[key,value]]
            return self.array
        
        # collision handling via chaining
        else:
            self.array[index].append([key,value])
            return self.array
        
    def get(self, keyToRetrieve: str) -> any:
        ''' method to obtain value from a key
            In: str key in question
            Out: None||value if key does not exists return None
        '''
        # validate string input and limit length of string to hash
        if(self.__isString(keyToRetrieve) == False): return None
        if(len(keyToRetrieve) > self.maxKeyLength): return None
        
        # hash the key
        index = self.hashingFunction(keyToRetrieve)
        keyValueList = self.array[index]
        
        # search for the key if there was collision
        for i in range(len(keyValueList)):
            currentKey = keyValueList[i][0]
            currentValue = keyValueList[i][1]
            
            if(currentKey == keyToRetrieve): return currentValue
        
        return None
    
#%% Testing insert()
print('Testing insert()----------------------------')

# testing chaining
# for this test to work primeNumber=31 and arrayLengthPrime=7
dictionary = hashTable()
dictionary.insert('bar',-100)
dictionary.insert('3',1)
if(dictionary.array[4] == [['bar', -100], ['3', 1]]): print('Test 1: passed')
else: print('Test 1: failed')

#%% Testing get()
print('Testing get()-------------------------------')

# testing getting value when there was a collision
# requires last test to run to fill the array with collisions
value = dictionary.get('bar')
if(value == -100): print('Test 1: passed')
else: print('Test 2: failed')
