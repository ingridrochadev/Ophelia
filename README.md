# Ophelia

Este é um sistema de Gerenciamento Eletrônico de Documentos (GED) com Reconhecimento Óptico de Caracteres (OCR) desenvolvido para automatizar a verificação de documentos de viagem, especialmente vistos, no contexto de viagens aos Estados Unidos. O sistema é projetado para melhorar a eficiência e precisão da verificação de documentos, reduzindo o tempo e os recursos necessários para processar passageiros em aeroportos.

**Funcionalidades Principais**

Recebimento e Processamento de Documentos:

O sistema é capaz de receber documentos de viagem digitalizados, mais especificamente vistos.
Utiliza OCR para extrair informações-chave dos documentos, como nome, data de nascimento, nacionalidade, tipo de visto, data de validade do visto, entre outros.

Verificação de Autenticidade e Validade:

Verifica os tipos de vistos, alertando para eventuais necessidades de documentação adicional e a validade dos documentos de viagem.
Fornece feedback imediato sobre a elegibilidade do passageiro para viajar aos EUA com base nas informações extraídas dos documentos.

Integração e Compatibilidade:

Integra-se com o sistema de embarque, para que o passageiro seja admitido ou não no voo.

Segurança e Conformidade:

Segue as melhores práticas de segurança de dados para proteger as informações dos passageiros.

**Solução Proposta:**

Para lidar com esses desafios, a Ophelia propõe a implementação de um sistema de Gerenciamento Eletrônico de Documentos (GED) com Reconhecimento Óptico de Caracteres (OCR). A solução inclui:

-   Digitalização de Documentos: Todos os vistos serão digitalizados e armazenados eletronicamente no sistema GED.

-   OCR e Indexação Automática: Após a digitalização, a tecnologia OCR será utilizada para extrair texto dos documentos digitalizados. Os documentos serão automaticamente indexados com base em informações-chave, como número do visto, passaporte e id do passageiro.

-   Gerenciamento de Workflow: O sistema GED será configurado com fluxos de trabalho automatizados para processar documentos de forma eficiente. Por exemplo, vistos serão lidos automaticamente para auto-preenchimento do cadastro e encaminhadas para aprovação ou negação do embarque.

-   Controle de Acesso e Segurança: Medidas de segurança robustas serão implementadas para proteger a confidencialidade e integridade dos documentos. O acesso aos documentos será controlado com base em funções e permissões de usuário para garantir conformidade com regulamentações de privacidade de dados.

**Benefícios Esperados:**

-   O sistema deve usar PostegreSQL como armazenamento
-   Autenticação e gestão de usuários: implementação de registro de usuários, edição de perfil, login e logout
-   Interface intuitiva: desenvolvimento de uma interface de usuário amigável e fácl de usar para o propósito do sistema
-   A interface gráfica pode ser criada em Streamlit


Instalação e Configuração:

Clonar o repositório do sistema: git clone [https://github.com/ingridrochadev/Ophelia]
Instalar as dependências do sistema: 
Configurar as credenciais de acesso aos sistemas externos, como bancos de dados e APIs de integração.
Executar o sistema: 
Contribuição:

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues relatando problemas ou sugestões de melhorias. Pull requests também são aceitos.
