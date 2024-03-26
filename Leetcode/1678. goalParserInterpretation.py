class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        for i in range(len(command)):
            if(command[i]=='G'):
                result+=('G')
            if(command[i]=='(' and command[i+1]==')'):
                result+=('o')
            if(command[i]=='('and command[i+1]=='a' and command[i+2]=='l'and command[i+3]==')'):
                result+=('al')
        return result