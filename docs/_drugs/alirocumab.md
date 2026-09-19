---
layout: default
title: Alirocumab
parent: Solo previsione del modello (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Relazione di valutazione farmaceutica

</div>

# ALIROCUMAB: Valutazione del Riutilizzo di Farmaci — In Attesa di Indicazioni Previste

## Riepilogo in una Frase

L'alirocumab (Praluent®) è un anticorpo monoclonale completamente umano che mira a PCSK9, originariamente sviluppato per il trattamento dell'ipercolesterolemia e la riduzione del rischio cardiovascolare. Il modello TxGNN **non ha ancora generato indicazioni nuove previste** per questo farmaco, e il dossier probatorio attualmente contiene **nessuna sperimentazione clinica** e **nessuna letteratura** da valutare. È necessaria un'ulteriore raccolta di dati prima che una valutazione del riutilizzo possa procedere.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originaria | Non elencata nel dossier probatorio attuale (nota: ipercolesterolemia, riduzione del rischio cardiovascolare) |
| Indicazione Nuova Prevista | — (Nessuna previsione TxGNN disponibile) |
| Punteggio di Previsione TxGNN | — |
| Livello di Evidenza | L5 (Nessuna previsione o studi di supporto) |
| Stato di Commercializzazione a Taiwan | ✗ Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | **Mantenere** |

---

## Perché Questa Previsione è Ragionevole?

Attualmente, il modello TxGNN non ha generato alcuna indicazione nuova prevista per l'alirocumab, quindi un'analisi di plausibilità meccanicistica non può essere condotta al momento.

Per riferimento, l'alirocumab è un inibitore di PCSK9 (proprotein convertase subtilisin/kexin type 9). PCSK9 normalmente si lega ai recettori LDL sulla superficie degli epatociti, promuovendo la loro degradazione e riducendo così la capacità del fegato di eliminare il colesterolo LDL dal sangue. Bloccando PCSK9, l'alirocumab aumenta il numero di recettori LDL disponibili, riducendo significativamente i livelli di LDL-C. Questo meccanismo è stato convalidato nello studio cardine ODYSSEY OUTCOMES che ha dimostrato la riduzione degli eventi cardiovascolari.

La via PCSK9 è stata implicata in aree al di là del metabolismo lipidico — compresa l'infiammazione, la sepsi, la rigenerazione epatica e l'infezione virale — suggerendo potenziali strategie di riutilizzo. Tuttavia, fino a quando le previsioni TxGNN non saranno generate, nessuna analisi formale di collegamento meccanicistico potrà essere condotta.

---

## Prove da Studi Clinici

Attualmente nessuna indicazione prevista da TxGNN è disponibile; pertanto, nessuna ricerca specifica per indicazione di studi clinici è stata condotta.

---

## Prove dalla Letteratura

Attualmente nessuna indicazione prevista da TxGNN è disponibile; pertanto, nessuna ricerca specifica per indicazione della letteratura è stata condotta.

---

## Informazioni sul Mercato di Taiwan

L'alirocumab **non è attualmente commercializzato a Taiwan**. Nessuna autorizzazione di commercializzazione TFDA è stata trovata (data della ricerca: 2026-03-29).

> Nota: L'alirocumab è approvato negli USA (FDA), nell'UE (EMA) e in molti altri mercati con il nome commerciale **Praluent®** (Sanofi / Regeneron) per l'ipercolesterolemia primaria, la dislipidemia mista e la malattia cardiovascolare aterosclerotica accertata per ridurre il rischio cardiovascolare.

---

## Considerazioni di Sicurezza

Nessun dato di sicurezza (avvertenze, controindicazioni o interazioni farmacologiche) è disponibile nel dossier probatorio attuale.

> Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza. Le considerazioni di sicurezza note principali per l'alirocumab dall'etichetta approvata includono:
> - **Reazioni di ipersensibilità** (incluse prurito, eruzione cutanea, orticaria; rari casi di vasculite da ipersensibilità)
> - **Reazioni nel sito di iniezione** (evento avverso più comune)
> - **Eventi neurocognitivi** (monitorati negli studi clinici; nessuna relazione causale confermata)
> - **Compromissione epatica** (nessun aggiustamento della dose necessario per lieve-moderata; dati limitati in grave)

---

## Conclusione e Prossimi Passi

**Decisione: Mantenere**

**Razionale:**
Il dossier probatorio per l'alirocumab è criticamente incompleto — nessuna indicazione nuova prevista da TxGNN è stata generata, nessuna autorizzazione di commercializzazione a Taiwan esiste, e i dati di sicurezza/meccanismo d'azione rimangono assenti. Senza un'indicazione nuova prevista, nessun percorso di valutazione del riutilizzo può essere avviato.

**Per procedere, quanto segue è necessario:**

1. **Esecuzione di Previsione TxGNN** — Eseguire il modello TxGNN per l'alirocumab (DB09302) per generare candidati di indicazioni di riutilizzo con punteggi di previsione
2. **Dati sul Meccanismo d'Azione (MOA)** — Interrogare l'API di DrugBank per recuperare i dati completi di MOA, target e via (Lacuna di Dati DG002)
3. **Foglio Illustrativo TFDA** — Ottenere e analizzare il foglio illustrativo ufficiale per avvertenze e controindicazioni (Lacuna di Dati DG001), o se non commercializzato a Taiwan, reperire da etichette approvate FDA/EMA
4. **Dati di Interazione Farmacologica** — Ri-interrogare i database di interazione farmacologica; l'alirocumab come anticorpo monoclonale ha interazioni mediate da CYP limitate, ma gli schemi di co-somministrazione con statine dovrebbero essere documentati
5. **Valutazione dell'Accesso al Mercato di Taiwan** — Se candidati di riutilizzo sono identificati, valutare il percorso per la registrazione TFDA o l'uso compassionevole

---

*Questo rapporto è stato generato il 2026-04-03 in base al dossier probatorio v4 (ID candidato: TW-DB09302-multi). I risultati sono solo per riferimento di ricerca e non costituiscono consulenza medica. I candidati di riutilizzo di farmaci richiedono una convalida clinica prima dell'applicazione.*

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

