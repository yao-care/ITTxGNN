---
layout: default
title: Tadalafil
parent: Solo previsione del modello (L5)
nav_order: 191
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

# TADALAFIL: da Disfunzione Erettile / Ipertensione Arteriosa Polmonare a Ipertricosi Universale Congenita di Tipo Ambras

## Riassunto in una frase

Il tadalafil è un inibitore selettivo della PDE5 ampiamente approvato per la disfunzione erettile, l'ipertensione arteriosa polmonare (PAH) e l'iperplasia prostatica benigna.
Il modello TxGNN assegna il suo punteggio più alto a **Ipertricosi Universale Congenita di Tipo Ambras**, con **0 trial clinici** e **0 pubblicazioni di supporto** — e l'evidenza meccanicistica suggerisce fortemente che si tratta di un **falso positivo**: il tadalafil è lui stesso una causa documentata di crescita eccessiva dei capelli (tricomegalia) come effetto avverso, il che significa che il modello ha probabilmente appreso un'associazione farmaco-effetto collaterale e l'ha erroneamente classificata come un segnale di trattamento.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Disfunzione erettile, ipertensione arteriosa polmonare, iperplasia prostatica benigna (noto dalla letteratura farmaceutica; nessun record normativo italiano disponibile) |
| Indicazione nuova prevista | Ipertricosi Universale Congenita di Tipo Ambras |
| Punteggio di previsione TxGNN | 99.98% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | ✗ Non commercializzato (0 licenze registrate nei dati) |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | In sospeso |

> ⚠️ **Nota sui dati**: Il tadalafil (Cialis®, Adcirca®) è disponibile in commercio in tutta l'UE, inclusa l'Italia. Il risultato zero licenze riflette probabilmente un divario nel recupero dei dati piuttosto che una vera assenza dal mercato italiano. Una conferma normativa tramite AIFA dovrebbe essere ottenuta prima di trarre conclusioni sullo stato del mercato.

---

## Perché questa previsione è ragionevole?

I dati dettagliati del meccanismo d'azione non sono presenti nel Pacchetto di Prove. Sulla base della conoscenza farmaceutica consolidata, il tadalafil inibisce selettivamente la fosfodiesterasi di tipo 5 (PDE5), prevenendo la degradazione del monofosfato di guanosina ciclico (cGMP). L'aumento risultante di cGMP intracellulare promuove il rilassamento della muscolatura liscia e la vasodilatazione — la base per i suoi usi approvati nella vascolatura peniena (disfunzione erettile), nella vascolatura polmonare (PAH) e nella muscolatura liscia prostatica (IPB).

L'ipertricosi universale congenita di tipo Ambras è un raro disturbo autosomico dominante causato da mutazioni nel gene *TRPS1*. È caratterizzato da crescita eccessiva e diffusa di peli terminali sulla superficie corporea intera. La patologia è radicata nello sviluppo anomalo del follicolo pilifero guidato da disfunzione di TRPS1, con **nessuna intersezione nota con il percorso di segnalazione PDE5/cGMP**.

La direzione meccanicistica qui è, in effetti, **invertita**: la tricomegalia (allungamento eccessivo delle ciglia) è un effetto avverso riconosciuto degli inibitori della PDE5, incluso il tadalafil, documentato in molteplici rapporti di farmacovigilanza. Ciò significa che l'aumento di cGMP probabilmente *promuove* la crescita del follicolo pilifero piuttosto che sopprimerla — esattamente il contrario di ciò che sarebbe necessario per trattare l'ipertricosi. Il modello TxGNN sembra aver codificato questa co-occorrenza farmaco-effetto collaterale come un'associazione di trattamento positivo, una modalità di fallimento nota negli algoritmi di repurposing basati su grafi di conoscenza. **Questa previsione dovrebbe essere classificata come un falso positivo ed esclusa da ulteriori sviluppi.**

---

## Evidenza da trial clinici

Attualmente nessun trial clinico correlato è registrato.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Nessuna autorizzazione normativa italiana è registrata per il tadalafil nel dataset attuale. Come notato sopra, probabilmente si tratta di un divario nei dati. Il tadalafil è autorizzato dall'UE con i marchi Cialis® (disfunzione erettile, IPB) e Adcirca® (ipertensione arteriosa polmonare); i record AIFA dovrebbero essere interrogati direttamente per confermare l'elenco delle autorizzazioni attive.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

> Nota aggiuntiva rilevante per le previsioni in questo pacchetto: Gli inibitori della PDE5 sono noti per innescare emicrania e, in casi documentati, aura emicranica tramite il percorso NO–cGMP che attiva il sistema trigeminovascolare. Un case report (PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/)) registra aura emicranica tipica associata al tadalafil senza emicrania. Questo è direttamente rilevante perché la previsione di rango 8 (emicrania con aura del tronco cerebrale) rappresenta un *rischio di sicurezza*, non un'opportunità di trattamento.

---

## Conclusione e prossimi passi

**Decisione: In sospeso**

**Razionale:**
Tutte le previsioni TxGNN di più alto rango per il tadalafil mostrano un modello sistematico di falsi positivi — disturbi correlati ai capelli (ranghi 1, 2, 5, 6) che riflettono un'inversione farmaco-effetto avverso, una malformazione cerebrale strutturale senza collegamento meccanicistico (rango 4), una condizione parodontale dove 20 pubblicazioni recuperate sono letteratura medica generale completamente non correlata al tadalafil (rango 3), e un sottotipo di emicrania dove l'unica pubblicazione rilevante documenta il tadalafil come la *causa* dell'aura (rango 8). Nessuna delle prime 8 previsioni costituisce un candidato viabile per il repurposing basato sulle evidenze attuali.

**L'unica direzione degna di investigazione formale:**

Rango 7 — **malattia cardiaca cifoscoliotica** — è l'unica previsione con una razionale indiretto ma biologicamente coerente: una grave cifoscoliosi toracica può causare malattia polmonare restrittiva → ipossia cronica → ipertensione arteriosa polmonare secondaria, e il tadalafil (Adcirca®) è approvato da FDA e EMA per PAH. Mentre nessun trial clinico dedicato esiste per questo sottogruppo, l'uso del tadalafil nell'ipertensione polmonare associata alla scoliosi rientra nell'ambito del suo meccanismo approvato.

**Per procedere, quanto segue è necessario:**

- **Remediation divario nei dati**: Recuperare i dati MOA dall'API DrugBank (DG002) e gli avvertimenti del foglio illustrativo/controindicazioni (DG001) per consentire una valutazione completa della sicurezza.
- **Verifica normativa AIFA**: Confermare lo stato di autorizzazione attuale del tadalafil in Italia (Cialis® e Adcirca® dovrebbero essere elencati; l'assenza dai dati attuali è probabilmente un errore nel recupero).
- **Audit del modello**: Segnalare le previsioni del tadalafil come caso di prova per il filtro di falso positivo PDE5i. Il modello sembra confondere sistematicamente i bordi del grafo degli effetti collaterali con i bordi terapeutici per questa classe di farmaci. Considerare di aggiungere un livello di esclusione degli effetti collaterali alla pipeline di post-processing.
- **Domanda di ricerca (solo rango 7)**: Progettare una serie di casi retrospettivi o un'analisi di sottogruppo che esamini l'uso di inibitori della PDE5 in pazienti con ipertensione polmonare associata a cifoscoliosi, utilizzando i dati del registro PAH esistente.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

