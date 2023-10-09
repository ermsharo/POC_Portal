
Gerar link para arquivo[]
Usuario logado{
    No cliente usario forcencer usario e senha e receber um jwt 
    Usuario usar o jwt para validar as requisições
    Ver base de dados original e aplicar para o nosso lado{
        Como vamos inserir um usuario novo; 

    }

}



criação usuario 
Pega{
    usuario -> salva no banco
    senha -> encriptamos com a nossa cifra -> salva senha encriptada no banco
}

Login usuario{
    pega usario e senha{
        com a chave cifrada, verifica a senha de login e compara com a do banco. 
        baseado no id daquele usuario gera um jwt. 

        jwt: 1h
        informações de usuario
    }
}

Criar um cliente{
    Faz login; 
    Recebe um arquivo; 
    Vizualiza arquivos diponiveis; 
    Baixa arquivos; 
}


Recebe um arquivo{
    -> Manda o arquivo para o backend 
    -> Registra o arquivo no banco de dados,  especificando o acesso, o usuario, atributos e em qual momento foi hospedado. 
}
Vizualiza arquivos diponiveis{
    -> Verifica acesso aos usuarios
    -> traz os arquivos disponiveis para acesso
    -> Permite a busca aos arquivos baseadas nos termos de busca
    -> Pagina a entrega dos arquivos no cliente 
} 

Arrumar timezone




