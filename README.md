# GHOSTPH
Isenção de responsabilidade

Quaisquer ações e/ou atividades relacionadas ao GHOSTPH são de sua exclusiva responsabilidade. A utilização indevida deste conjunto de ferramentas pode resultar em acusações criminais contra as pessoas em questão. Os contribuidores não serão responsabilizados no caso de qualquer acusação criminal ser movida contra qualquer indivíduo que utilize indevidamente este kit de ferramentas para infringir a lei.

Este kit de ferramentas contém materiais que podem ser potencialmente prejudiciais ou perigosos para as redes sociais . Consulte as leis da sua província/país antes de acessar, usar ou de qualquer outra forma utilizar isso de maneira errada.

Esta ferramenta é feita apenas para fins educacionais . Não tente violar a lei com nada contido aqui. Se esta é a sua intenção, então dê o fora daqui !

Isso apenas demonstra "como funciona o GHOSTPH". Você não deve usar indevidamente as informações para obter acesso não autorizado às redes sociais de alguém . No entanto, você pode tentar isso por sua própria conta e risco.

# Características
° Páginas de login mais recentes e atualizadas.
° Amigável para iniciantes
° Várias opções de tunelamento
° Host local
° Cloudflared
° LocalXpose
° Suporte a URL de máscara
° Suporte Docker

Explicação dos principais pontos:

O script descobre hosts ativos na rede via ARP (camada 2).
Para cada host, faz um scan de portas TCP comuns usando pacotes SYN.
Tenta identificar o nome do host via DNS reverso.
O código é comentado para facilitar o entendimento.
Atenção:

Execute como administrador/root para funcionar corretamente.
Use apenas em redes autorizadas e para fins educacionais.

# Instalação de Dependências
Antes de executar o GHOSTPH, certifique-se de ter instalado as dependências necessárias. Você pode fazer isso executando o seguinte comando:

```
pip install scapy
```
