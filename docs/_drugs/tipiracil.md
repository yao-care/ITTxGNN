---
layout: default
title: Tipiracil
parent: Solo previsione del modello (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "tipiracil"
predicted_indications: ["cecum villous adenoma", "lipoma of colon", "rectosigmoid junction neoplasm", "cecum neuroendocrine tumor G1", "colonic lymphangioma", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "cavernous hemangioma of colon", "colorectal gastrointestinal stromal tumor"]
description: "Tipiracil: nuova indicazione prevista, Cecum villous adenoma (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Tipiracil
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

## Tipiracil: Cecum villous adenoma
{: .text-alpha }

## Sintesi in una frase

Tipiracil è un componente dell'associazione trifluridina/tipiracil (Lonsurf), utilizzata per il trattamento del carcinoma del colon-retto.
Il modello TxGNN prevede che possa essere efficace per l'**adenoma villoso del cieco**,
ma al momento **non sono presenti studi clinici né pubblicazioni** a supporto di questa indicazione: si tratta di una predizione puramente computazionale.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Cecum villous adenoma |
| Punteggio di predizione TxGNN | 0.9999 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 4 su 4) |
| Numero di autorizzazioni | 4 (valide: 4) |
| Decisione raccomandata | Hold (sospendere) |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Sulla base delle informazioni note, tipiracil è un componente dell'associazione con la trifluridina; agisce come inibitore della timidina fosforilasi, che previene la degradazione della trifluridina e ne aumenta l'esposizione. La sua efficacia nel carcinoma del colon-retto è documentata, ma da solo non possiede attività citotossica diretta.

Il legame con l'adenoma villoso del cieco si basa soprattutto sulla vicinanza tissutale: si tratta di una lesione benigna dello stesso tratto intestinale in cui l'associazione è usata per la malattia maligna. Non esistono tuttavia studi o dati mirati che indichino un beneficio in una lesione benigna, e la similarità con l'indicazione originale non è stata valutata.

Anche le altre nove predizioni di vertice (per esempio lipoma del colon, neoplasia della giunzione retto-sigmoidea, tumore neuroendocrino G1 del cieco, tumore stromale gastrointestinale colorettale) restano a livello L5 o L4 e, nel complesso, hanno un razionale meccanicistico debole. La neoplasia della giunzione retto-sigmoidea è verosimilmente già coperta dall'indicazione per il carcinoma colorettale, quindi non rappresenta un vero riposizionamento.

---

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati a questa indicazione.

---

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata a questa indicazione.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 044856019 | LONSURF 20 cpr rivestite 15 mg + 6,14 mg (Servier) | Compresse rivestite | Valida |
| 044856033 | LONSURF 60 cpr rivestite 15 mg + 6,14 mg (Servier) | Compresse rivestite | Valida |
| 044856045 | LONSURF 20 cpr rivestite 20 mg + 8,19 mg (Servier) | Compresse rivestite | Valida |
| 044856060 | LONSURF 60 cpr rivestite 20 mg + 8,19 mg (Servier) | Compresse rivestite | Valida |

Nei dati compilati non sono riportati il testo dell'indicazione approvata (la colonna indica quindi lo stato dell'autorizzazione) né la forma farmaceutica; la forma «compresse rivestite» è desunta dal nome del prodotto.

---

## Citotossicità

| Voce | Contenuto |
|------|------|
| Classificazione di citotossicità | Tipiracil in sé non ha attività citotossica diretta; è associato alla trifluridina, un analogo nucleosidico citotossico (antimetabolita) |
| Rischio di mielosoppressione | Per l'associazione, fare riferimento alle avvertenze e precauzioni del foglietto illustrativo |
| Classificazione di emetogenicità | Fare riferimento alle avvertenze e precauzioni del foglietto illustrativo |
| Parametri da monitorare | Emocromo con formula, funzionalità epatica e renale (secondo la pratica clinica per i citotossici) |
| Protezione nella manipolazione | Per l'associazione, seguire le norme di manipolazione dei farmaci citotossici |

---

## Considerazioni sulla sicurezza

**Interazioni farmacologiche**: dai dati compilati risultano 14 interazioni, 13 di livello moderato:

- Cimetidina
- Tafenoquina
- Ketoconazolo
- Brigatinib
- Crizotinib
- Encorafenib
- Etinilestradiolo
- Lenvatinib
- Medrossiprogesterone acetato
- Megestrolo acetato
- Ribociclib
- Rucaparib
- Vandetanib

È inoltre riportata un'interazione di tipo farmacologico con la proteina non strutturale 15 dei coronavirus (SARS-CoV-2), priva di classificazione di gravità e senza rilevanza clinica stabilita.

Per avvertenze e controindicazioni, fare riferimento al foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione per l'adenoma villoso del cieco si basa solo sul modello (livello L5), senza studi clinici né letteratura.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA
- Chiarimento dello stato regolatorio in Italia (autorizzazioni annullate)
- Studi preclinici o clinici che valutino tipiracil/trifluridina nell'adenoma villoso, con la dovuta cautela sul rapporto rischio-beneficio in una lesione benigna
- Analisi della similarità con l'indicazione originale e della compatibilità delle vie di somministrazione
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

