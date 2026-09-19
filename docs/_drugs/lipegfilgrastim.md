---
layout: default
title: Lipegfilgrastim
parent: Solo previsione del modello (L5)
nav_order: 136
evidence_level: L5
indication_count: 5
---

# Lipegfilgrastim
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Lipegfilgrastim: Dalla neutropenia indotta da chemioterapia al disturbo primario del rilascio delle piastrine

## Riassunto in una frase

Il lipegfilgrastim è un fattore stimolante le colonie di granulociti (G-CSF) a lunga durata d'azione e glicopeguilato, utilizzato principalmente per ridurre la durata della neutropenia nei pazienti sottoposti a chemioterapia citotossica.
Il modello TxGNN prevede che potrebbe essere efficace per il **disturbo primario del rilascio delle piastrine**, con **0 studi clinici** e **0 pubblicazioni** che attualmente supportano questo indirizzo — facendo di questa una previsione solo da modello in questa fase.
Data l'assenza di prove corroboranti e la debole razionale meccanicistica, la raccomandazione attuale è **Mantenere**.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|---------|
| Indicazione originale | Nessun dato di indicazione approvata in Italia |
| Nuova indicazione prevista | Disturbo primario del rilascio delle piastrine |
| Punteggio di previsione TxGNN | 99.93% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Mantenere |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili in questo pacchetto di prove. In base alla sua classe farmacologica, il lipegfilgrastim è una forma glicopeguilata di filgrastim che agisce come agonista del G-CSF (fattore stimolante le colonie di granulociti) al recettore CSF3R. Questo attiva le cascate di segnalazione JAK2/STAT3 e PI3K/Akt, promuovendo la proliferazione, differenziazione e rilascio dei progenitori dei neutrofili dal midollo osseo. La modifica della glicopeguilazione estende la sua emivita rispetto al filgrastim standard, permettendo la somministrazione una volta per ciclo nei pazienti in chemioterapia.

L'indicazione nuova prevista — disturbo primario del rilascio delle piastrine — si riferisce a un difetto funzionale nell'esocitosi dei granuli α o dei granuli densi dalle piastrine, mediato da complessi proteici SNARE (ad es., VAMP-8, syntaxin-11) che sono strutturalmente e meccanicisticamente separati dall'asse di segnalazione G-CSF/CSF3R. Il G-CSF ha infatti effetti indiretti sui megacariociti (le cellule precursore delle piastrine) attraverso la segnalazione incrociata del recettore MPL o la secrezione stromale di IL-6, che potrebbe teoricamente influenzare la trombopoiesi. Tuttavia, questa influenza si riferisce alla quantità di piastrine piuttosto che alla macchina del rilascio dei granuli che è difettosa nei disturbi del rilascio — rendendo il ponte meccanicistico speculativo.

La previsione di TxGNN molto probabilmente riflette la **vicinanza del grafo di conoscenza ematopoietica**: i disturbi piastrinici e i disturbi neutrofili coabitano in vicinanze sovrapposte del grafo (nicchia di midollo osseo condivisa, antenati delle cellule staminali ematopoietiche, ambienti di citochine condivisi). Questa similarità topologica nel grafo di conoscenza non si traduce necessariamente in rilevanza funzionale o terapeutica. Nessun modello preclinico, studio clinico o letteratura pubblicata attualmente collega il lipegfilgrastim ai disturbi del rilascio dei granuli piastrinici.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato registrato.

---

## Evidenza da letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusione e prossimi passi

**Decisione: Mantenere**

**Razionale:**
Questa è una previsione solo da modello (L5) con zero prove cliniche o precliniche di supporto, e la connessione meccanicistica tra la segnalazione del recettore G-CSF e il rilascio dei granuli piastrinici mediato da SNARE è al massimo indiretta — il punteggio di TxGNN probabilmente riflette la vicinanza strutturale del grafo di conoscenza piuttosto che la plausibilità biologica.

**Per procedere, sono necessari i seguenti elementi:**

- **Conferma MOA**: Recuperare il record completo di DrugBank (DB13200) per caratterizzare formalmente il percorso G-CSF/CSF3R–JAK2/STAT3 e qualsiasi effetto megacariocitario documentato
- **Evidenza preclinica**: Identificare o commissionare studi di modelli in vitro/animali che esaminano l'effetto del lipegfilgrastim sulla secrezione dei granuli piastrinici prima che si formi qualsiasi ipotesi clinica
- **Revisione dello stato normativo**: Confermare se il lipegfilgrastim ha un'autorizzazione EMA (ce l'ha in Europa con il nome commerciale *Lonquex*) e valutare se esiste un'autorizzazione AIFA italiana, poiché ciò influenzerebbe il percorso normativo per il riposizionamento
- **Profilo di sicurezza nei disturbi ematologici**: Valutare il rischio di sanguinamento, il rischio di trombocitopenia e l'interazione emostatica nei pazienti con disturbi del rilascio delle piastrine — una popolazione in cui un intervento con fattore di crescita non ha una linea di base di sicurezza stabilita
- **Revisione delle indicazioni alternative**: Considerare le altre previsioni meglio classificate (ad es., retinopatia diabetica tramite mobilizzazione delle EPC) per determinare se qualcuna ha un supporto meccanicistico più forte prima di investire risorse in questo indirizzo

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

