class Respostas:
    def pergunta1():
        pergunta = int(input('''
            1.O que você fazia em São Paulo?
            2.A quanto tempo você estava em São Paulo?
            3.Onde você está hospedado?  
            R:'''))
        if pergunta == 1:
            return (True, pergunta) 
        else:
            return (False, pergunta)
       
    def pergunta2():
        pergunta = int(input('''
            1.Você está sendo acusado de terrorismo. Sabia disso?
            2.Sua esposa estava na cidade?
            3.Quais os nomes dos seus amigos?  
            R:'''))
        if pergunta == 3:
            return (True, pergunta) 
        else:
            return (False, pergunta)
        
    def pergunta3():
        pergunta = int(input('''
            1.Vi seu amigo Thiago acompanhado desta mulher, reconhece? \U0001F48F("Mostra uma foto.")
            2.Sabe onde seus amigos estão?
            3.Como conheceu seus amigos?  
            R:'''))
        if pergunta == 1:
            return (True, pergunta) 
        else:
            return (False, pergunta)
    def pergunta4():
        pergunta = int(input('''
            1.Você sabia que o Thiago está tendo um caso com a Carla já tem 1 ano?
            2.Você está sendo acusado de terrorismo, qualquer informação extra reduzirá sua pena!
            3.Onde você pois a bomba?
            R:'''))
        if pergunta == 2:
            return (True, pergunta) 
        else:
            return (False, pergunta)
        