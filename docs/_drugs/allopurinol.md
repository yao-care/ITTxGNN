---
layout: default
title: Allopurinol
parent: Solo previsione del modello (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinolo: dalla gotta alla porfiria epatica

## Sintesi in una frase

L'allopurinolo è un inibitore della xantina ossidasi, utilizzato originariamente per il trattamento della gotta, dell'iperuricemia e della nefropatia acuta da urati.
Il modello TxGNN prevede che possa essere efficace per la **porfiria epatica**,
ma al momento **non risultano studi clinici** e le **2 pubblicazioni** disponibili sono solo di livello ipotetico o preclinico.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Gotta, iperuricemia, nefropatia acuta da urati (dalle indicazioni del grafo di conoscenza; il testo autorizzato AIFA non è disponibile) |
| Nuova indicazione prevista | Porfiria epatica |
| Punteggio di predizione TxGNN | 99,95% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 15 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo report. In base alle conoscenze generali, l'allopurinolo è un inibitore della xantina ossidasi, la cui efficacia nella gotta e nell'iperuricemia è consolidata; un legame con la porfiria epatica è solo ipotizzabile.

Il collegamento possibile è che l'inibizione della xantina ossidasi possa influenzare il metabolismo delle purine e dell'eme. Si tratta però di una speculazione: le due pubblicazioni trovate non testano l'allopurinolo in pazienti con porfiria. Una è un articolo ipotetico sul targeting metabolico dell'enzima 5-aminolevulinato sintasi (ALAS1) e sull'utilizzo dell'eme; l'altra è uno studio sul ratto riguardante gli effetti della carbamazepina sul metabolismo dell'eme epatico.

Va aggiunto che i pazienti con porfiria sono sensibili a molti farmaci che inducono la sintesi epatica dell'eme, per cui la sicurezza richiederebbe una verifica molto attenta.

Anche le altre indicazioni previste (ipertensione portale familiare a esordio precoce, sindrome epatopolmonare, cirrosi idiopatica associata al rame, trombosi portale primitiva, sclerosi epatoportale, miopatia necrotizzante immunomediata, sindrome da antisintetasi, miopatia infiammatoria con abbondanti macrofagi) non hanno studi clinici né letteratura di supporto. Diverse hanno punteggi identici (0,99943), il che suggerisce un'associazione non specifica nel grafo di conoscenza e non un segnale legato alla malattia.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Ipotesi/Revisione | Medical Hypotheses | Propone il targeting metabolico della 5-ALAS, tramite triptofano o inibizione dell'utilizzo dell'eme da parte della triptofano 2,3-diossigenasi, come terapia delle porfirie epatiche acute; non riguarda direttamente l'allopurinolo |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Studio animale (ratto) | Biochemical Pharmacology | La carbamazepina, a dose molto bassa, esacerba le porfirie epatiche alterando il metabolismo dell'eme nel fegato di ratto; non riguarda l'allopurinolo |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Produttore | Stato |
|---------|------|------|------|------|
| 022441036 | Allopurinolo 50 cpr 100 mg | Non indicata | Molteni & C. F.lli Alitti | Cancellata |
| 039060076 | Allopurinolo 50 cpr 100 mg | Non indicata | Sandoz | Cancellata |
| 045054057 | Allopurinolo 30 cpr 300 mg | Non indicata | Mylan | Cancellata |
| 021259027 | Zyloric 30 cpr div 300 mg | Non indicata | Teofarma | Cancellata |
| 022051015 | Allurit 40 cpr 150 mg | Non indicata | Teofarma | Cancellata |

Sono elencate le prime 5 delle 15 autorizzazioni, tutte cancellate. Il testo dell'indicazione approvata non è disponibile.

---

## Considerazioni sulla sicurezza

- **Controindicazioni dal grafo di conoscenza** (non derivate dal foglio illustrativo): malattia epatica, malattia della colecisti, insufficienza renale, vasculite da ipersensibilità, angioite leucocitoclastica cutanea, vasculite cutanea allergica, malattia da anticorpi anti-membrana basale glomerulare.
- **Interazioni farmacologiche**: sono state identificate 217 interazioni. Tra quelle di livello moderato figurano idrossido di alluminio, attapulgite, caolino, magaldrato e sucralfato. Tra quelle minori figurano amoxicillina e clorpropamide. Per molte altre (ad es. metformina, omeprazolo, pantoprazolo, glimepiride, morfina, doxiciclina) il livello di gravità non è classificato.
- Per le avvertenze e le controindicazioni ufficiali, consultare il foglio illustrativo.

Poiché la porfiria epatica è una condizione in cui il fegato è già vulnerabile e il grafo segnala la malattia epatica come controindicazione, il profilo di sicurezza richiede particolare attenzione.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il punteggio TxGNN è molto alto, ma non esistono studi clinici e la letteratura è solo ipotetica o preclinica (livello L5). Inoltre tutte le autorizzazioni italiane risultano cancellate e il segnale di sicurezza epatica è un ulteriore elemento di cautela.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione e analisi della plausibilità biologica nella via di sintesi dell'eme
- Studi preclinici che valutino l'allopurinolo in modelli di porfiria epatica
- Foglio illustrativo AIFA con avvertenze e controindicazioni ufficiali, per la valutazione di sicurezza
- Verifica della sicurezza dell'allopurinolo in pazienti con porfiria e malattia epatica
- Chiarimento dello stato regolatorio attuale in Italia, dato che tutte le autorizzazioni sono cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

