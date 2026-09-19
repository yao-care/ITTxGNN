---
layout: default
title: Valsartan
parent: Prove moderate (L3-L4)
nav_order: 210
evidence_level: L4
indication_count: 7
---

# Valsartan
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **7** 
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

# Valsartan: dall'Ipertensione alla Malattia Renale da Ipertensione Maligna

---

## Sintesi in una frase

Valsartan è un bloccante del recettore dell'angiotensina II (ARB) consolidato per il trattamento dell'ipertensione e dell'insufficienza cardiaca mediante il blocco selettivo del recettore AT1.
Il modello TxGNN prevede che potrebbe essere efficace per la **Malignant Hypertensive Renal Disease**, con un punteggio di predizione del **99.97%**.
Le prove attuali a supporto di questa direzione si limitano a **1 studio meccanicistico preclinico** e **nessuna prova clinica registrata** specifica per questa indicazione.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originaria | Ipertensione / Insufficienza cardiaca (classe ARB; nessun dato di registrazione TFDA di Taiwan acquisito in questo dataset) |
| Indicazione Predetta Nuova | Malignant Hypertensive Renal Disease |
| Punteggio Predizione TxGNN | 99.97% |
| Livello di Evidenza | L4 |
| Stato del Mercato Taiwan | Non Commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In Sospeso |

---

## Perché questa Predizione è Ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili dalla fonte dati. Sulla base della conoscenza farmacologica consolidata, valsartan appartiene alla classe dei bloccanti del recettore dell'angiotensina II (ARB). Blocca selettivamente il sottotipo di recettore AT1, prevenendo all'angiotensina II (Ang II) di esercitare i suoi effetti vasocostrittivi, pro-fibrotici e pro-infiammatori. Nel rene, questo si traduce in una riduzione della pressione intraglomerulare, diminuzione della proteinuria e soppressione della fibrosi renale mediata da TGF-β — gli stessi percorsi che guidano il danno d'organo nelle emergenze ipertensive.

La malattia renale da ipertensione maligna (nefroangiosclerosi maligna) si sviluppa quando una pressione sanguigna gravemente elevata causa danno renale acuto nefrotossico, caratterizzato da necrosi fibrinoide delle arteriole, microangiopatia trombotica e deterioramento rapido della funzione renale. Il driver patologico centrale è l'iperattivazione dell'Ang II attraverso il sistema renina-angiotensina-aldosterone (RAAS), che porta a stimolazione sostenuta di AT1R e a un ciclo autoamplificante di vasocostrizione e danno glomerulare. Valsartan blocca direttamente questo recettore, rendendo la logica meccanicistica essenzialmente di primo principio: interrompere la segnalazione dell'Ang II nel punto effettore primario.

Il punteggio di predizione elevato del modello TxGNN (99.97%) è quindi meccanicisticamente coerente. L'incertezza principale non è la plausibilità biologica ma l'assenza completa di prove cliniche dedicate specifiche per questo sottotipo di malattia grave. Un supporto preclinico indiretto esiste da modelli animali di nefropatia ipertensiva iperazione RAAS, sebbene utilizzando un meccanismo farmacologico diverso (antagonismo dell'endotelina). L'indagine clinica formale degli ARB — incluso valsartan — nella nefropatia ipertensiva maligna rimane una questione di ricerca aperta e clinicamente rilevante.

---

## Prove da Prove Cliniche

Attualmente nessuna prova clinica correlata registrata per malattia renale da ipertensione maligna.

---

## Prove da Letteratura

| PMID | Anno | Tipo | Rivista | Risultati Chiave |
|------|------|------|---------|-----------------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Animale/Meccanicistico | Pharmacological Research | Avosentan (antagonista dell'endotelina-A) ha fornito nefroprotezzione in ratti transgenici doppi che sovraesprimono renina umana e angiotensinogeno — un modello di nefropatia ipertensiva grave guidata da RAAS — a dosi inferiori a quelle che causano ritenzione di fluidi; conferma che la modulazione farmacologica dell'asse renina-angiotensina può arrestare il danno renale ipertensivo in vivo |

> **Avvertenza importante:** Lo studio precedente valuta avosentan (un antagonista dell'endotelina), non valsartan. La sua rilevanza è meccanicistica — convalida l'iperattivazione di RAAS come il driver patologico primario della nefropatia ipertensiva maligna e dimostra che la protezione degli organi è conseguibile attraverso il blocco mirato del percorso. Non è stata identificata alcuna prova diretta clinica o sperimentale per valsartan in questa indicazione specifica.

---

## Informazioni sul Mercato di Taiwan

Nessun record di registrazione TFDA (Taiwan Food and Drug Administration) per valsartan è stato trovato in questo dataset. Valsartan è ampiamente approvato in tutte le principali giurisdizioni normative (U.S. FDA, EMA, PMDA) per ipertensione, insufficienza cardiaca con frazione di eiezione ridotta e disfunzione ventricolare sinistra post-MI. L'assenza di dati di registrazione di Taiwan in questo pacchetto di prove può riflettere una lacuna nella raccolta dati e dovrebbe essere verificata direttamente rispetto al database dei farmaci TFDA prima di prendere decisioni normative.

---

## Considerazioni sulla Sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusione e Prossimi Passi

**Decisione: In Sospeso**

**Razionale:**
Sebbene il caso meccanicistico per valsartan nella malattia renale da ipertensione maligna sia biologicamente convincente — il blocco di AT1R affronta direttamente il cascata di danno glomerulare guidata da RAAS — la base di prove attuale è L4, consistente unicamente di uno studio preclinico utilizzando un farmaco meccanicisticamente distinto. Non esistono dati clinici o osservazionali umani per supportare l'avanzamento in questa fase.

**Per procedere, è necessario quanto segue:**

- **Prove cliniche:** Studio di coorte retrospettivo o analisi di registro valutando gli esiti dell'uso di ARB (specificamente valsartan o losartan come comparatore) in pazienti con nefropatia ipertensiva maligna confermata
- **Dati meccanicistici:** Documentazione formale del MOA da DrugBank (selettività AT1R, cinetica di legame, profilo di soppressione di RAAS a valle)
- **Dati sulla sicurezza:** Foglio illustrativo TFDA o fonte equivalente per stabilire avvertenze chiave, controindicazioni e requisiti di aggiustamento della dose renale (critico considerando che la popolazione target ha compromissione renale grave per definizione)
- **Design dello studio:** Definire criteri diagnostici che distinguono la malattia renale da ipertensione maligna da altri sottotipi di nefropatia ipertensiva e identificare endpoint misurabili (traiettoria di eGFR, riduzione della proteinuria, sopravvivenza renale a 12 mesi)
- **Ponte traslazionale:** Considerare l'avvio di una revisione sistematica della letteratura o metanalisi sull'uso di ARB nell'emergenza ipertensiva con coinvolgimento renale come precursore a minor costo della pianificazione prospettica della prova

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

