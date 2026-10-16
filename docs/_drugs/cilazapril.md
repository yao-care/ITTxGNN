---
layout: default
title: Cilazapril
parent: Prove moderate (L3-L4)
nav_order: 107
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Cilazapril: nuova indicazione prevista, Ipertensione polmonare da malattia polmonare e/o ipossia (livello di evidenza L4). Indicazione originale: Ipertensione arteriosa (indicazione ricavata dal graf…"
monitor_inn: "CILAZAPRIL"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "malignant renovascular hypertension"]
---

# Cilazapril
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

# Cilazapril: Dall'ipertensione arteriosa all'ipertensione polmonare da malattia polmonare e/o ipossia

## Riepilogo in breve

Cilazapril è un inibitore dell'enzima di conversione dell'angiotensina (ACE), originariamente utilizzato per il trattamento dell'ipertensione arteriosa.
Il modello TxGNN prevede che possa essere efficace per l'**ipertensione polmonare da malattia polmonare e/o ipossia** (punteggio 99,2%).
Le evidenze disponibili sono però limitate: **nessuno studio clinico** registrato e **4 pubblicazioni** precliniche (studi su animali e in vitro).

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione arteriosa (indicazione ricavata dal grafo di conoscenza; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Ipertensione polmonare da malattia polmonare e/o ipossia |
| Punteggio di predizione TxGNN | 99,2% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (entrambe cancellate) |
| Decisione raccomandata | Hold (sospendere; trattare come domanda di ricerca) |

---

## Perché questa predizione è ragionevole?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione. In base alle conoscenze di classe, cilazapril inibisce l'ACE, riducendo la produzione di angiotensina II, un potente vasocostrittore, con conseguente calo della pressione sistemica. La sua efficacia nell'ipertensione arteriosa è nota e, sul piano meccanicistico, potrebbe essere applicabile anche alla circolazione polmonare.

La relazione tra indicazione originale e nuova è plausibile: il sistema renina-angiotensina locale dell'arteria polmonare è coinvolto nello sviluppo dell'ipertensione polmonare ipossica. Gli studi preclinici suggeriscono che l'inibizione dell'ACE possa ridurre la vasocostrizione e il rimodellamento vascolare indotti dall'ipossia. Si tratta però di un'evidenza indiretta, limitata a modelli animali e cellulari.

Gli altri esiti previsti dal modello (ipertensione polmonare a meccanismo multifattoriale non chiaro, malattia renale ipertensiva maligna, ipertensione renovascolare maligna) hanno punteggi simili (circa 99,1–99,2%) ma **nessuna evidenza** clinica o bibliografica: il loro sostegno è puramente computazionale (livello L5, decisione Hold).

---

## Evidenze da studi clinici

Al momento non risulta registrato alcuno studio clinico correlato.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [1708054](https://pubmed.ncbi.nlm.nih.gov/1708054/) | 1991 | Studio sull'animale | J Cardiovasc Pharmacol | Effetti di cilazapril sulla struttura delle arterie polmonari in ratti esposti a ipossia cronica (prevenzione dell'ispessimento della tunica media) |
| [7712584](https://pubmed.ncbi.nlm.nih.gov/7712584/) | 1994 | Studio sull'animale | Zhonghua Jie He He Hu Xi Za Zhi | Effetto protettivo di cilazapril contro l'aumento della pressione arteriosa polmonare media e la riduzione della PaO2 nei ratti con ipossia cronica |
| [10072805](https://pubmed.ncbi.nlm.nih.gov/10072805/) | 1997 | Studio meccanicistico preclinico | Zhonghua Jie He He Hu Xi Za Zhi | Ruolo dell'ACE dell'arteria polmonare nello sviluppo dell'ipertensione polmonare ipossica |
| [1378120](https://pubmed.ncbi.nlm.nih.gov/1378120/) | 1992 | Studio in vitro | J Cardiovasc Pharmacol | Cilazapril e captopril accelerano il recupero dall'ipossia in aggregati di cellule miocardiche in coltura |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 027460043 | INIBACE 14 cpr rivestite 5 mg (CHEPLAPHARM ARZNEIMITTEL GMBH) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |
| 027464041 | INITISS 14 cpr rivestite 5 mg (TEOFARMA Srl) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |

---

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: l'unica voce disponibile riguarda il bersaglio farmacologico, l'enzima di conversione dell'angiotensina (ACE), di cui cilazapril è inibitore; non sono segnalate interazioni con altri farmaci.
- **Nota di classe**: gli ACE-inibitori comportano rischi noti in caso di stenosi bilaterale dell'arteria renale (peggioramento acuto della funzione renale), da valutare con attenzione in particolare per l'ipertensione renovascolare.

Per le avvertenze e le controindicazioni complete, fare riferimento al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold (trattare come domanda di ricerca)**

**Motivazione:**
Il punteggio TxGNN è molto alto, ma le evidenze si limitano a studi preclinici (animali e in vitro) senza alcuno studio sull'uomo. Inoltre, tutte le autorizzazioni italiane risultano cancellate, il che limita la praticabilità dello sviluppo.

**Per procedere è necessario:**
- Acquisire i dati di meccanismo d'azione (MOA) da DrugBank
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni (lacuna bloccante per la valutazione di sicurezza)
- Verificare con revisione sistematica la presenza di studi clinici sull'uomo con ACE-inibitori nell'ipertensione polmonare da ipossia
- Valutare la fattibilità regolatoria e commerciale, considerato lo stato di mercato "solo cancellate"
- Se si intende procedere, progettare uno studio esplorativo di fase 2 con un piano di monitoraggio della sicurezza (funzione renale, potassio, pressione arteriosa)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

