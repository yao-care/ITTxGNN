---
layout: default
title: Lisinopril
parent: Solo previsione del modello (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lisinopril: nuova indicazione prevista, Infarto miocardico posterolaterale (livello di evidenza L5). Indicazione originale: Ipertensione…"
monitor_inn: "LISINOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
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

# Lisinopril: dall'ipertensione all'infarto miocardico posterolaterale

## Sintesi in una frase

Il lisinopril è un inibitore dell'enzima di conversione dell'angiotensina (ACE), utilizzato originariamente per ipertensione e infarto miocardico. Il modello TxGNN prevede che possa essere efficace per l'**infarto miocardico posterolaterale**, ma si tratta di un sottotipo anatomico di un'indicazione già esistente. Per questa previsione non risultano **né studi clinici né pubblicazioni** specifiche (0 studi, 0 articoli).

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, infarto miocardico (il testo delle indicazioni nelle autorizzazioni AIFA non è disponibile; le indicazioni derivano dal grafo di conoscenza PrimeKG) |
| Nuova indicazione prevista | Infarto miocardico posterolaterale |
| Punteggio di previsione TxGNN | 99,90% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 20 (tutte revocate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

I dati sul meccanismo d'azione non sono al momento disponibili nei dati compilati per questo report. In base alle conoscenze generali, il lisinopril è un inibitore dell'ACE: riduce la formazione di angiotensina II e, di conseguenza, il tono vascolare e il rimodellamento cardiaco dopo infarto.

L'infarto miocardico posterolaterale è un sottotipo anatomico dell'infarto miocardico, indicazione già associata al lisinopril. Non si tratta quindi di un vero riposizionamento. Il punteggio elevato riflette probabilmente la vicinanza ontologica al termine "infarto miocardico" nel grafo di conoscenza, più che un'evidenza specifica per questo sottotipo.

Tra le altre previsioni del modello, alcune sono meccanisticamente plausibili ma poco supportate:

- **Cuore polmonare cronico** (punteggio 99,68%): due lavori specifici sul lisinopril (PMID 14524095 e 17047621), probabilmente piccoli studi clinici, suggeriscono un beneficio emodinamico ed endoteliale. Il disegno e la numerosità non sono verificabili.
- **Ipertensione polmonare da malattia polmonare/ipossia**: la letteratura recuperata è per lo più non pertinente (fisiologia animale, trote, retinopatia del prematuro). Gli ACE-inibitori non sono raccomandati dalle linee guida per l'ipertensione polmonare e la vasodilatazione sistemica potrebbe peggiorare l'ipossiemia.
- **Ipertensione/nefropatia ipertensiva maligna e ipertensione nefrovascolare maligna**: plausibili per il coinvolgimento del sistema renina-angiotensina, ma gli ACE-inibitori possono causare peggioramento della funzione renale in presenza di stenosi dell'arteria renale.

## Evidenza da studi clinici

Attualmente non risultano studi clinici registrati correlati a questa previsione.

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata per l'infarto miocardico posterolaterale.

Per completezza, le previsioni di rango inferiore dispongono di pochi riferimenti rilevanti:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Studio clinico (disegno non verificato) | Kardiologiia | Il lisinopril 10 mg/die ha attenuato l'ipertensione polmonare e migliorato la funzione sistolica del ventricolo destro in pazienti con scompenso cardiaco, cardiopatia ischemica e BPCO |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Studio clinico (disegno non verificato) | Probl Tuberk Bolezn Legk | Lisinopril nel trattamento di pazienti con cuore polmonare cronico (abstract non disponibile) |
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | Caso clinico | JPMA | ACE-inibitore più coenzima Q10 come trattamento aggiuntivo in un caso di rottura del setto interventricolare dopo infarto; evidenza solo indiretta |
| [20852161](https://pubmed.ncbi.nlm.nih.gov/20852161/) | 2010 | Caso clinico | Am J Health Syst Pharm | Ipotensione e bradicardia gravi con l'associazione tizanidina e lisinopril (segnale di sicurezza) |

## Informazioni sul mercato italiano

Tutte e 20 le autorizzazioni risultano revocate. Il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili nei dati compilati. Le prime 5:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 037426158 | LISINOPRIL*14 cpr 20 mg | Ratiopharm GmbH | Revocata |
| 026834022 | ZESTRIL*14 cpr 20 mg | Atnahs Pharma Netherlands BV | Revocata |
| 026837017 | ALAPRIL*14 cpr 5 mg | Neopharmed Gentili SpA | Revocata |
| 026837029 | ALAPRIL*14 cpr 20 mg | Neopharmed Gentili SpA | Revocata |
| 037471188 | LISINOPRIL*28 cpr 20 mg | Sandoz SpA | Revocata |

## Considerazioni sulla sicurezza

I dati di etichetta (avvertenze e controindicazioni) non sono disponibili; si rimanda al foglio illustrativo.

**Controindicazioni e condizioni a rischio (dal grafo di conoscenza, non dal testo dell'etichetta):** angioedema (incluso quello ereditario, acquisito e indotto da bloccanti del sistema renina-angiotensina-aldosterone), malattia renale, malattia epatica ed encefalopatia epatica, pancreatite, malattie della colecisti, lupus eritematoso sistemico, diabete e chetoacidosi diabetica, deficit di potassio, neutropenia/agranulocitosi, stenosi aortica, ipotensione, iperparatiroidismo, malattie del tessuto connettivo e malattie ossee.

**Interazioni farmacologiche:** sono state rilevate 100 interazioni complessive; tra quelle elencate:
- **Maggiori:** citrato di potassio, bicarbonato di potassio (rischio di iperkaliemia).
- **Moderate:** corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), antidiabetici (metformina, inibitori di SGLT2 e DPP-4, clorpropamide), acido acetilsalicilico, morfina, bupropione, dronabinolo, lassativi/preparati per la pulizia intestinale.

Dalla letteratura emerge inoltre un segnale di ipotensione e bradicardia con l'associazione a tizanidina.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione riguarda un sottotipo anatomico di un'indicazione già nota e non è supportata da studi o pubblicazioni specifici (livello L5). Inoltre, tutte le autorizzazioni italiane sono revocate, quindi non vi è un prodotto commercializzato su cui basare un'estensione.

**Per procedere sono necessari:**
- Verifica dell'attuale stato regolatorio in Italia e delle ragioni delle revoche
- Testo delle indicazioni approvate e dati di etichetta (avvertenze e controindicazioni) dalle schede tecniche AIFA
- Dati sul meccanismo d'azione da DrugBank
- Valutazione se l'infarto miocardico posterolaterale rientri già nell'indicazione "infarto miocardico", rendendo superfluo un riposizionamento
- Per le previsioni di rango inferiore (in particolare il cuore polmonare cronico): verifica del disegno e della numerosità degli studi esistenti e, se opportuno, studi clinici controllati
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

