---
layout: default
title: Alirocumab
parent: Solo previsione del modello (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alirocumab: nuova indicazione prevista, Ittiosi X-linked senza deficit di steroide solfatasi (livello di evidenza L5). Indicazione originale: Dislipidemia sindromica, aterosclerosi, arteriosclerosi…"
monitor_inn: "ALIROCUMAB"
predicted_indications: ["ichthyosis, X-linked, without steroid sulfatase deficiency", "disorder of other vitamins and cofactors metabolism and transport", "xanthomatosis (disease)", "46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect", "cholesterol catabolic process disease", "46,XY disorder of sex development due to a cholesterol synthesis defect", "dappled diaphyseal dysplasia", "neutral lipid storage disease", "3-hydroxyacyl-CoA dehydrogenase deficiency", "spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder"]
---

# Alirocumab
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

# Alirocumab: Dall'ipercolesterolemia/aterosclerosi a Ittiosi X-linked senza deficit di steroide solfatasi

## Sintesi

Alirocumab è un anticorpo monoclonale anti-PCSK9, originariamente utilizzato per le dislipidemie e le malattie aterosclerotiche (dislipidemia sindromica, aterosclerosi, arteriosclerosi, arteriolosclerosi).
Il modello TxGNN predice una possibile efficacia per l'**ittiosi X-linked senza deficit di steroide solfatasi**, ma per questa indicazione non risultano **né studi clinici né pubblicazioni** a supporto: la predizione si basa solo sul modello (livello di evidenza L5).

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Dislipidemia sindromica, aterosclerosi, arteriosclerosi, arteriolosclerosi (dal grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione predetta | Ittiosi X-linked senza deficit di steroide solfatasi |
| Punteggio di predizione TxGNN | 99,43% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 5 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. È noto tuttavia che alirocumab è un anticorpo che inibisce PCSK9 (proproteina convertasi subtilisina/kexina di tipo 9), aumentando la disponibilità dei recettori LDL e la clearance del colesterolo LDL.

Per l'ittiosi X-linked, **non è stato identificato un legame meccanicistico plausibile**. Questa malattia comporta l'accumulo di colesterolo solfato nella cute, un processo su cui l'inibizione di PCSK9 non ha un effetto stabilito. Nonostante il punteggio elevato, l'assenza di studi e di letteratura indica che la predizione sembra un artefatto del grafo di conoscenza.

Va inoltre segnalato che, tra le altre predizioni del modello, il **xantomatosi** è biologicamente plausibile (la riduzione del LDL-C potrebbe ridurre il carico xantomatoso, con evidenza solo indiretta da due case report) e la **malattia del catabolismo del colesterolo** si sovrappone alle indicazioni lipidiche già approvate, quindi rappresenta più una riformulazione dell'uso esistente che un vero riposizionamento. Entrambe sono candidate più sensate rispetto a quella di rango 1.

---

## Evidenza da studi clinici

Attualmente non risultano studi clinici correlati registrati per questa indicazione.

---

## Evidenza dalla letteratura

Attualmente non risulta letteratura correlata disponibile per questa indicazione.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 044500027 | PRALUENT, 2 penne preriempite SC 1 ml 75 mg | – | Non disponibile (autorizzazione cancellata) |
| 044500078 | PRALUENT, 1 penna preriempita SC 1 ml 150 mg | – | Non disponibile (autorizzazione cancellata) |
| 044500015 | PRALUENT, 1 penna preriempita SC 1 ml 75 mg | – | Non disponibile (autorizzazione cancellata) |
| 044500080 | PRALUENT, 2 penne preriempite SC 150 mg 1 ml | – | Non disponibile (autorizzazione cancellata) |
| 044500193 | PRALUENT, 1 penna preriempita SC 2 ml 300 mg (150 mg/ml) | – | Non disponibile (autorizzazione cancellata) |

Titolare: Sanofi Winthrop Industrie. Tutte e 5 le autorizzazioni risultano cancellate, nessuna è attualmente valida.

---

## Considerazioni di sicurezza

- **Interazioni**: l'interrogazione ha rilevato una sola voce, di natura farmacologica e non una vera interazione tra farmaci: il bersaglio di alirocumab, PCSK9 (proproteina convertasi subtilisina/kexina di tipo 9). Alirocumab è stato approvato dalla FDA nel luglio 2015 come primo agente anti-PCSK9 per l'ipercolesterolemia familiare eterozigote o la malattia cardiovascolare aterosclerotica clinica non adeguatamente controllate con dieta e statine; l'approvazione EMA è seguita pochi mesi dopo.
- **Sicurezza generale**: un'analisi aggregata dello studio ODYSSEY OUTCOMES (47.296 anni-paziente di osservazione controllata con placebo, PMID 38658193) ha descritto il profilo di sicurezza di alirocumab nella popolazione cardiovascolare.

Per le avvertenze e le controindicazioni ufficiali, consultare il foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per l'ittiosi X-linked non esistono studi clinici né letteratura, e non è stato identificato un legame meccanicistico con l'inibizione di PCSK9: l'elevato punteggio TxGNN (99,43%) appare un artefatto del modello. Inoltre, in Italia tutte le autorizzazioni sono attualmente cancellate.

**Per procedere sarebbe necessario:**
- Acquisire il foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Ottenere i dati sul meccanismo d'azione (MOA) da DrugBank
- Verificare le ragioni della cancellazione delle autorizzazioni italiane e la disponibilità effettiva del prodotto
- Valutare in alternativa candidati più plausibili, come la xantomatosi (rango 3), previa raccolta di evidenza clinica diretta
- Stabilire preliminarmente un'ipotesi biologica per l'ittiosi X-linked prima di qualsiasi studio preclinico
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

