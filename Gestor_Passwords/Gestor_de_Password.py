import random
import PySimpleGUI as sg
import os
import time

theme='Reddit'
#criar as janelas e os layouts
def janela_inicial():
    sg.theme(theme)
    layout = [
        [sg.Text('        O que deseja fazer?',font='Famaly 15')],
        [sg.Button('Consultar',font='Famaly 12', button_color=('White','Blue')),sg.Button('Adicionar Password',font='Famaly 12',button_color=('White','Green')),sg.Button('Sair',font='Famaly 12',button_color=('White','Red'))]
    ]
    return sg.Window('Gestor de Passwords',layout=layout,finalize=True)

def janela_consultar():
    sg.theme(theme)
    layout= [
        [sg.Text('Site / Software:',font='Famaly 12',size=(15,1)),sg.Input(key='consulta_site',size=(20,5))],
        [sg.Button('Procurar',font='Famaly 12',button_color=('White','Blue')),sg.Button('Voltar',font='Famaly 12',button_color=('White','Green')),sg.Button('Sair',font='Famaly 12',button_color=('white','red'))],
        [sg.Output(size=(30,2))]
    ]    
    return sg.Window('Consulta de Password',layout=layout,finalize=True)

def janela_acres_gerar():
    sg.theme(theme)
    layout= [
        [sg.Text('       Pretende acrescentar ou gerar uma nova?',font='Famaly 15')],
        [sg.Text('              '),sg.Button('Adicionar',font='Famaly 12',button_color=('White','Blue')),sg.Text('  '),sg.Button('Gerar',font='Famaly 12',button_color=('White','Green')),sg.Text('  '),sg.Button('Sair',font='Famaly 12',button_color=('white','red'))]
    ]
    return sg.Window('Acrescentar ou Gerar',layout=layout,finalize=True)

def janela_acrescentar():
    sg.theme(theme)
    layout= [
        [sg.Text('Site / Software',font='Famaly 12',size=(15,1)),sg.Input(key='acres_site',size=(20,1))],
        [sg.Text('User / E-mail',font='Famaly 12',size=(15,1)),sg.Input(key='acres_user',size=(20,1))],
        [sg.Text('Password',font='Famaly 12',size=(15,1)),sg.Input(key='acres_pass',size=(20,1))],
        [sg.Button('Guardar',font='Famaly 12',button_color=('White','Blue')),sg.Button('Voltar',font='Famaly 12',button_color=('White','Green')),sg.Button('Sair',font='Famaly 12',button_color=('white','red'))],
        [sg.Output(key='_output_acrescentar',size=(30,2.5))]
    ]
    return sg.Window('Acrescentar Passwords',layout=layout,finalize=True)

def janela_gerar():
    sg.theme(theme)
    layout = [
            [sg.Text('Site/Software',font='Famaly 12',size=(15,1)), sg.Input(key='site',size=(20,1))],
            [sg.Text('E-mail/User',font='Famaly 12',size=(15,1)),sg.Input(key='user',size=(20,1))],
            [sg.Text('Quantidade de caracteres',font='Famaly 12',size=(20,1)),sg.Combo(values=list(range(30)),key='total_chars',default_value=5, size=(4,1))],
            [sg.Output(size=(32,2),key='output')],
            [sg.Button('Gerar Senha',font='Famaly 12',button_color=('White','Blue')),sg.Button('Continuar',font='Famaly 12',button_color=('White','Green')),sg.Button('Sair',font='Famaly 12',button_color=('white','red'))]
    ]
    return sg.Window('Gerar Password',layout=layout,finalize=True)

def janela_final():
    sg.theme(theme)
    layout= [
        [sg.Text('    Pretende continuar?',font='Famaly 12',size=(20,1))],
        [sg.Text('      '),sg.Button('Sim',font='Famaly 12',button_color=('White','Green')),sg.Button('Sair',font='Famaly 12',button_color=('white','red'))]
    ]
    return sg.Window('Continuar',layout=layout,finalize=True)


#função para escrever no ficheiro uma pass nova
def write_file_new(nova_senha,values):
    with open('Senhas.txt','a', newline='') as arquivo:
            arquivo.write(f"Site: {values['site']}  User_Name: {values['user']}  Nova Senha: {nova_senha}")
            arquivo.write('\n')
           
#função para acrecentar a base de dados
def write_file_add(values):
    #acrescentar a bd
    with open('Senhas.txt','a', newline='') as arquivo:
            arquivo.write(f"Site: {values['acres_site']}  User_Name: {values['acres_user']}  Nova Senha: {values['acres_pass']}")
            arquivo.write('\n')
    print('Guardado com sucesso!')

#funçao para procurar a pass
def procurar_pass(site):
    #abrir fichieiro e procurar pass
    arquivo = open('Senhas.txt','r')
    linha_ficheiro = arquivo.readline()
    while linha_ficheiro:
        site_pro=linha_ficheiro.split()
        if site_pro[1]== site:
            passe = site_pro[6]
            arquivo.close()
            return passe
        linha_ficheiro=arquivo.readline() 
    arquivo.close()
    return False               

def gerar_senha(values):
        char_list = 'ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz123456789!#$&'
        chars = random.choices(char_list,k=int(values['total_chars']))
        new_pass = ''.join(chars)
        return new_pass


#Criar janelas iniciais
janela1,janela2,janela3,janela4,janela5,janela6 = janela_inicial(),None,None,None,None,None

#criar  um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    #Quando a janela for fechada
    if window == janela1 and event == 'Sair' or event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Sair' or event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == 'Sair' or event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == 'Sair' or event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == 'Sair' or event == sg.WIN_CLOSED:
        break
    if window == janela6 and event == 'Sair' or event == sg.WIN_CLOSED:
        break
    # ir para próxima janela_consultar
    if window == janela1 and event == 'Consultar':
        janela2 = janela_consultar()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    #ir procurar a pass
    if window == janela2 and event == 'Procurar':
        search_site = values['consulta_site']
        senha_founded = procurar_pass(search_site)
        if senha_founded == False:
            print('Senha não encontrada!')
        print('Senha: '+senha_founded)
        print ('== Concluído ==')
    
    #ir para acrescentar ou gerar
    if window == janela1 and event == 'Adicionar Password':
        janela3 = janela_acres_gerar()
        janela1.hide()
    #ir para acrescentar
    if window == janela3 and event == 'Adicionar':
        janela3.hide()
        janela4 = janela_acrescentar()
    if window == janela4 and event == 'Guardar':
        write_file_add(values)
    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela3.un_hide()    
    if window == janela3 and event == 'Gerar':
        janela3.hide()
        janela5 = janela_gerar()
    if  window == janela5 and event == 'Gerar Senha':
        nova_senha = gerar_senha(values)
        print('====== Nova Senha ======')
        print('====== '+nova_senha+' ======')
        write_file_new(nova_senha,values)
    if window == janela5 and event == 'Continuar':
        janela5.hide()
        janela6 = janela_final()
    if window == janela6 and event == 'Sim':
        janela6.hide()
        janela1.un_hide()

