#                importando bibliotecas
import time

#                 Variáveis

riscovalue = ""
testesselect = ""
testesselecterror = 1
checklist = ""
testes= "cliente ciente que a empresa não se responsabiliza por testes não feitos."
selectfrontal = ""
incellselect = "n"
primlinhselect = "n"
problemainformadoassistencia = 1
assistenciaerror = 1
riscoerror = 1
liquidoerror = 1
riscoif = 0
riscoiferror = 1
initerror = 1
problemainformadoerror = 1
selectorerror = 1
pecaselector = 0
pecagarantia = "1 Mês de garantia"
qualidadepeca = "original chinesa"
qualidadefrontalerror = 0
frontalservice = 0
initvalue = 1
liquidovalue = ""
liquidovalueerror= 1
liquidoexit = 1
aro = ""
arovalue = ""
arovalueerror = 0
looparo = 0
qualidadeconectorerror = 0
pecaconectorerror = 0
servicoexecutado = ""
option1 = 0
option2 = 0
formatopadraofrontal = 1
pelicula = ""
peliculaerror = ""
formatopadraoconector = 1
formatopadrao = 1
garantiaerror = 1
pecaerror = 1
option3 = 0

#                        licença do sistema
print("Sistema Desenvolvido por Vithor Hernandez para a empresa Mega Sampa Cell")
print("Todos os créditos reservados")
print("@vtzin_sk8")
print("Copyright 2023©️")
print("--------------------------------------------------------------------------------")
#                        iniciar programa
print("deseja usar o programa? (s/n)")
value = input("Escolha: ")
while initvalue != 0:
    if value == "s":
        break
    elif value == "n":
        testesselecterror = 0
        liquidoexit = 0
        initerror = 0
        break
    else:
        print("você digitou uma opção incorreta, por favor, digite novamente")
        print("deseja usar o programa? (s/n)")
        value = input("Escolha: ")
        print("--------------------------------------------------------------------------------")
#                     escolha de serviço executado
while initerror != 0:
    print("--------------------------------------------------------------------------------")
    while selectorerror != 0:
        try:
            print("escolha qual serviço será feito:")
            print("1 - troca de frontal")
            print("2 - troca de conector")
            print("3 - outros tipos de troca")
            print("4 - sair do programa")

            selector = int(input("Escolha: "))
            if selector == 1:
                initerror = 0
                selectorerror = 0
                option1 = 1
                servicoexecutado = "troca da frontal"
                pecagarantia = "3 Mêses de garantia."
                qualidadefrontalerror = 1
                pecaselector = 1
                break
            elif selector == 2:
                initerror = 0
                selectorerror = 0
                option2 = 1
                servicoexecutado = "troca do conector"
                qualidadeconectorerror = 1
                pecaconectorerror = 1
                pecaselector = 2
                pecainfo = "troca do conector"
                break
            elif selector == 3:
                initerror = 0
                selectorerror = 0
                option3 = 1
                pecaselector = 3
                break
            elif selector == 4:
                testesselecterror = 0
                initerror = 0
                selectorerror = 0
                liquidoexit = 0
                problemainformadoerror = 0
                break
            else:
                print("você digitou uma opção invalida, por favor, tente novamente")
        except ValueError:
            print("por favor, responda utilizando apenas numeros nesse campo")
#                      escolha de tipo de frontal usada
    while qualidadefrontalerror != 0:
        try:
            print("por favor, digite a qualidade da sua frontal:")
            print("1 - original nacional")
            print ("2 - original chinesa")
            print ("3- incell")
            print ("4- primeira linha")
            selectfrontal = int(input("Escolha: "))
            if selectfrontal == 1:
                arovalueerror = 1
                qualidadepeca = "original nacional"
                print ("voce selecionou:", qualidadepeca)
                break
            elif selectfrontal == 2:
                arovalueerror = 1
                print ("voce selecionou:", qualidadepeca)
                break
            elif selectfrontal == 3:
                print("--------------------------------------------------------------------------------")
                print("esse tipo de tela (incell) foi aconcelhada pelo lucas a não ser usada.")
                print("tem certeza que deseja continuar? (s/n)")
                incellselect = input("Escolha: ")
                if incellselect == "s":
                    arovalueerror = 1
                    print("--------------------------------------------------------------------------------")
                    qualidadepeca = "incell"
                    print ("voce selecionou:", qualidadepeca)
                    break
                elif incellselect == "n":
                    print("--------------------------------------------------------------------------------")
                else:
                    print("--------------------------------------------------------------------------------")
                    print("você digitou uma opção incorreta, por favor, digite novamente")
            elif selectfrontal == 4:
                print("--------------------------------------------------------------------------------")
                print("esse tipo de tela (primeira linha) foi aconcelhada pelo lucas a não ser usada.")
                print("tem certeza que deseja continuar? (s/n)")
                primlinhselect = input("Escolha: ")
                if primlinhselect == "s":
                    arovalueerror = 1
                    print("--------------------------------------------------------------------------------")
                    qualidadepeca = "primeira linha"
                    print ("voce selecionou:", qualidadepeca)
                    break
                elif primlinhselect == "n":
                    print("--------------------------------------------------------------------------------")
                else:
                    print("--------------------------------------------------------------------------------")
                    print("você digitou uma opção errada, por favor, digite novamente")
        except ValueError:
            print("por favor, responda utilizando apenas numeros nesse campo")

        
    while arovalueerror != 0:
        print("a frontal é com aro? (s/n)")
        arovalue = input("Responda: ")
        if arovalue == "s":
            aro = "com aro"
            qualidadepeca = qualidadepeca + " (" + aro + ")"
            print("você selecionou a opçâo", "(", "frontal", qualidadepeca, ")")
            qualidadepeca = ", " + qualidadepeca + ", "
            break
        elif arovalue == "n":
            aro = "sem aro"
            qualidadepeca = qualidadepeca + " (" + aro + ")"
            print("você selecionou a opçâo", "(", "frontal", qualidadepeca, ")")
            break
        else:
            print("você digitou uma opção incorreta, por favor, digite novamente")
#          escolha o tipo de conector usado
    while qualidadeconectorerror != 0:
        while pecaconectorerror != 0:
            pecagarantia += ". "
            print("qual a qualidade da peça que vai ser usada no celular do cliente?")
            print('obs: caso a peça não tenha uma "qualidade" especificada, apenas deixe esse campo em branco ')
            qualidadepeca = input("Digite:")
            if qualidadepeca == "":
                qualidadepeca += ""
                servicoexecutado += ", "
                qualidadeconectorerror = 0
                break
            elif qualidadepeca == " ":
                qualidadepeca = ""
                servicoexecutado += ", "
                qualidadeconectorerror = 0
                break
            elif qualidadepeca == "  ":
                qualidadepeca = ""
                servicoexecutado += ", "
                qualidadeconectorerror = 0
                break
            elif qualidadepeca == "   ":
                qualidadepeca = ""
                servicoexecutado += ", "
                qualidadeconectorerror = 0
                break
            else:
                qualidadepeca = ", " + "qualidade da peça " + qualidadepeca + ", "
                qualidadeconectorerror = 0
                break
    #       começo do problema informado

    while problemainformadoerror != 0:
        print ("qual é o problema do celular do cliente?")
        print ("obs: por favor, escreva esse campo de forma resumida para no final não passar do maximo de linhas do programa de O.S")
        problema = input("Problema: ")
        while assistenciaerror != 0:
            print("já passou por assistencia tecnica? (s/n)")
            assistencia = input("responda: ")
            if assistencia == "s":
                assistencia = "já passou por assistencia tecnica"
                assistenciaerror = 0
                print("por qual peça ele passou a assitencia?")
                assistenciavalue = input("digite aqui: ")
                assistencia = assistencia + " (" + assistenciavalue + ")"
            elif assistencia == "n":
                assistenciavalue = ""
                assistencia = "nunca passou por assistencia tecnica"
                break
            else:
                print ("você digitou uma opção incorreta, por favor, digite novamente")
#                          contato com liquido
        while liquidoerror != 0:
            print("já teve contato com algum tipo de liquido? (s/n)")
            liquido = input("responda: ")
            if liquido == "s":
                print("Atenção: em casos como esse que o aparelho tem contato com liquido, o serviço é sem garantia e a empresa não se responsabiliza por danos causados pelo mesmo")
                while liquidovalueerror != 0:
                    print("tem certeza que deseja continuar? (s/n)")
                    liquidovalue = input("Responda: ")
                    if liquidovalue == "s":
                        print("alertar ao cliente que a empresa não se responsabiliza por danos de liquido")
                        pecagarantia = "serviço sem garantia. "
                        liquido = "já teve contato com agua (serviço sem garantia)"
                        break
                    elif liquidovalue == "n":
                        testesselecterror = 0
                        option1 = 0
                        option2 = 0
                        option3 = 0
                        liquidoerror = 0
                        riscoerror = 0
                        riscoiferror = 0
                        liquidoexit = 0
                        break
                    else:
                        print("você digitou uma opção incorreta, por favor, tente novamente")
            elif liquido =="n":
                liquido = "nunca teve contato com nenhum tipo de liquido"
                liquidoerror = 0
            else:
                print("você digitou uma opção invalida, por favor, digite novamente")
            if  liquidovalue == "s":
                break
        while riscoerror != 0:
            print("há algum risco ao abrir o aparelho? (s/n)")
            risco = input("responda: ")
            if risco == "s":
                riscoif = 1
                break
            elif risco == "n":
                riscoiferror = 0
                risco= "não a riscos para abrir o aparelho"
                break
            else:
                print("você digitou uma opção invalida, por favor, digite novamente")
        while riscoiferror != 0:
            if riscoif == 1:
                print("qual é o risco? (tampa/frontal)")
                riscovalue = input("responda: ")
                if riscovalue == "tampa":
                    risco = "cliente ciente do risco da tampa quebrar ou descascar"
                    riscoiferror = 0
                elif riscovalue == "frontal":
                    risco = "cliente ciente do risco da frontal quebrar ou ficar com picos de luz"
                    riscoiferror = 0
                else:
                    print("você digitou uma opção inválida, por favor, digite novamente")
        break
#------------------------------------------------
    while testesselecterror != 0:
        print("todos os testes da check list foram possiveis de serem feitos? (s/n)")
        testesselect = input("responda: ")
        if testesselect == "s":
            checklist = "ENTRADA: todos os testes foram feitos e passados para a check list."
            testes = ""
            break
        elif testesselect == "n":
            print("quais testes foram/não foram possiveis de serem feitos")
            print("exemplo: apenas vibra e botão power foram possiveis de serem testados devido ao estado do aparelho.")
            checklist = input("Digite: ")
            checklist = "ENTRADA: " + checklist + "."
            break
        else:
            print("você digitou uma opção incorreta, por favor, digite novamente")
#-----------------------------
    if selector == 1:
        while option1 != 0:
            while peliculaerror != 0:
                print("o aparelho esta com pelicula? (s/n)")
                print("OBS: caso esteja, avise o cliente que é necessario a retirada da pelicula para o aparelho entrar para concerto")
                pelicula = input("Escolha: ")
                if pelicula == "s":
                    print("não se esqueça de avisar ao cliente que é necessario a retirada da pelicula")
                    pelicula = " cliente autorizou a retirada da pelicula"
                    break
                elif pelicula == "n":
                    pelicula = " aparelho entrando sem pelicula"
                    break
                else:
                    print("você digitou uma opção invalida, por favor, tente novamente")
            while formatopadraofrontal !=0:
                print("--------------------------------------------------------------------------------")
                print("PROBLEMA INFORMADO:")
                print(problema, assistencia, liquido, risco)
                print("--------------------------------------------------------------------------------")
                print("SERVIÇO EXECUTADO:")
                print(servicoexecutado, qualidadepeca, pecagarantia, pelicula )
                print("--------------------------------------------------------------------------------")
                print("OBSERVAÇÕES:")
                print(checklist)
                print(testes)
                print("--------------------------------------------------------------------------------")
                break
            break
        break  
    elif selector == 2:
        while option2 != 0:
            while peliculaerror != 0:
                print("o aparelho esta com pelicula? (s/n)")
                print("OBS: caso esteja, avise o cliente que é necessario a retirada da pelicula para o aparelho entrar para concerto")
                pelicula = input("Escolha: ")
                if pelicula == "s":
                    print("não se esqueça de avisar ao cliente que é necessario a retirada da pelicula")
                    pelicula = "cliente autorizou a retirada da pelicula"
                    break
                elif pelicula == "n":
                    pelicula = "aparelho entrando sem pelicula"
                    break
                else:
                    print("você digitou uma opção invalida, por favor, tente novamente")
            
            
            while formatopadraoconector !=0:
                print("--------------------------------------------------------------------------------")
                print("PROBLEMA INFORMADO:")
                print(problema, assistencia, liquido, risco)
                print("--------------------------------------------------------------------------------")
                print("SERVIÇO EXECUTADO:")
                print(servicoexecutado, qualidadepeca, pecagarantia, pelicula )
                print("--------------------------------------------------------------------------------")
                print("OBSERVAÇÕES:")
                print(checklist)
                print(testes)
                print("--------------------------------------------------------------------------------")
                break
            break
        break
    elif selector == 3:
        while option3 != 0:
            print("qual serviço vai ser feito no aparelho do cliente?")
            servicoexecutado = input("Digite: ")
            while pecaerror != 0:
                print("qual a qulidade da peça que vai ser usada no celular do cliente?")
                print('obs: caso a peça não tenha uma "qualidade" especificada, apenas deixe esse campo em branco ')
                qualidadepeca = input("Digite:")
                if qualidadepeca == "":
                    qualidadepeca += ""
                    break
                elif qualidadepeca == " ":
                    qualidadepeca = ""
                    break
                elif qualidadepeca == "  ":
                    qualidadepeca = ""
                    break
                elif qualidadepeca == "   ":
                    qualidadepeca = ""
                    break
                else:
                    qualidadepeca = "," + "qualidade da peça " + qualidadepeca
                    break
            #                 garantia
            while garantiaerror != 0:
                print("quanto tempo de garantia tem esse serviço?")
                print("obs: caso não tenha garantia apenas deixe esse campo em branco")
                pecagarantia = input("Digite: ")
                if pecagarantia == "":
                    pecagarantia = ""
                    break
                elif pecagarantia == " ":
                    pecagarantia = ""
                    break
                elif pecagarantia == "  ":
                    pecagarantia = ""
                    break
                elif pecagarantia == "   ":
                    pecagarantia = ""
                    break
                else:
                    pecagarantia = ", " + pecagarantia + " de garantia"
                    break
                
            #                     pelicula
            while peliculaerror != 0:
                print("o aparelho esta com pelicula? (s/n)")
                print("OBS: caso esteja, avise o cliente que é necessario a retirada da pelicula para o aparelho entrar para concerto")
                print("OBS: caso seja um serviço que não precise retirar a pelicula, apenas deixe esse campo em branco")
                pelicula = input("Escolha: ")
                if pelicula == "s":
                    print("não se esqueça de avisar ao cliente que é necessario a retirada da pelicula")
                    pelicula = ", cliente autorizou a retirada da pelicula"
                    break
                elif pelicula == "n":
                    pelicula = ", aparelho entrando sem pelicula"
                    break
                elif pelicula == "":
                    break
                elif pelicula == " ":
                    pelicula = ""
                elif pelicula == "  ":
                    pelicula = ""
                elif pelicula == "   ":
                    pelicula = ""
                else:
                    print("você digitou uma opção invalida, por favor, tente novamente")

            #              -----------parte que mostra como ficou------------

            while formatopadrao !=0:
                print("--------------------------------------------------------------------------------")
                print("PROBLEMA INFORMADO:")
                print(problema, assistencia, liquido, risco)
                print("--------------------------------------------------------------------------------")
                print("SERVIÇO EXECUTADO:")
                print(servicoexecutado, qualidadepeca ,pecagarantia, pelicula )
                print("--------------------------------------------------------------------------------")
                print("OBSERVAÇÕES:")
                print(checklist)
                print(testes)
                print("--------------------------------------------------------------------------------")
                break
            break
while liquidoexit != 0:
    print("arquivo .txt gerado com sucesso!")
    arquivo = open('ordem de serviço.txt','w')
    arquivo.write("PROBLEMA INFORMADO:\n")
    arquivo.write(" \n")
    arquivo.write(problema +", " + assistencia + "\n")
    arquivo.write(liquido + ", " + risco + "." + "\n")
    arquivo.write(" \n")
    arquivo.write("SERVIÇO EXECUTADO:\n")
    arquivo.write(servicoexecutado + " " + qualidadepeca + " " + pecagarantia + pelicula)
    arquivo.write("  \n")
    arquivo.write("  \n")
    arquivo.write("OBSERVAÇÕES:\n")
    arquivo.write(checklist + "\n")
    arquivo.write(testes + "\n")
    arquivo.write(" \n")
    arquivo.write("AVISO: \n")
    arquivo.write("* não se esqueça de preencher as observações gerais com o estado que o aparelho está entrando \n")
    arquivo.write("* não se esqueça de puxar o imei do aparelho \n")
    arquivo.write("* quaisquer erros no sistema, comunicar a gerente para o mesmo ser corrigido \n")
    arquivo.write(" \n")
    arquivo.write("obrigado por usar o sistema <3 \n")
    arquivo.close()
    break 
                
 # "break" para não dar loop no programa

#agradecimentos
print("--------------------------------------------------------------------------------")
print("obrigado por usar o programa <3")

#setando tempo para o programa fechar

time.sleep(10)