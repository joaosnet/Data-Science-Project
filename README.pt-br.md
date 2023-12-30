# Projeto Airbnb Rio - Previsão de Preços

![Tamanho do repositório do GitHub](https://img.shields.io/github/repo-size/joaosnet/Data-Science-Project?style=for-the-badge)
![Contagem de linguagens do GitHub](https://img.shields.io/github/languages/count/joaosnet/Data-Science-Project?style=for-the-badge)
![Forks do GitHub](https://img.shields.io/github/forks/joaosnet/Data-Science-Project?style=for-the-badge)
![Problemas abertos do Bitbucket](https://img.shields.io/bitbucket/issues/joaosnet/Data-Science-Project?style=for-the-badge)
![Pull requests abertos do Bitbucket](https://img.shields.io/bitbucket/pr-raw/joaosnet/Data-Science-Project?style=for-the-badge)
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/joaosnet/Data-Science-Project/blob/master/README.md)

<img align="right" height="256" src="screenshots/homepage.png"/>

## Contexto

No Airbnb, qualquer pessoa que possua um quarto ou qualquer tipo de propriedade (apartamento, casa, chalé, pousada, etc.) pode oferecer sua propriedade para aluguel diário.

Você cria seu perfil de anfitrião (pessoa que disponibiliza uma propriedade para aluguel diário) e cria o anúncio para sua propriedade.

Nesse anúncio, o anfitrião deve descrever as características da propriedade o mais detalhadamente possível, a fim de ajudar os locatários/viajantes a escolher a melhor propriedade para eles (e tornar seu anúncio mais atraente).

Existem várias personalizações disponíveis para o seu anúncio, desde requisitos de estadia mínima, preço, número de quartos, até políticas de cancelamento, taxas extras para hóspedes adicionais, requisitos de verificação de identidade para locatários, etc.

## Capturas de tela

### Captura de tela 1: Visualização do Mapa da Propriedade

![Visualização do Mapa da Propriedade](/screenshots/Property-Map-View.png)

_Figura 1: Visualização do Mapa da Propriedade_

## Nosso Objetivo

Construir um modelo de previsão de preços que permita a uma pessoa comum que possui uma propriedade determinar quanto deve cobrar pelo aluguel diário de sua propriedade.

Alternativamente, para o locatário comum, dado a propriedade que ele está procurando, ajudá-lo a determinar se essa propriedade tem um preço competitivo (abaixo da média para propriedades com as mesmas características) ou não.

## Dados Disponíveis, Inspirações e Créditos

Os conjuntos de dados foram obtidos no site Kaggle: [link](https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro)

Eles estão disponíveis para download abaixo da aula (se você baixar os dados diretamente do Kaggle, poderá encontrar resultados diferentes dos meus, pois os conjuntos de dados podem ter sido atualizados).

Se você preferir uma solução alternativa, podemos consultar a solução fornecida pelo usuário do Kaggle Allan Bruno no seguinte notebook: [link](https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb)

Você notará semelhanças entre a solução que desenvolveremos aqui e a dele, mas também algumas diferenças significativas no processo de construção do projeto.

- Os conjuntos de dados contêm preços de propriedades e suas respectivas características para cada mês.
- Os preços são dados em Real brasileiro (R$).
- Temos dados de abril de 2018 a maio de 2020, com exceção de junho de 2018, para o qual não há conjunto de dados disponível.

## Expectativas Iniciais

- Acredito que a sazonalidade possa ser um fator importante, pois meses como dezembro tendem a ser caros no Rio de Janeiro.
- A localização da propriedade deve fazer uma diferença significativa no preço, pois no Rio de Janeiro, a localização pode mudar completamente as características do local (segurança, beleza natural, atrações turísticas).
- Comodidades adicionais podem ter um impacto significativo, considerando que há muitos prédios e casas antigas no Rio de Janeiro.

Vamos explorar o quanto esses fatores impactam os preços e se existem outros fatores menos intuitivos que são extremamente importantes.

## 🤝 Contribuidores

<table>
  <tr>
    <td align="center">
      <a href="https://www.instagram.com/jaonativi/" title="Gerente de Projetos Desenvolvedor Backend">
        <img src="https://avatars.githubusercontent.com/u/87316339?v=4" width="100px;" alt="Foto do João Natividade no GitHub"/><br>
        <sub>
          <b>João Natividade</b>
        </sub>
      </a>
    </td>
  </tr>
</table>