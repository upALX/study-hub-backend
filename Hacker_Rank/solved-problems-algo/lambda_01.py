def lambda_exec(x, y) -> int:
    

    value = lambda x,y:x+2*y

    return value

result = lambda_exec(x=1, y=2)

print(int(result))