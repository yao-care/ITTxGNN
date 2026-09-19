---
layout: default
title: Dupilumab
parent: Solo previsione del modello (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Dupilumab
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relazione di valutazione farmaceutica

</div>

# Dupilumab (DB12159): Nessuna previsione di riutilizzo TxGNN disponibile

## Riassunto in una frase

Dupilumab (Dupixent) è un anticorpo monoclonale biologico che bersaglia il recettore IL-4Rα, utilizzato per trattare le condizioni infiammatorie di tipo 2, inclusa la dermatite atopica e l'asma. Il Pacchetto di evidenze attuale contiene **nessuna previsione di riutilizzo TxGNN**, poiché i dati di input critici — incluso il meccanismo d'azione, le indicazioni originali e le informazioni sulla sicurezza — non sono stati caricati con successo. Una valutazione significativa del riutilizzo non può procedere fino a quando queste lacune di dati non vengono risolte.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Dati non caricati (dermatite atopica / malattia infiammatoria di tipo 2 secondo fonti pubbliche) |
| Indicazione nuova prevista | Nessuna previsione disponibile |
| Punteggio di previsione TxGNN | N/A |
| Livello di evidenza | N/A — il modello non ha prodotto alcun output |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **Rinviare** |

---

## Riepilogo delle lacune di dati

Il Pacchetto di evidenze è stato generato con un solo input confermato (`drugbank`), e due lacune critiche sono state segnalate al momento della creazione:

| ID lacuna | Categoria | Elemento mancante | Gravità | Impatto |
|-----------|-----------|-------------------|---------|---------|
| DG001 | Livello del farmaco | Avvertenze del foglio illustrativo / controindicazioni | **Bloccante** | Non è possibile procedere al pre-screening di sicurezza (S1) |
| DG002 | Livello del farmaco | Meccanismo d'azione (MOA) | Alto | Analisi della rilevanza meccanicistica non disponibile |

Poiché `predicted_indications` è vuoto, tutte le sezioni successive (evidenza da trial clinici, evidenza da letteratura, analisi meccanicistica) non possono essere generate.

---

## Considerazioni sulla sicurezza

Si rimanda al foglio illustrativo per le informazioni sulla sicurezza.
Nessun dato di interazione farmaco-farmaco è stato trovato per Dupilumab nelle fonti consultate.

---

## Conclusioni e prossimi passi

**Decisione: Rinviare**

**Fondamento logico:**
La pipeline TxGNN ha restituito zero candidati di riutilizzo per Dupilumab, molto probabilmente perché gli input richiesti dal modello — inclusi i graph embeddings MOA e le etichette di indicazione originale — erano assenti dal Pacchetto di evidenze. Nessuna revisione dell'evidenza è possibile senza un set di previsioni valido.

**Per procedere, è necessario quanto segue:**

- [ ] Ri-eseguire la previsione TxGNN con dati completi del nodo farmaco (MOA, categorie DrugBank, etichette di indicazione note)
- [ ] Caricare il foglio illustrativo (TFDA/EMA/FDA) per estrarre le indicazioni approvate, le avvertenze e le controindicazioni
- [ ] Confermare la MOA di DrugBank: Dupilumab è un antagonista di IL-4Rα (blocca la segnalazione di IL-4 e IL-13); questo dovrebbe essere recuperabile tramite l'API di DrugBank (DB12159)
- [ ] Verificare lo stato di autorizzazione commerciale in Italia (AIFA) / Taiwan (TFDA) — attualmente entrambi mostrano 0 licenze, il che potrebbe essere un problema di recupero dati piuttosto che una vera non-approvazione
- [ ] Una volta che le previsioni sono disponibili, ri-generare il Pacchetto di evidenze v5 e ri-eseguire questo rapporto

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

