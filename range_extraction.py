
def solution(args):
    rango = sorted(args)
    primero_en_rango = ultimo = None
    result = ""
    for i, r in enumerate(rango):
        if not result: 
            result = str(r)
            primero_en_rango = r
        else:
            if r == ultimo + 1:
                if primero_en_rango != ultimo:
                    result.replace(f"-{ultimo}", f"-{r}")
                else:
                    result += f"-{r}"
            else:
                result += f",{r}"
                primero_en_rango = r
                
                
        
        ultimo = r        
    print(result)
    
if __name__ == '__main__':
    solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
    solution([-3,-2,-1,2,10,15,16,18,19,20])
