---
layout: default
title: Lenograstim
parent: Prove moderate (L3-L4)
nav_order: 133
evidence_level: L4
indication_count: 4
---

# Lenograstim
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **4** 
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

# Lenograstim: Dalla neutropenia / mobilizzazione di cellule staminali al disordine primario di rilascio delle piastrine

## Riassunto monoriga

Lenograstim è un fattore ricombinante glicosilato di stimolazione della crescita dei granulociti (G-CSF), noto principalmente per ridurre la neutropenia indotta da chemioterapia e mobilizzare le cellule staminali ematopoietiche (HSC) precedentemente al trapianto.
Il modello TxGNN predice che potrebbe essere efficace per il **Disordine primario di rilascio delle piastrine**, con **13 trial clinici** identificati (tutti di rilevanza solo indiretta) e **nessuna letteratura pubblicata** che attualmente supporti questa direzione.
La base probatoria è scarsa: tutti i collegamenti con i trial risalgono all'utilizzo di mobilizzazione HSCT piuttosto che al trattamento diretto dei difetti di rilascio piastrinico, rendendo questa un'inferenza del grafo della conoscenza piuttosto che evidenza clinica.

---

## Panoramica rapida

| Voce | Contenuto |
|------|---------|
| Indicazione originale | Non disponibile (nessuna licenza registrata in Italia) |
| Indicazione nuova predetta | Disordine primario di rilascio delle piastrine |
| Punteggio predittivo TxGNN | 99.91% |
| Livello di evidenza | L4 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Hold |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono formalmente disponibili in questo Evidence Pack. Sulla base della farmacologia consolidata, lenograstim si lega al recettore G-CSF (G-CSFR/CD114), stimolando la proliferazione e la differenziazione dei precursori dei neutrofili. Crucialmente, G-CSFR è anche espresso sulle cellule progenitrici dei megacariociti — i precursori delle piastrine — significando che lenograstim potrebbe esercitare un'influenza secondaria e indiretta sulla produzione piastrinica. Tuttavia, il suo ruolo clinico primario è sempre stato il recupero dei neutrofili e la mobilizzazione delle HSC, non la funzione piastrinica.

Il disordine primario di rilascio delle piastrine comprende condizioni in cui le piastrine non riescono a scaricare il contenuto dei loro granuli (granuli densi, granuli alfa) all'attivazione. Si tratta di difetti strutturali o enzimatici nella biologia granulare — distinti dalla quantità piastrinica. Lenograstim non ha nessun meccanismo noto per riparare il confezionamento dei granuli o il macchinario di rilascio, quindi il collegamento tra il farmaco e questa indicazione è meccanisticamente indiretto al massimo.

Il percorso più plausibile catturato da TxGNN è il seguente: i gravi disordini di rilascio piastrinico refrattario sono teoricamente curabili da HSCT allogenico, che sostituisce la linea difettosa dei megacariociti con i progenitori sani di un donatore. Lenograstim appare frequentemente nei trial clinici di allo-HSCT come adiuvante nella mobilizzazione delle HSC. Il grafo della conoscenza di TxGNN probabilmente ha collegato i punti tramite il nodo condiviso **ematologia → allo-HSCT → lenograstim** — un'associazione legittima ma indiretta che non dovrebbe essere interpretata come evidenza terapeutica diretta per i disordini di rilascio piastrinico.

---

## Evidenza dei trial clinici

Tutti i 13 trial recuperati riguardano lenograstim nel contesto del trapianto di cellule staminali ematopoietiche. Nessuno studia direttamente lenograstim per il disordine primario di rilascio delle piastrine; tutti hanno un grado di rilevanza indiretta (Grado C). La tabella seguente esclude due trial chiaramente fuori tema (un trial antivirale COVID-19 e due trial di profilassi CMV) che sono stati restituiti come rumore di ricerca.

| Numero del trial | Fase | Stato | Arruolamento | Risultati chiave |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Fase 2 | Interrotto | 200 | HSCT da donatore non correlato per malignità ematologiche; lenograstim utilizzato per la mobilizzazione delle HSC del donatore — nessun endpoint di disordine di rilascio piastrinico |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fase 2 | Completato | 60 | Trapianto allogenico/singenico di cellule staminali ematiche per sarcomi pediatrici ad alto rischio; contesto di mobilizzazione di cellule staminali solo |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Fase 2 | Interrotto | 16 | Trapianto di sangue cordonale + infusione di cellule NK per leucemia mieloide non in RC; interrotto precocemente, non correlato alla funzione piastrinica |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Fase 2 | Completato | 19 | Studio di fattibilità di HSCT ad intensità ridotta per mutazioni GATA2; piccolo pilota, nessun focus sul disordine di rilascio piastrinico |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fase 1/2 | In reclutamento | 260 | Ottimizzazione della dose di ciclofosfamide post-trapianto per la profilassi della GVHD dopo PBSCT; lenograstim è un adiuvante di mobilizzazione, non l'intervento primario |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fase 2 | In reclutamento | 358 | Trial platform che confronta regimi di profilassi GVHD in PBSCT da donatore non correlato mismatched; lenograstim non è il farmaco dello studio |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Fase 3 | In reclutamento | 156 | HSCT autologo vs miglior terapia disponibile per SM ricorrente-remittente resistente al trattamento; ruolo limitato di lenograstim nella mobilizzazione |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Fase 2 | Completato | 9 | HSCT autologo per LES grave; pilota molto piccolo (n=9), malattia ed endpoint non correlati ai disordini di rilascio piastrinico |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Fase 1/2 | Completato | 147 | HSCT allogenico non mieloablativi per malignità ematologiche; lenograstim utilizzato nella fase di mobilizzazione del donatore |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Fase 1 | Ritirato | 0 | Studio di trapianto di midollo osseo da donatore non correlato mismatched crioconservato; ritirato prima di arruolare pazienti — nessun dato utilizzabile |

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Lenograstim non ha autorizzazioni di prodotti registrate in Italia e non è attualmente commercializzato. Non ci sono licenze da visualizzare.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Razionale:**
Nonostante un punteggio TxGNN elevato (99.91%), la previsione riflette un'inferenza del grafo della conoscenza tramite percorsi HSCT piuttosto che evidenza clinica diretta — nessun trial ha testato lenograstim contro i disordini di rilascio piastrinico, nessuna letteratura documenta questo uso, e il meccanismo del farmaco non affronta la patofisiologia centrale dei difetti di rilascio dei granuli. L'assenza di un'autorizzazione di commercializzazione italiana aggiunge un ulteriore ostacolo normativo prima che qualsiasi sviluppo clinico potrebbe iniziare.

**Per procedere, è necessario quanto segue:**
- Documentazione formale del MOA da DrugBank o da un foglio illustrativo approvato per confermare se sono descritti effetti sulla biologia dei granuli o sulla funzione piastrinica
- Revisione mirata della letteratura per rapporti di casi o studi meccanicistici che esplorino gli effetti di G-CSF sul rilascio dei granuli densi/alfa piastrinici
- Verifica se l'allo-HSCT ha risultati curativi documentati specificamente nei disordini primari di rilascio piastrinico, e se lenograstim era l'agente di mobilizzazione utilizzato in quei casi
- Dati preclinici (in vitro / murini) che valutano l'effetto diretto di lenograstim sulla biogenesi dei granuli dei megacariociti
- Valutazione del percorso normativo italiano per il perseguimento di una nuova indicazione da un punto di partenza attualmente non commercializzato

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

