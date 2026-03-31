# ITTxGNN - Italia: Riposizionamento dei Farmaci

[![Website](https://img.shields.io/badge/Website-ittxgnn.yao.care-blue)](https://ittxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Previsioni di riposizionamento dei farmaci (drug repurposing) per l'Italia utilizzando il modello TxGNN.

## Avvertenza

- I risultati di questo progetto sono esclusivamente a scopo di ricerca e non costituiscono consulenza medica.
- I candidati al riposizionamento dei farmaci richiedono una validazione clinica prima dell'applicazione.

## Panoramica del Progetto

| Elemento | Quantita |
|----------|----------|
| **Report sui Farmaci** | 333 |
| **Previsioni Totali** | 7,794,696 |

## Metodi di Previsione

### Metodo del Grafo della Conoscenza (Knowledge Graph)
Interrogazione diretta delle relazioni farmaco-malattia nel grafo della conoscenza TxGNN, identificando potenziali candidati al riposizionamento basati sulle connessioni esistenti nella rete biomedica.

### Metodo di Apprendimento Profondo (Deep Learning)
Utilizza il modello di rete neurale pre-addestrato TxGNN per calcolare i punteggi di previsione, valutando la probabilita di nuove indicazioni terapeutiche per i farmaci approvati.

## Link

- Sito Web: https://ittxgnn.yao.care
- Articolo TxGNN: https://doi.org/10.1038/s41591-023-02233-x
