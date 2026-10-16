---
layout: default
title: Captopril
parent: Solo previsione del modello (L5)
nav_order: 88
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Captopril: nuova indicazione prevista, Malattia renale ipertensiva maligna (livello di evidenza L5). Indicazione originale: Ipertensione, disturbo ipertensivo…"
---

# Captopril
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

# Captopril: dall'ipertensione alla malattia renale ipertensiva maligna

## Riepilogo in breve

Il captopril è un inibitore dell'enzima di conversione dell'angiotensina (ACE), utilizzato originariamente per ipertensione e nefropatia diabetica.
Il modello TxGNN ne prevede l'efficacia nella **malattia renale ipertensiva maligna**, con punteggio molto alto.
A supporto, però, non c'è nessuno **studio clinico** e c'è **1 sola pubblicazione**, un caso diagnostico che non fornisce prove terapeutiche.

## Quadro d'insieme

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, disturbo ipertensivo, nefropatia diabetica (da indicazioni del grafo di conoscenza; il testo autorizzato AIFA non è disponibile) |
| Nuova indicazione prevista | Malattia renale ipertensiva maligna |
| Punteggio di predizione TxGNN | 99,28% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 4 (tutte cancellate) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati per questo report. In base alle conoscenze generali, il captopril appartiene alla classe degli inibitori dell'ACE: riduce l'angiotensina II e quindi la pressione arteriosa, ed è consolidato nell'ipertensione e nella nefropatia diabetica.

La malattia renale ipertensiva maligna è guidata da una forte attivazione del sistema renina-angiotensina-aldosterone, quindi il meccanismo è plausibile. Va però osservato che si tratta di fatto di un'estensione dell'indicazione ipertensiva già esistente, e non di un riposizionamento realmente nuovo.

Il punteggio TxGNN elevato resta una predizione computazionale e non sostituisce prove cliniche.

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Caso clinico | Clinical Nuclear Medicine | Renografia con captopril positiva senza stenosi dell'arteria renale, dovuta a un carcinoma a cellule renali; l'ipertensione renina-dipendente si è risolta dopo nefrectomia. Valore diagnostico, non terapeutico |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 035036161 | CAPTOPRIL*24 cpr 50 mg (EG SpA) | Non indicata | Non indicata (cancellata) |
| 035317561 | CAPTOPRIL*24 cpr 50 mg (MYLAN SpA) | Non indicata | Non indicata (cancellata) |
| 035317559 | CAPTOPRIL*50 cpr 25 mg (MYLAN SpA) | Non indicata | Non indicata (cancellata) |
| 035036159 | CAPTOPRIL*50 cpr 25 mg (EG SpA) | Non indicata | Non indicata (cancellata) |

## Considerazioni sulla sicurezza

Le informazioni del foglio illustrativo AIFA non sono disponibili nei dati compilati. Ciò impedisce di proseguire con la valutazione di sicurezza.

- **Controindicazioni dal grafo di conoscenza** (non da testo di etichetta): angioedema (anche ereditario, acquisito e indotto da bloccanti del sistema RAAS), malattie renali, malattie epatiche ed encefalopatia epatica, pancreatite, malattie della colecisti, lupus eritematoso sistemico, malattie del tessuto connettivo, deficit di potassio, diabete mellito e chetoacidosi diabetica, neutropenia e agranulocitosi, stenosi aortica e valvulopatie aortiche, ipotensione, iperparatiroidismo e osteite fibrosa, malattie ossee.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni; tra quelle mostrate, la maggior parte è di livello moderato, ad esempio con corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), antidiabetici (metformina, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, clorpropamide, acetoesamide), bupropione, morfina, acido acetilsalicilico e dronabinolo. Antiacidi come idrossido di alluminio e carbonato di calcio hanno interazione minore.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il punteggio del modello è alto, ma non esistono studi clinici né evidenze terapeutiche dirette; l'unica pubblicazione è un caso diagnostico. Inoltre tutte le autorizzazioni italiane sono cancellate e i dati di sicurezza del foglio illustrativo mancano.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni (lacuna bloccante)
- Dati sul meccanismo d'azione da DrugBank
- Letteratura clinica terapeutica diretta sul captopril nella malattia renale ipertensiva maligna
- Chiarire se l'indicazione sia già coperta dall'uso ipertensivo consolidato, e verificare la situazione regolatoria, dato che le autorizzazioni sono cancellate

---

### Nota sulle altre indicazioni previste

Sono emerse altre tre indicazioni, con evidenza ancora più debole:

- **Ipertensione nefrovascolare maligna** (punteggio 99,28%, livello L4, "domanda di ricerca"): coerente dal punto di vista meccanicistico, ma le pubblicazioni sono per lo più aneddotiche o diagnostiche (renografia). Cautela: gli ACE-inibitori possono peggiorare la funzione renale in caso di stenosi bilaterale dell'arteria renale o di rene unico stenotico.
- **Ipertensione polmonare da malattia polmonare e/o ipossia** (99,15%, L5, Hold): la letteratura recuperata è in gran parte non pertinente; i vasodilatatori sistemici possono peggiorare il rapporto ventilazione-perfusione.
- **Ipertensione polmonare a meccanismo multifattoriale poco chiaro** (99,15%, L5, Hold): nessuno studio né pubblicazione disponibile.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

