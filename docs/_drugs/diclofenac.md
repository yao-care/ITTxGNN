---
layout: default
title: Diclofenac
parent: Solo previsione del modello (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Diclofenac: nuova indicazione prevista, Ipotricosi semplice del cuoio capelluto (livello di evidenza L5). Indicazione originale: Testo di indicazione autorizzata non disponibile nei dati compilati.…"
monitor_inn: "DICLOFENAC"
predicted_indications: ["hypotrichosis simplex of the scalp", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "brachyolmia", "brachyolmia-amelogenesis imperfecta syndrome", "congenital hypotrichosis milia", "myosclerosis", "diffuse alopecia areata", "juvenile idiopathic arthritis", "WHIM syndrome"]
---

# Diclofenac
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

## Diclofenac: dai disturbi reumatici e dermatologici all'ipotricosi semplice del cuoio capelluto
{: .text-alpha }

## Sintesi in una frase

Il diclofenac è un antinfiammatorio non steroideo (FANS) usato per artrite reumatoide, osteoartrosi, spondilite anchilosante e alcune patologie cutanee come la cheratosi attinica. Il modello TxGNN lo propone per l'**ipotricosi semplice del cuoio capelluto** con un punteggio molto alto, ma **non esistono studi clinici né pubblicazioni** a sostegno di questa direzione: è una previsione puramente computazionale.

---

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Testo di indicazione autorizzata non disponibile nei dati compilati. Dal grafo di conoscenza: artrite reumatoide, osteoartrosi, spondilite anchilosante, cheratosi attinica |
| Nuova indicazione prevista | Ipotricosi semplice del cuoio capelluto |
| Punteggio di predizione TxGNN | 99,69% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è (poco) plausibile

I dati compilati non riportano il meccanismo d'azione dettagliato. È noto che il diclofenac è un inibitore delle ciclossigenasi COX-1 e COX-2, e che riduce la sintesi di prostaglandine con effetto antinfiammatorio e analgesico.

L'ipotricosi semplice è invece un disturbo genetico della crescita dei capelli, associato a varianti in geni come CDSN, APCDD1 e RPL21. L'inibizione delle COX non agisce su questi difetti di base e non è stato identificato alcun legame meccanicistico credibile.

L'alto punteggio TxGNN riflette probabilmente la vicinanza nel grafo di conoscenza con le indicazioni dermatologiche del farmaco, come la cheratosi attinica, e non una reale base biologica. Un'ipotesi indiretta, ancora priva di supporto, riguarda il ruolo delle prostaglandine nel ciclo del capello (la PGD2 inibisce la crescita), ma resta puramente teorica.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate, nessuna è attualmente valida. Il testo dell'indicazione approvata e la forma farmaceutica non sono disponibili nei dati compilati. Principali autorizzazioni:

| N. autorizzazione | Prodotto | Titolare |
|---------|------|------|
| 038049045 | EMINOCS, soluzione orale 100 ml 50 mg/ml | Dymalife Pharmaceutical Srl |
| 035248018 | Diclofenac, 5 fiale IM 75 mg 3 ml | DOC Generici Srl |
| 028945020 | VOLTFAST, 30 compresse rivestite 50 mg | Novartis Farma SpA |
| 029456011 | Diclofenac, 30 compresse gastroresistenti 50 mg | EG SpA |
| 045242070 | SOLACUTAN, gel 90 g 3% | Mibe Pharma Italia Srl |

---

## Considerazioni di sicurezza

Le avvertenze e le controindicazioni tratte dal foglio illustrativo non sono disponibili. Per la sicurezza si rimanda al foglio illustrativo.

- **Condizioni associate a controindicazione nel grafo di conoscenza** (non dal testo del foglio illustrativo): ipertensione, insufficienza cardiaca congestizia, infarto del miocardio e altre malattie cardiovascolari, ictus e malattie cerebrovascolari, ulcera peptica (anche attiva), malattia infiammatoria intestinale, insufficienza epatica, malattie epatiche e danno epatico da farmaci, asma, diabete mellito e chetoacidosi diabetica, disturbi della coagulazione, anemia ed emoglobinopatie, malattie della colecisti, cheratite, abuso o dipendenza da sostanze.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni in totale. Tra quelle mostrate, di gravità moderata: acido acetilsalicilico, corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), metformina e altri antidiabetici (glimepiride, glipizide, clorpropamide, acetoesamide, exenatide), mesalazina, balsalazide, aprepitant, fenfluramina e destrofenfluramina. Di gravità minore: famotidina, ranitidina, cimetidina.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- La previsione per l'ipotricosi semplice del cuoio capelluto non ha alcun supporto clinico o bibliografico (L5) e nessun meccanismo plausibile.
- Tutte le autorizzazioni italiane sono cancellate e i dati di sicurezza del foglio illustrativo sono mancanti.

**Per procedere sarebbe necessario:**
- Acquisire il foglio illustrativo AIFA con avvertenze e controindicazioni.
- Reperire i dati di meccanismo d'azione da DrugBank.
- Disporre di dati preclinici che colleghino l'inibizione delle COX alla biologia del follicolo pilifero.

**Nota su un'altra previsione:** tra le previsioni valutate, l'**artrite idiopatica giovanile** (punteggio 99,25%) è l'unica con una letteratura di qualche rilievo (livello L3). Comprende piccoli studi clinici datati, come uno studio crossover del 1988 che confronta diclofenac, naprossene e tolmetina, e alcune revisioni. Si tratta però di un'estensione naturale dell'uso dei FANS nelle artriti già note, più che di un vero riposizionamento. Se lo si volesse approfondire, andrebbe verificato lo stato di mercato per le formulazioni e la regione rilevanti.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

