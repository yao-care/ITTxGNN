---
layout: default
title: Pioglitazone
parent: Solo previsione del modello (L5)
nav_order: 352
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

# Pioglitazone: dal diabete mellito di tipo 2 all'opsismodisplasia

## Sintesi

Il pioglitazone è un antidiabetico orale, originariamente impiegato nel trattamento del diabete mellito di tipo 2.
Il modello TxGNN prevede che possa essere efficace per l'**opsismodisplasia**, una rara displasia scheletrica, con un punteggio molto alto (99,59%).
Tuttavia, per questa indicazione non risultano **né sperimentazioni cliniche né pubblicazioni**: la previsione si basa solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Diabete mellito di tipo 2 (dalla knowledge graph TxGNN; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Opsismodisplasia |
| Punteggio di predizione TxGNN | 99,59% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 15 (tutte cancellate; 0 valide) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Per i dati compilati per questo report non è disponibile una descrizione dettagliata del meccanismo d'azione. In base alle conoscenze generali, il pioglitazone è un agonista di PPAR-gamma e un insulino-sensibilizzante, la cui efficacia nel diabete di tipo 2 è documentata.

L'opsismodisplasia è causata da mutazioni di INPPL1 (carenza di SHIP2), che coinvolgono la via di segnalazione PI3K/insulina e la crescita ossea endocondrale. Un nesso con il pioglitazone sarebbe solo indiretto e speculativo: **non è stato stabilito alcun legame meccanicistico**. Il punteggio elevato deriva esclusivamente dalle associazioni nel grafo di conoscenza e non è una prova di efficacia.

Tra le altre indicazioni previste figurano la sindrome della persona rigida classica e la sindrome dell'arto rigido focale (punteggio 99,50%), la sindrome da disfunzione tiamino-responsiva, diverse lipodistrofie localizzate e l'agenesia pancreatica. Anche queste restano ipotesi senza evidenze cliniche. In particolare, per l'agenesia pancreatica il pioglitazone richiede insulina endogena per agire e non può sostituire le cellule beta mancanti, quindi non è appropriato come terapia primaria.

## Evidenze dagli studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

Attualmente non risulta letteratura correlata per l'opsismodisplasia.

Per completezza, per la quarta indicazione prevista, l'agenesia pancreatica, sono state recuperate 7 pubblicazioni. Riguardano il diabete di tipo 2 e i tiazolidinedioni in generale, non la malattia in questione, e offrono quindi solo evidenza indiretta sulla classe di farmaci.

## Informazioni sul mercato italiano

Tutte le 15 autorizzazioni sono cancellate; nessuna è attualmente valida. Il testo dell'indicazione approvata non è disponibile.

| N. autorizzazione | Prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 034946018 | ACTOS 28 cpr 15 mg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 034946044 | ACTOS 28 cpr 30 mg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 034946121 | ACTOS 28 cpr 45 mg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 040476032 | Pioglitazone 28 cpr 15 mg | Mylan SpA | Cancellata |
| 042677221 | Pioglitazone 28 cpr 45 mg | Accord Healthcare SLU | Cancellata |

## Considerazioni di sicurezza

- **Controindicazioni suggerite dal grafo di conoscenza** (non derivate dal foglio illustrativo): insufficienza cardiaca congestizia, malattie renali, malattie epatiche, malattie della colecisti, insufficienza surrenalica/malattia di Addison, ipopituitarismo e deficit di ormone della crescita, malattie del timo, malattie infettive.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni (fonte DDInter). Tra quelle di livello moderato: abiraterone, acetazolamide, alpelisib, epinefrina, fenilefrina, pseudoefedrina, formoterolo, salbutamolo, idroclorotiazide, idrocortisone, etanolo e abametapir (topico). Tra quelle di livello minore: nifedipina, etinilestradiolo e vari corticosteroidi topici.

Avvertenze e controindicazioni ufficiali del foglio illustrativo AIFA non sono disponibili: consultare il foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione è basata solo sul modello (L5), senza studi clinici o letteratura e senza un legame meccanicistico chiaro. Inoltre in Italia non esistono autorizzazioni valide e il profilo di sicurezza ufficiale non è disponibile.

**Per procedere è necessario:**
- Acquisire e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per lo screening di sicurezza
- Ottenere i dati sul meccanismo d'azione (ad es. da DrugBank)
- Condurre una valutazione preclinica del nesso tra PPAR-gamma/insulino-sensibilizzazione e la via INPPL1/SHIP2
- Valutare la fattibilità regolatoria, dato che tutte le autorizzazioni italiane sono cancellate
- Eventualmente riconsiderare altre indicazioni previste con razionale biologico più plausibile (ad es. le lipodistrofie)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

