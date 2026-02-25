#file parsinng problem :evaluated  expressionns in ip.txt file line by line and saved output in the op.txt file
import re
def evaluate_expression(expr):
 
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d|\))\s*\(', r'\1*(', expr)
    return eval(expr)

def file_parsing(ip,op):
    with open(ip , 'r') as input, open(op, 'w') as output:
        for line in input:
            if not line.strip():
                continue
            exp=line.split('=')[0].strip()
            if exp:
                result= evaluate_expression(exp)
              # for debug  print(f"{exp} = {result}")
                output.write(f"{exp} = {result}\n")
if __name__ =='__main__':

    file_parsing('ip.txt','op.txt')