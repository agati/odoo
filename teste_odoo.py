import odoorpc


def conectaBd():
    # odoo = odoorpc.ODOO('107.170.32.11','jsonrpc', 80, 120, None, None)
    # odoo = odoorpc.ODOO('chocotech.trustcode.com.br','jsonrpc', 80, 120, None, None)


    # Verifica as bases disponíveis
    # print(odoo.db.list())

    # faz login
    # odoo.login('chocotech', 'demo', 'demo')
    odoo.login('procele', 'agati@procele.com.br', 'Unicef08@')

    # criando uma base de dados
    # odoo.db.create('admin', 'procele', demo=True, lang='pt_BR', admin_password='admin')

    # usuário logado
    user = odoo.env.user
    print(user.name)  # name of the user connected
    print(user.company_id.name)  # the name of its company
    versao = odoo.version
    print(versao)
    banco = odoo.db
    print(banco)
    #report = odoo.report
    #print(report)
    ambiente = odoo.env
    print(ambiente)

    print("*************** fim do conectaBd() *********************************")



def insereCliente(nome, email, telefone, endereco):

    if 'res.partner' in odoo.env:

        Partner = odoo.env['res.partner']
        partner_id = Partner.create({'name': nome, 'email': email, 'phone': telefone, 'street': endereco})
        print('Id do registro inserido vale:',partner_id)
        partner = Partner.browse(partner_id)
        print(partner)
        print("*************** fim do insereCliente() *********************************")
        return

def atualizaTelCliente(nome, valor):

    if 'res.partner' in odoo.env:
        partner = odoo.env['res.partner']
        partner_ids = partner.search([])
        print("Total de clientes na lista vale:", len(partner_ids))
        for linha in partner.browse(partner_ids):
            print(linha.name, linha.id, linha.phone)
            if linha.name==nome:
                print('ok')
                linha.phone=valor
                print(linha.name, linha.id, linha.phone)
        print("*************** fim do atualizaTelCliente() *********************************")
        return


def totalClientes():

    if 'res.partner' in odoo.env:
        partner = odoo.env['res.partner']
        partner_ids = partner.search([])
        print("Total de clientes na lista vale:", len(partner_ids))

        print("*************** fim do totalClientes() *********************************")
    return

def listaAlfabeticaClientes():
    if 'res.partner' in odoo.env:
        matriz_nomes=[]
        partner = odoo.env['res.partner']
        partner_ids = partner.search([])
        print("Total de clientes na lista vale:", len(partner_ids))
        for linha in partner.browse(partner_ids):
            print(linha.name, linha.id, linha.phone)
            matriz_nomes.append(linha.name)
        print("A matriz de nomes vale: ", matriz_nomes)
        matriz_nomes.sort()
        print("A matriz de nomes após sort vale: ", matriz_nomes)
        






    return

# inicio
odoo = odoorpc.ODOO('procele.odoo.com', 'jsonrpc', 80, 120, None, None)


# 1-Inserir (nome, email,telefone, endereco
conectaBd()
insereCliente('José da Silva', 'assai@guarana.com.br', '47 99184-1100', 'Rua das Alegrias, 777')

# 2-Atualiza cliente
atualizaTelCliente('José da Silva', '1111-1111')


#3-Consulta quantos clientes existem na base de dados
totalClientes()

#4-Listar os 10 primeiros clientes por ordem alfabética
listaAlfabeticaClientes()


quit()


