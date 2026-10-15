---
layout: default
title: Tetracycline
parent: Prove moderate (L3-L4)
nav_order: 432
evidence_level: L4
indication_count: 4
---

# Tetracycline
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

# Tetraciclina: dall'uso in infezioni batteriche alla cheratocongiuntivite epiteliale puntata

## Sintesi in una frase

La tetraciclina è un antibiotico ad ampio spettro, originariamente usato per infezioni delle vie urinarie, bronchite, acne, gonorrea, congiuntivite e polmonite, tra le altre.
Il modello TxGNN prevede che possa essere utile per la **cheratocongiuntivite epiteliale puntata**, ma a sostegno di questa direzione c'è solo **1 pubblicazione** (un case report indiretto) e **nessuno studio clinico registrato**.
L'evidenza è quindi molto limitata e il punteggio elevato riflette soprattutto la vicinanza a indicazioni già note.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni delle vie urinarie, bronchite, acne, antrace, gonorrea, faringite, congiuntivite, polmonite e altre infezioni batteriche (dalle indicazioni del grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Cheratocongiuntivite epiteliale puntata |
| Punteggio di predizione TxGNN | 99,58% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 1 (revocata) |
| Decisione raccomandata | Hold (sospendere) |

---

## Perché questa predizione è plausibile?

I dati compilati per questo report non includono una descrizione dettagliata del meccanismo d'azione. In base alle informazioni note, la tetraciclina appartiene alla classe delle tetracicline, la cui efficacia nelle infezioni oculari da clamidia (tracoma e congiuntivite da inclusione) è consolidata, e meccanicamente potrebbe essere applicabile alle patologie della superficie oculare. Le tetracicline hanno inoltre proprietà antinfiammatorie e di inibizione delle metalloproteinasi della matrice (MMP), che potrebbero giovare all'infiammazione della superficie oculare.

Il legame tra indicazione originale e nuova è soprattutto di prossimità: la cheratite epiteliale puntata può comparire dopo una congiuntivite da clamidia. L'unico articolo recuperato (PMID 1424659) descrive però una cheratite persistente comparsa *dopo* la risoluzione della congiuntivite trattata con tetraciclina o doxiciclina. Non dimostra quindi un beneficio della tetraciclina sulla cheratite. Il punteggio elevato riflette probabilmente la vicinanza all'indicazione già esistente di congiuntivite, più che nuove prove.

Altre predizioni nello stesso elenco (per completezza):
- **Rinosinusite cronica** (punteggio 99,15%, livello L4): la più supportata da letteratura, ma riguarda soprattutto doxiciclina e omadacicline, non la tetraciclina. È formulabile come domanda di ricerca a livello di classe.
- **Sinusite etmoidale cronica** (99,15%, L4): solo uno studio di sensibilità antibiotica in vitro.
- **Neoplasia dei seni paranasali** (99,10%, L5): nessuna evidenza, solo predizione del modello.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Due casi di congiuntivite follicolare da *Chlamydia trachomatis*, trattati con tetraciclina o doxiciclina orale con risoluzione dei follicoli, seguiti da cheratite epiteliale puntata ricorrente e bilaterale. Evidenza indiretta: non mostra beneficio della tetraciclina sulla cheratite |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 041527019 | PYLERA*120 cps 140 mg + 125 mg + 125 mg flacone (LAB. JUVISE' PHARMACEUTICALS) | Non indicata | Non indicata (autorizzazione revocata) |

---

## Considerazioni sulla sicurezza

Non sono disponibili avvertenze o controindicazioni tratte dal foglio illustrativo; si rimanda al foglio illustrativo per le informazioni di sicurezza.

- **Controindicazioni/condizioni a rischio (dal grafo di conoscenza, non dal testo dell'etichetta)**: insufficienza epatica e malattie epatiche, malattie renali, insufficienza renale, uremia, glomerulonefrite, epilessia, neutropenia, agranulocitosi, deficit di G6PD, neuropatia periferica, colite da *Clostridium difficile*, diabete e chetoacidosi diabetica, fibrillazione atriale, blocco atrioventricolare, gotta, disturbi della coagulazione, insufficienza respiratoria e altre condizioni.
- **Interazioni farmacologiche**: sono state identificate 308 interazioni. Tra quelle di livello **maggiore** figurano isotretinoina, acitretina e acido aminolevulinico. Tra quelle di livello **moderato**: etinilestradiolo, amoxicillina, ampicillina, sali di bismuto, idrossido di alluminio, aminofillina, atovaquone, balsalazide, atracurio, citrato di sodio e asparaginasi. Tra quelle di livello **minore**: acetazolamide, idroclorotiazide e amiloride.

---

## Conclusioni e prossimi passi

**Decisione: Hold (sospendere)**

**Motivazione:**
Per la cheratocongiuntivite epiteliale puntata non esistono studi clinici e l'unica pubblicazione è un case report indiretto. Inoltre la tetraciclina ha in Italia solo un'autorizzazione revocata. Il punteggio TxGNN elevato non basta a giustificare un avanzamento.

**Per procedere, sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Studi clinici o evidenze dirette sull'uso della tetraciclina (o di un comparatore di classe come la doxiciclina) nelle patologie della superficie oculare
- Valutazione della compatibilità della via di somministrazione (ad es. formulazione oftalmica) e della disponibilità di prodotti sul mercato italiano
- In alternativa, valutare la rinosinusite cronica come domanda di ricerca a livello di classe, con la doxiciclina come comparatore pratico
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

