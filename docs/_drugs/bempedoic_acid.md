---
layout: default
title: Bempedoic Acid
parent: Solo previsione del modello (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Acido bempedoico: dall'ipercolesterolemia a ipertiroidismo (predizione TxGNN di primo rango)

## Riepilogo in una frase

L'acido bempedoico è un inibitore dell'ATP-citrato liasi (ACLY) usato per abbassare il colesterolo LDL; nei dati compilati per questo report non è però riportata alcuna indicazione approvata in modo esplicito. Il modello TxGNN predice come prima indicazione l'**ipertiroidismo** (punteggio molto alto, ma **nessuno studio clinico e nessuna pubblicazione** a supporto). Tra le predizioni del modello, la più sostenuta dalla letteratura è l'**ipercolesterolemia familiare omozigote (HoFH)**, con 18 pubblicazioni, in gran parte rassegne.

## Quadro d'insieme

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (testi delle indicazioni autorizzate vuoti); l'uso noto è la riduzione del colesterolo LDL |
| Nuova indicazione predetta | Ipertiroidismo (rango 1) |
| Punteggio di predizione TxGNN | 99,61% |
| Livello di evidenza | L5 (solo predizione del modello) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 5 (tutte cancellate) |
| Decisione raccomandata | Hold |

Per contesto, la predizione più rilevante sul piano clinico è l'HoFH (rango 6, punteggio 99,48%, livello L4, indicazione "Research Question"), discussa di seguito.

## Perché questa predizione è ragionevole?

Per l'**ipertiroidismo** non emerge un collegamento meccanicistico plausibile. I dati dettagliati sul meccanismo d'azione non sono disponibili nel dossier, ma dalle conoscenze generali l'acido bempedoico è un profarmaco attivato nel fegato dall'enzima ACSVL1 che inibisce ACLY, a monte della HMG-CoA reduttasi nella sintesi del colesterolo. Non ha azioni note sulla sintesi o sulla secrezione degli ormoni tiroidei. L'alto punteggio TxGNN è quindi una predizione basata sul grafo di conoscenza, senza supporto clinico o bibliografico.

Lo stesso vale per le altre predizioni di vertice: resistenza agli ormoni tiroidei da mutazione di THRB, ipertiroxinemia, osteoporosi indotta da farmaci, osteoporosi associata a gravidanza e neoplasia endocrina multipla non hanno una base meccanicistica solida. "Malignant catarrh" e rinotracheite infettiva bovina sono malattie veterinarie, probabilmente artefatti del grafo (stesso punteggio identico). Per l'infezione da citomegalovirus esiste solo un'ipotesi teorica legata al metabolismo lipidico dell'ospite.

Fa eccezione l'**HoFH**: l'inibizione di ACLY riduce il colesterolo LDL, rilevante in questa malattia. Il limite è che l'effetto dipende dall'aumento dei recettori LDL, per cui l'efficacia potrebbe essere ridotta nei pazienti con varianti LDLR-null o gravemente difettive.

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati all'ipertiroidismo né alle altre indicazioni predette nei dati compilati.

## Evidenze dalla letteratura

Per l'ipertiroidismo: attualmente nessuna letteratura correlata disponibile.

Per l'HoFH (indicazione con evidenza più consistente), principali pubblicazioni:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Coorte | J Clin Lipidol | Valutazione real-world di efficacia e tollerabilità dell'acido bempedoico nell'HoFH (dati di esito non forniti) |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Rassegna | J Am Coll Cardiol | Terapie emergenti per ridurre LDL-C e apoB, incluso l'acido bempedoico |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Rassegna | J Atheroscler Thromb | Progressi nel trattamento dell'HoFH |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Rassegna | Exp Mol Pathol | Terapie innovative per la gestione dell'HoFH |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Rassegna | Cardiol Rev | Evinacumab e altre terapie ipolipemizzanti nell'HoFH |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Consenso di esperti | J Clin Lipidol | Aggiornamento NLA sull'ipercolesterolemia familiare |
| [42761917](https://pubmed.ncbi.nlm.nih.gov/42761917/) | 2026 | Rassegna | Methodist DeBakey Cardiovasc J | Panoramica sull'ipercolesterolemia familiare |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Rassegna | Am J Prev Cardiol | Importanza della riduzione prolungata dell'LDL-C nella prevenzione ASCVD |
| [29424317](https://pubmed.ncbi.nlm.nih.gov/29424317/) | 2019 | Rassegna | Curr Vasc Pharmacol | Meccanismi d'azione dei nuovi ipolipemizzanti |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Rassegna | Indian Heart J | Farmaci ipolipemizzanti non statinici tradizionali e nuovi |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 051828010 | NILEMDO 28 cpr rivestite 180 mg (FARMED Srl) | n.d. | Non disponibile (cancellata) |
| 048721029 | NILEMDO 28 cpr rivestite 180 mg (Daiichi Sankyo Europe GmbH) | n.d. | Non disponibile (cancellata) |
| 051564019 | NILEMDO 28 cpr rivestite 180 mg (GMM Farma Srl) | n.d. | Non disponibile (cancellata) |
| 051658019 | NUSTENDI 28 cpr rivestite 180 mg + 10 mg (GMM Farma Srl) | n.d. | Non disponibile (cancellata) |
| 048668026 | NUSTENDI 28 cpr rivestite 180 mg + 10 mg (Daiichi Sankyo Europe GmbH) | n.d. | Non disponibile (cancellata) |

Tutte e cinque le autorizzazioni risultano cancellate; non ci sono autorizzazioni valide.

## Considerazioni sulla sicurezza

**Interazioni farmacologiche** (23 segnalate; elenco dei principali):

- **Gravità maggiore**: corticosteroidi (idrocortisone, triamcinolone, desametasone, betametasone, budesonide, prednisolone, prednisone, metilprednisolone, deflazacort, fludrocortisone), levofloxacina, simvastatina.
- **Gravità moderata**: empagliflozin, gliburide, repaglinide, rifaximina, rosuvastatina, selexipag, fexofenadina, revefenacin.

Per avvertenze e controindicazioni si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione principale (ipertiroidismo) non ha alcuna evidenza clinica né bibliografica né un razionale meccanicistico (livello L5). L'unica direzione biologicamente plausibile, l'HoFH, è sostenuta soprattutto da rassegne e da una coorte real-world senza dati di esito disponibili, e va trattata come domanda di ricerca.

**Per procedere sono necessari:**
- Recupero dei fogli illustrativi AIFA (avvertenze, controindicazioni, indicazioni autorizzate), dato che le autorizzazioni sono tutte cancellate e va chiarita la ragione
- Dati sul meccanismo d'azione da DrugBank
- Analisi dei risultati della coorte real-world nell'HoFH (PMID 41274797) e valutazione dell'efficacia per genotipo (LDLR-null o meno)
- Revisione della plausibilità biologica delle predizioni di rango elevato prima di qualsiasi ulteriore studio
- Piano di gestione delle interazioni, in particolare con statine (simvastatina) e corticosteroidi
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

