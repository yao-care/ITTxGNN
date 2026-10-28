---
layout: default
title: Simoctocog Alfa
parent: Solo previsione del modello (L5)
nav_order: 404
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Simoctocog Alfa: nuova indicazione prevista, Pseudo-malattia di von Willebrand (livello di evidenza L5). Indicazione originale: Emofilia (incluso il quadro sintomatico dell'emofilia nelle donne por…"
monitor_inn: "SIMOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "thrombotic thrombocytopenic purpura"]
---

# Simoctocog Alfa
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Simoctocog alfa: dall'emofilia alla pseudo-malattia di von Willebrand
{: .text-alpha }

## Sintesi in una frase

Simoctocog alfa è un fattore VIII della coagulazione ricombinante umano (con delezione del dominio B), usato originariamente per il trattamento dell'emofilia.
Il modello TxGNN ne prevede una possibile efficacia nella **pseudo-malattia di von Willebrand**, ma al momento **non sono presenti sperimentazioni cliniche né pubblicazioni** a sostegno di questa ipotesi: la previsione si basa solo sul modello.

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Emofilia (incluso il quadro sintomatico dell'emofilia nelle donne portatrici) |
| Nuova indicazione prevista | Pseudo-malattia di von Willebrand |
| Punteggio di previsione TxGNN | 1,0000 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 7 su 7) |
| Numero di autorizzazioni | 7 (valide: 7) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Simoctocog alfa è un fattore VIII ricombinante con delezione del dominio B, che sostituisce l'attività del FVIII carente. I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione, ma la funzione di sostituzione del FVIII è quella nota per questa classe di farmaci.

Il legame con la nuova indicazione è però debole. La pseudo-malattia di von Willebrand (tipo piastrinico) è causata da un difetto di guadagno di funzione della glicoproteina piastrinica GPIbα, che aumenta il legame con il fattore di von Willebrand (VWF). Ne derivano perdita dei multimeri VWF ad alto peso molecolare e trombocitopenia. Il difetto primario riguarda l'interazione piastrine/VWF e non la carenza di FVIII; la sostituzione di FVIII ha quindi solo un razionale indiretto (è possibile una riduzione secondaria di FVIII).

Il punteggio proviene dal modello TxGNN (deep learning) e può riflettere similarità apprese dal modello tra malattie correlate, non prove biologiche.

### Altre indicazioni previste (valutazione sintetica)

| Rango | Malattia prevista | Punteggio TxGNN | Livello | Plausibilità meccanicistica |
|---|---|---|---|---|
| 2 | Disturbo da difetto di rilascio piastrinico | 1,0000 | L5 | Non supportata: il difetto è piastrinico intrinseco |
| 3 | Trombastenia di Glanzmann | 1,0000 | L5 | Nessun ruolo chiaro: fattori della coagulazione normali; trattamenti standard piastrine e rFVIIa |
| 4 | Sindrome di Scott | 0,9997 | L5 | Speculativa: il FVIII è cofattore del complesso tenasi, ma manca la superficie fosfolipidica |
| 5 | Carenza acquisita di fattori della coagulazione | 0,9995 | L5 | La più plausibile (es. emofilia A acquisita), ma gli autoanticorpi inibitori spesso rendono inefficace la sostituzione |
| 6 | Diatesi emorragica da difetto del recettore del collagene | 0,9992 | L5 | Nessun razionale diretto: patologia piastrinica |
| 7 | Disturbo emorragico da trombocitopenia costituzionale | 0,9992 | L5 | Non supportata: il fattore limitante è la piastrina |
| 8 | Trombocitopenia alloimmune fetale e neonatale | 0,9984 | L5 | Nessun ruolo meccanicistico: processo immunitario |
| 10 | Porpora trombotica trombocitopenica | 0,9972 | L5 | Non supportata; possibile preoccupazione di sicurezza (stato protrombotico) |

## Evidenza da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

Tutte le 7 autorizzazioni (titolare: Octapharma AB, prodotto NUWIQ) risultano cancellate. Il testo dell'indicazione approvata non è disponibile.

| Numero di autorizzazione | Nome del prodotto | Stato |
|---------|------|------|
| 043534080 | NUWIQ 1.500 UI + siringa solvente 2,5 ml + accessori | Valida |
| 043534066 | NUWIQ 3.000 UI + siringa solvente 2,5 ml + accessori | Valida |
| 043534054 | NUWIQ 2.500 UI + siringa solvente 2,5 ml + accessori | Valida |
| 043534041 | NUWIQ 2.000 UI + siringa solvente 2,5 ml | Valida |
| 043534039 | NUWIQ 1.000 UI + siringa solvente 2,5 ml | Valida |

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Nei dati compilati non risultano interazioni farmacologiche né controindicazioni derivate dal grafo di conoscenza. Per la porpora trombotica trombocitopenica, la sostituzione di FVIII potrebbe teoricamente aggravare lo stato protrombotico.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la pseudo-malattia di von Willebrand non ha alcun supporto clinico o bibliografico (L5) e il meccanismo (difetto piastrinico/VWF) non è corretto dalla sostituzione di FVIII. Inoltre il prodotto non ha attualmente autorizzazioni valide in Italia.

**Per procedere sarebbe necessario:**
- Recuperare il foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante e bloccante per la valutazione di sicurezza
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Valutare in via prioritaria le indicazioni più plausibili, in particolare la carenza acquisita di fattori della coagulazione (emofilia A acquisita), con una revisione della letteratura sul ruolo del FVIII sostitutivo in presenza di inibitori
- Chiarire la disponibilità commerciale del prodotto (autorizzazioni cancellate) o individuare formulazioni alternative di FVIII ricombinante
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

