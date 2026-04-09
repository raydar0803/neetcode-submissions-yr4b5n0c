class Solution:
    def isValid(self, s: str) -> bool:
        #stack o(n) time, o(n) space 
        stack = []
        parantheses = {}
        parantheses[')'] = '('
        parantheses['}'] = '{'
        parantheses[']'] = '['
        print(parantheses)

        for character in s: 
            if(character == '(' or character == '{' or character == '['):
                stack.append(character)
            else:
                if character in parantheses:
                    if stack and stack[-1] == parantheses[character]:
                        stack.pop()
                    else:
                        return False
        return True if not stack else False


        