
if __name__ == "__main__":
    import buscaminas
else:
    from emoji import iconos
    def bombas_vecinas (x,y,m):
        cantidad_bombas = 0 
        if x-1 >= 0 and m[y][x-1] == iconos.MINA.value :
            cantidad_bombas += 1
        if x+1 < len(m[0]) and m[y][x+1] == iconos.MINA.value :
            cantidad_bombas += 1
        if y-1 >= 0  and m[y-1][x] == iconos.MINA.value :
            cantidad_bombas += 1
        if y+1 < len(m) and  m[y+1][x] == iconos.MINA.value :
            cantidad_bombas += 1
        if y+1 < len(m) and m[y+1][x-1] == iconos.MINA.value and x-1 >= 0 :
            cantidad_bombas += 1
        if x-1 >= 0 and y-1 >= 0 and m[y-1][x-1] == iconos.MINA.value :
            cantidad_bombas += 1
        if y+1 < len(m) and x+1 < len(m[0]) and m[y+1][x+1] == iconos.MINA.value :
            cantidad_bombas += 1
        if y-1 >= 0 and x+1 < len(m[0]) and m[y-1][x+1] == iconos.MINA.value :
            cantidad_bombas += 1
        return(numero_bombas(cantidad_bombas))
        

    def numero_bombas(cantidad_bombas):

        if cantidad_bombas == 0 :
            return ("\u0030\ufe0f\u20e3")
        if cantidad_bombas == 1 :
            return ("\u0031\ufe0f\u20e3")
        if cantidad_bombas == 2 :
            return ("\u0032\ufe0f\u20e3")
        if cantidad_bombas == 3 :
            return ("\u0033\ufe0f\u20e3")
        if cantidad_bombas == 4 :
            return ("\u0034\ufe0f\u20e3")
        if cantidad_bombas == 5 :
            return ("\u0035\ufe0f\u20e3")
        if cantidad_bombas == 6 :
            return ("\u0036\ufe0f\u20e3")
        if cantidad_bombas == 7 :
            return ("\u0037\ufe0f\u20e3")
        if cantidad_bombas == 8 :
            return ("\u0038\ufe0f\u20e3")
        
    def jugar (m:list):
        pass