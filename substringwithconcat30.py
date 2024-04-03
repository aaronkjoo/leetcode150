import collections
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # Input: s = "barfoothefoobarman", words = ["foo","bar"]
        # Output: [0, 9]
        
        word_len = len(words[0]) #length is 3
        list_len = len(words) #length is 2
        word_dict = {}
        word_count = collections.Counter(words) # word_count = Counter({'foo': 1, 'bar': 1})
        window = word_len * list_len # length is 3 * 2 = 6
        res = []
        for i in range(0,len(s)-window+1): #char by char within the window range
            temp = s[i:i+window] #Temp word that's within the window range
            #print("Temp:")
            #print(temp)
            lst = []
            while temp:
                lst.append(temp[:word_len])
                print("Temp[:word_len]")
                print(temp[:word_len])
                temp = temp[word_len:]
                print("Temp[word_len:]")
                print(temp)
            
            if collections.Counter(lst) == word_count:
                #print("List:")
                #print(lst)
                res.append(i)

        return res

str1 = "barfoothefoobarman"
arr = ["foo", "bar"]    
solution = Solution()
print(solution.findSubstring(str1, arr))


###
""" 
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        list_len = len(words)
        word_dict = {}
        word_count = Counter(words)
        window = word_len * list_len
        res = []
        for i in range(0,len(s)-window+1): #char by char within the window range
            temp = s[i:i+window]
            lst = []
            while temp:
                lst.append(temp[:word_len])
                temp = temp[word_len:]
            
            if Counter(lst) == word_count:
                res.append(i)

        return res
"""
            

