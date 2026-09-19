---
layout: default
title: Letermovir
parent: Solo previsione del modello (L5)
nav_order: 134
evidence_level: L5
indication_count: 1
---

# Letermovir
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

# Letermovir: dalla profilassi della CMV alla candidosi vulvovaginale

## Riassunto in una frase

Letermovir è un agente antivirale sviluppato specificamente per la profilassi dell'infezione da citomegalovirus (CMV) nei riceventi di trapianto di cellule staminali ematopoietiche. Il modello TxGNN prevede che potrebbe essere efficace per la **Candidosi Vulvovaginale**, tuttavia **zero trial clinici** e **zero pubblicazioni** attualmente supportano questa direzione — l'evidenza si situa al livello più basso (L5), e l'analisi meccanicistica suggerisce fortemente che si tratti di un falso positivo topologico del grafo di conoscenza piuttosto che di un genuino segnale farmacologico.

---

## Panoramica rapida

| Voce | Contenuto |
|------|----------|
| Indicazione originale | Profilassi della CMV nei riceventi di trapianto di cellule staminali ematopoietiche |
| Indicazione nuova prevista | Candidosi Vulvovaginale |
| Punteggio di predizione TxGNN | 99.88% |
| Livello di evidenza | L5 |
| Stato di commercializzazione in Italia | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospendere |

---

## Perché questa predizione è ragionevole?

Attualmente, dati dettagliati sul meccanismo d'azione non sono formalmente disponibili in questo Pacchetto di Evidenze. Sulla base della farmacologia nota, Letermovir inibisce selettivamente il **complesso terminasi virale della CMV** (subunità UL51/UL56/UL89) — un enzima che il virus utilizza per scindere e confezionare il DNA appena replicato nei capsidi dei virioni. Questo meccanismo è straordinariamente specifico per l'herpesvirus umano 5 (CMV) e non ha attività documentata contro alcun patogeno fungino.

La candidosi vulvovaginale è causata da specie di *Candida* (prevalentemente *C. albicans*), la cui patogenesi coinvolge la biosintesi dell'ergosterolo e la sintesi della parete cellulare β-1,3-glucano — vie biochimiche completamente non correlate agli enzimi terminasi del DNA virale. Non esiste un ponte biologico stabilito o plausibile tra il meccanismo antivirale di Letermovir e l'attività antifungina.

Il punteggio TxGNN straordinariamente elevato (99.88%) quasi certamente riflette un **falso positivo topologico del grafo di conoscenza**: i riceventi di trapianto di cellule staminali ematopoietiche immunosoppressi ricevono Letermovir per la profilassi della CMV mentre simultaneamente presentano rischio elevato di infezioni fungine opportunistiche, inclusa la candidosi. Questa co-occorrenza a livello di paziente crea co-associazione spuria dei nodi nel grafo di conoscenza — un artefatto statistico, non una relazione farmacologica.

---

## Evidenza dai trial clinici

Attualmente non sono registrati trial clinici correlati.

---

## Evidenza dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

---

## Considerazioni di sicurezza

Fare riferimento al foglio illustrativo per le informazioni di sicurezza.

---

## Conclusioni e passi successivi

**Decisione: Sospendere**

**Razionale:**
La predizione TxGNN che collega Letermovir alla candidosi vulvovaginale è valutata come un falso positivo topologico del grafo di conoscenza senza base meccanicistica, senza supporto da trial clinici, e senza evidenza dalla letteratura (Livello di evidenza L5). Perseguire questa indicazione senza alcun razionale biologico non sarebbe un utilizzo responsabile delle risorse di sviluppo.

**Per riconsiderare questa decisione, sarebbe necessario:**
- Dati in vitro che dimostrino qualsiasi attività di Letermovir contro specie di *Candida*
- Un'ipotesi meccanicistica credibile che spieghi come l'inibizione della terminasi di CMV potrebbe produrre effetti antifungini
- Almeno uno studio preclinico (modello animale o studi su cellule) che dimostri l'efficacia in un contesto di infezione fungina

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

