############
# Postgres #
############
# import psycopg2

# try:
    # con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
    # cur = con.cursor()
    # cur.execute("insert into scripts(nome, conteudo) values('devops', 'projeto de python')")
    # cur.execute("update scripts set nome='devops_novo' where nome='devops' ")
    # cur.execute("select * from scripts")
    # print(cur.fetchone())
    # con.commit()
    # print('Registro criado com sucesso')
    
# except Exception as e:
#     print(f'Erro: {e}')
#     print('Fazendo rollback')
#     con.rollback()

# finally:
#     print('Finalizando conexao com o banco de dados')
#     cur.close()
#     con.close()


#########################################################



#########
# MySQL #
#########

# import MySQLdb

# try:
#     con = MySQLdb.connect(host="localhost", user="developer", passwd="4linux", db="projetos")
#     cur = con.cursor()

    # cur.execute("insert into clientes(nome, endereco) values ('novo_nome', 'novo_endereco')")
    # cur.execute("select * from clientes")
    # print(cur.fetchone())
    # print(cur.fetchall())

#     con.commit()
#     print('Sucesso...')

# except Exception as e:
#     print(f'Erro: {e}')
#     con.rollback()

# finally:
#     print('Finalizando...')
#     cur.close()
#     con.close()

from pymongo import MongoClient

client = MongoClient('localhost')
db = client['dexterops']


def inserir_dado():
    try:
        db.fila.insert({"_id": 200,
                        "empresa": "4linux",
                        "cursos": [{
                                    "nome": "Python Fundamentals",
                                    "carga horaria": 40
                                    },
                                    {
                                    "nome": "Linux Fundamentals",
                                    "carga horaria": 40
                                    }
                                    ]
                        })
    except Exception as e:
        print(f'Erro: {e}')


def buscar_dados():

    for r in db.fila.find():
        print(f'Empresa {r["empresa"]}')
        for c in r["cursos"]:
            print("=============")
            print(f'Nome {c["nome"]} Carga Horária: {c["carga horaria"]}')

buscar_dados()