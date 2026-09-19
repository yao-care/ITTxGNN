---
layout: default
title: Imatinib
parent: Solo previsione del modello (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Imatinib
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

# Imatinib: Dalla LMC e GIST al Fibrosarcoma Cardiaco

## Riepilogo in una frase

Imatinib (Gleevec/Glivec) è un inibitore della tirosin-chinasi originariamente sviluppato per la Leucemia Mieloide Cronica (LMC) e i Tumori Stromali Gastrointestinali (GIST), che colpisce le chinasi BCR-ABL, c-KIT e PDGFR.
Il modello TxGNN predice che potrebbe essere efficace per il **Fibrosarcoma Cardiaco**,
con **0 studi clinici** e **1 pubblicazione** attualmente identificati per questa indicazione — rappresentando una previsione solo del modello con prove dirette minime.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Leucemia Mieloide Cronica (LMC) e Tumori Stromali Gastrointestinali (GIST) |
| Nuova indicazione prevista | Fibrosarcoma Cardiaco |
| Punteggio di previsione TxGNN | 99.94% |
| Livello di evidenza | L5 |
| Stato del mercato Taiwan | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospendere |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili nel set di dati fornito. Sulla base della letteratura pubblicata consolidata, imatinib è un inibitore di piccole molecole della tirosin-chinasi che blocca competitivamente tre chinasi oncogeniche chiave: BCR-ABL (la proteina di fusione che guida la LMC), c-KIT (mutata costitutivamente nel GIST e in altri sarcomi), e PDGFR-α/β (sovraattivato in tumori fibroblastici come il dermatofibrosarcoma protuberans). Il suo successo di riferimento nella LMC e nel GIST ha stabilito il paradigma della terapia mirata molecolarmente, e la sua attività di blocco di PDGFR è stata successivamente applicata in più tipi di tumori fibroblastici e mesenchimali.

Il fibrosarcoma cardiaco è una neoplasia primaria del cuore estremamente rara, con meno di 100 casi documentati in tutta la letteratura pubblicata. Perché imatinib sia rilevante dal punto di vista meccanicistico qui, le cellule tumorali dovrebbero presentare mutazioni attivanti o sovraespressione di BCR-ABL, c-KIT o PDGFR — nessuno dei quali è stato segnalato nel fibrosarcoma cardiaco fino ad oggi. La razionalità teorica rimane plausibile in linea di principio, data l'attività nota di imatinib contro i tumori fibroblastici guidati dal percorso PDGF, ma è interamente non supportata da dati clinici o preclinici diretti per questo sito tumorale specifico.

Il punteggio di previsione TxGNN del 99.94% riflette la similarità della rete di grafici nella rete di conoscenza droga-malattia, non l'efficacia clinica. Poiché il fibrosarcoma cardiaco è così raro che genera quasi nessun segnale letterario, la previsione del modello non può essere validata indipendentemente in questa fase. Questo è un output generatore di ipotesi, non una raccomandazione basata su prove.

---

## Evidenza degli studi clinici

Attualmente nessuna prova clinica correlata registrata.

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|------|------|---------|----------------------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Editoriale / Commento | Prescrire International | Rassegna narrativa delle indicazioni in espansione di imatinib oltre la LMC, includendo LLA Ph+ e altri tumori ematologici/solidi; discute la mancanza di prove robuste per molti nuovi usi. Non affronta il fibrosarcoma cardiaco — recuperato a causa della rassegna ampia dell'indicazione di imatinib. |

---

## Citotossicità

| Elemento | Contenuto |
|----------|-----------|
| Classificazione della citotossicità | Terapia mirata (Inibitore della tirosin-chinasi — inibitore di BCR-ABL / c-KIT / PDGFR-α/β) |
| Rischio di mielosoppressione | Moderato — neutropenia, trombocitopenia e anemia sono frequentemente segnalate; la gravità è generalmente inferiore alla chemioterapia citotossica convenzionale |
| Classificazione dell'emetogenicità | Bassa a moderata (somministrazione per via orale; la nausea è comune ma di solito gestibile) |
| Elementi di monitoraggio | Emocromo completo (CBC con differenziale), test di funzionalità epatica (ALT, AST, bilirubina), funzionalità renale (creatinina sierica), valutazione della ritenzione di liquidi / edema periferico, peso corporeo |
| Protezione nella manipolazione | Si applicano precauzioni standard per la manipolazione di farmaci citotossici; nessun contenimento speciale oltre i protocolli standard di TKI per via orale |

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.

---

## Conclusione e passi successivi

**Decisione: Sospendere**

**Razionale:**
Il fibrosarcoma cardiaco è un tumore estremamente raro senza alterazioni documentate di BCR-ABL, c-KIT o PDGFR, e l'unica pubblicazione identificata è un editoriale generale che non affronta questa indicazione. Non esistono studi clinici e la plausibilità biologica rimane non verificata. Procedere sarebbe prematuro senza dati patologici molecolari fondamentali.

**Per procedere, è necessario quanto segue:**
- Patologia molecolare del tessuto del fibrosarcoma cardiaco: profilo IHC o NGS per l'espressione di PDGFR-α/β, mutazione c-KIT o altre alterazioni di chinasi sensibili a imatinib
- Creazione di modelli preclinici (linee cellulari o xenotrapianti derivati da pazienti) specifici per il fibrosarcoma cardiaco
- Recupero dei dati del meccanismo d'azione da DrugBank (lacuna di dati DG002) per documentare formalmente la plausibilità biologica
- Foglio illustrativo Taiwan (TFDA) e dati di sicurezza (lacuna di dati DG001) per abilitare la valutazione completa della sicurezza S1 prima di qualsiasi considerazione clinica

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

