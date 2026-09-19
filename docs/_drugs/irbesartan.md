---
layout: default
title: Irbesartan
parent: Prove moderate (L3-L4)
nav_order: 126
evidence_level: L4
indication_count: 4
---

# Irbesartan
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

# Irbesartan: Dall'ipertensione all'ipertensione renovascolare maligna

## Riassunto in una frase

L'irbesartan è un antagonista dei recettori dell'angiotensina II di tipo 1 (AT1) (ARB), riconosciuto a livello mondiale per l'ipertensione essenziale e la protezione renale nella nefropatia diabetica di tipo 2.
Il modello TxGNN predice che potrebbe essere efficace per l'**ipertensione renovascolare maligna** con un punteggio di previsione del 99.31%; tuttavia, **nessuno studio clinico dedicato o pubblicazione** è stato identificato per questa indicazione specifica.
Criticamente, una ben nota controindicazione della classe degli ARB — rischio di insufficienza renale acuta in caso di stenosi bilaterale dell'arteria renale — si sovrappone direttamente con l'eziologia più comune di questa indicazione predetta e vincola sostanzialmente l'ipotesi clinica.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Ipertensione essenziale / Nefropatia diabetica (ARB consolidato; nessuna autorizzazione italiana registrata) |
| Indicazione nuova predetta | Ipertensione renovascolare maligna |
| Punteggio di previsione TxGNN | 99.31% |
| Livello di evidenza | L4 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | In sospeso |

---

## Perché è ragionevole questa previsione?

Attualmente, i dati dettagliati del meccanismo di azione non sono disponibili in questo Evidence Pack (query DrugBank in sospeso). Sulla base della farmacologia consolidata, l'irbesartan è un antagonista selettivo dei recettori dell'angiotensina II di tipo 1 (AT1). Bloccando i recettori AT1, interrompe il sistema renina-angiotensina-aldosterone (RAAS): riducendo la vasocostrizione, abbassando la ritenzione di sodio mediata dall'aldosterone, e — criticamente per il rene — diminuendo la resistenza arteriolare efferente e la pressione intraglomerulare, risultando in proteinuria ridotta e nefrosclerosi più lenta.

La corrispondenza meccanicistica con l'ipertensione renovascolare maligna è immediatamente evidente: la fisiopatologia centrale segue la sequenza stenosi dell'arteria renale → ischemia renale → massiccio rilascio di renina → picco di angiotensina II → sovra-attivazione dei recettori AT1 → pressione arteriosa incontrollata con danno d'organo. Poiché l'irbesartan agisce precisamente al livello effettore AT1, mira all'apice di questa cascata. Il punteggio TxGNN di 99.31% molto probabilmente riflette la forte connettività del grafo di conoscenza tra questa malattia e il cluster dei nodi ipertensione/RAAS. Un'indicazione analoga, strettamente correlata — **malattia renale ipertensiva maligna (rango 2, stesso punteggio)** — è supportata da evidenza indiretta di Fase 3: lo studio IDNT (Lewis EJ et al., *NEJM* 2001) ha dimostrato che l'irbesartan ritarda significativamente gli endpoint compositi renali (HR 0.80, p = 0.02) nella nefropatia diabetica, una condizione che condivide lo stesso meccanismo di nefrosclerosi mediata dal RAAS e ipertensione glomerulare.

Tuttavia, una **controindicazione ben consolidata a livello di classe** deve essere messa in primo piano: i pazienti con stenosi bilaterale dell'arteria renale (o stenosi unilaterale in un rene solitario) dipendono dal tono arteriolare efferente mantenuto dall'angiotensina II per preservare la pressione di filtrazione glomerulare. L'uso di ARB o inibitori dell'ACE in questo contesto anatomico può precipitare insufficienza renale acuta. Poiché la stenosi bilaterale dell'arteria renale è una causa principale dell'ipertensione renovascolare, questa controindicazione si applica a una sottopopolazione significativa — possibilmente maggioritaria — di pazienti nell'indicazione predetta. Il modello TxGNN cattura la plausibilità farmacologica a livello del percorso, ma non sembra aver codificato questa eccezione anatomica, che è il caveat centrale per questa previsione.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato è registrato.

---

## Evidenza da letteratura

Attualmente nessuna letteratura correlata è disponibile.

---

## Informazioni sul mercato italiano

L'irbesartan non ha **autorizzazioni di commercializzazione** in Italia secondo il database normativo attuale (query AIFA: 0 record). Nessuna voce di prodotto approvato o testo di indicazione è disponibile per la revisione. L'irbesartan è, tuttavia, ampiamente autorizzato in altre giurisdizioni (UE, US, Giappone) come ARB per l'ipertensione e la nefropatia diabetica — una discrepanza che potrebbe giustificare un aggiornamento dei dati normativi prima di trarre conclusioni specifiche per paese.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.

> **Avviso al clinico (derivato dalla logica di riutilizzo, non da campi di dati di sicurezza):** Un rischio critico a livello di classe è documentato per tutti gli ARB: in caso di stenosi bilaterale dell'arteria renale o rene solitario, il blocco AT1 rimuove il supporto della pressione di filtrazione glomerulare dipendente dall'angiotensina II e può precipitare **insufficienza renale acuta**. Questo rischio è direttamente e specificamente rilevante all'indicazione predetta primaria (ipertensione renovascolare maligna) e costituisce un prerequisito di valutazione della sicurezza prima che qualsiasi indagine clinica sia progettata.

---

## Conclusioni e prossimi passi

**Decisione: In sospeso**

**Razionale:**

Nessuno studio clinico dedicato o pubblicazione supporta l'irbesartan specificamente nell'ipertensione renovascolare maligna, e il singolo sottotipo anatomico più importante di questa malattia (stenosi bilaterale dell'arteria renale) rappresenta una controindicazione nota degli ARB — significando che la previsione, sebbene logica dal punto di vista meccanicistico a livello del percorso, è clinicamente ad alto rischio senza stratificazione del paziente. L'indicazione strettamente correlata di rango 2 (malattia renale ipertensiva maligna) ha una base di evidenza più forte (L3; supporto indiretto dello studio IDNT; raccomandazione: Procedere con Guardrails) e potrebbe essere un obiettivo di riutilizzo a breve termine più fattibile.

**Per procedere, è necessario quanto segue:**

- **Dati di stratificazione del paziente**: proporzione di casi di ipertensione renovascolare maligna con stenosi unilaterale vs. bilaterale dell'arteria renale, per definire il sottoinsieme in cui l'uso di ARB è sicuro e potenzialmente benefico
- **Documentazione formale del meccanismo di azione**: query API di DrugBank (DG002 in sospeso) per confermare il profilo di legame recettoriale, la selettività e la farmacocinetica
- **Revisione dell'RCP italiano (Riassunto delle Caratteristiche del Prodotto)**: avvertenze del foglio illustrativo AIFA e controindicazioni (DG001 Blocking gap) richieste prima che qualsiasi valutazione della sicurezza possa essere completata
- **Evidenza da coorte retrospettiva**: una ricerca di dati del mondo reale o di registro su outcomes di utilizzo di ARB specificamente nell'ipertensione renovascolare unilaterale come proof-of-concept prima della progettazione dello studio
- **Riconsiderazione dell'indicazione di rango 2** (malattia renale ipertensiva maligna) come obiettivo primario di riutilizzo, data la sua sovrapposizione meccanicistica con lo studio IDNT e un profilo di rischio-evidenza più azionabile

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

