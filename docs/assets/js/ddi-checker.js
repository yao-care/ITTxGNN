/**
 * ITTxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author ITTxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'Grave' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'Moderata' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'Lieve' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Warfarin + Ibuprofene: aumento del rischio emorragico',
      detail: 'I FANS inibiscono la funzione piastrinica e possono potenziare l’effetto anticoagulante del warfarin, aumentando in modo significativo il rischio di sanguinamento gastrointestinale.',
      recommendation: 'Usare invece il paracetamolo oppure associare un IPP per la protezione gastrica.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Warfarin + Acido acetilsalicilico: aumento del rischio emorragico',
      detail: 'Entrambi agiscono sull’emostasi; l’uso combinato aumenta molto il rischio di sanguinamento.',
      recommendation: 'Se l’associazione è necessaria, usare acido acetilsalicilico a basse dosi e monitorare attentamente l’INR.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Warfarin + Naprossene: aumento del rischio emorragico',
      detail: 'L’associazione di naprossene e warfarin aumenta il rischio di sanguinamento gastrointestinale e di altre emorragie.',
      recommendation: 'Usare invece il paracetamolo per il dolore.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformina + mezzi di contrasto iodati: rischio di acidosi lattica',
      detail: 'I mezzi di contrasto possono causare un danno renale acuto, con accumulo di metformina e acidosi lattica.',
      recommendation: 'Sospendere la metformina 48 ore prima della procedura e riprenderla solo dopo aver accertato una funzione renale normale.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Colchicina + Claritromicina: rischio di tossicità',
      detail: 'La claritromicina è un potente inibitore del CYP3A4 e aumenta molto i livelli ematici di colchicina.',
      recommendation: 'Evitare l’associazione o ridurre in modo sostanziale la dose di colchicina.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Colchicina + inibitori della proteasi dell’HIV: rischio di tossicità grave',
      detail: 'Gli inibitori della proteasi dell’HIV aumentano marcatamente i livelli di colchicina e possono causare tossicità fatale.',
      recommendation: 'Controindicato nei pazienti con insufficienza renale o epatica.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Simvastatina + Amiodarone: rischio di miopatia',
      detail: 'L’amiodarone aumenta i livelli di simvastatina, con maggior rischio di rabdomiolisi.',
      recommendation: 'Non superare 20 mg/die di simvastatina oppure passare a un’altra statina.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'SSRI + Tramadolo: rischio di sindrome serotoninergica',
      detail: 'Entrambi aumentano l’attività serotoninergica; l’uso combinato può causare una sindrome serotoninergica potenzialmente letale.',
      recommendation: 'Monitorare attentamente i sintomi (ipertermia, mioclono, alterazione dello stato mentale) e valutare un analgesico alternativo.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'SSRI + Linezolid: rischio di sindrome serotoninergica',
      detail: 'Il linezolid è un inibitore delle MAO; associarlo a un SSRI è molto pericoloso.',
      recommendation: 'Evitare l’associazione. Se il linezolid è necessario, sospendere l’SSRI e rispettare un adeguato periodo di washout.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodarone + Moxifloxacina: rischio di prolungamento del QT',
      detail: 'Entrambi possono prolungare l’intervallo QT; l’uso combinato aumenta il rischio di torsione di punta.',
      recommendation: 'Evitare l’associazione o monitorare attentamente l’ECG.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digossina + Amiodarone: rischio di tossicità da digossina',
      detail: 'L’amiodarone aumenta i livelli ematici di digossina di circa il 70%.',
      recommendation: 'All’avvio dell’amiodarone dimezzare la dose di digossina e monitorarne i livelli ematici.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Clopidogrel + IPP: ridotto effetto antiaggregante',
      detail: 'L’omeprazolo inibisce il CYP2C19 e riduce la conversione del clopidogrel nel suo metabolita attivo.',
      recommendation: 'Valutare invece il pantoprazolo o un anti-H2.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Litio + FANS: rischio di tossicità da litio',
      detail: 'I FANS riducono l’escrezione renale del litio, aumentandone i livelli ematici.',
      recommendation: 'Evitare l’associazione o monitorare attentamente i livelli di litio.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'Integratori di potassio + diuretici risparmiatori di potassio: rischio di iperkaliemia',
      detail: 'Entrambi aumentano il potassio sierico; l’uso combinato può causare un’iperkaliemia potenzialmente letale.',
      recommendation: 'Monitorare regolarmente il potassio sierico ed evitare integrazioni di potassio concomitanti.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Metotrexato + Cotrimossazolo: rischio di mielosoppressione',
      detail: 'Entrambi inibiscono il metabolismo dei folati; l’uso combinato aumenta il rischio di mielosoppressione e mucosite.',
      recommendation: 'Evitare l’associazione oppure garantire un’adeguata integrazione di folati e monitorare attentamente l’emocromo.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'Regole DDI integrate di ITTxGNN (15 regole selezionate; non è una consultazione completa di DDInter)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">Nessun avviso di interazione trovato</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>Raccomandazione:</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">Fonte: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nRaccomandazione: ${alert.recommendation}`,
      source: {
        label: 'ITTxGNN DDI Checker',
        url: 'https://ittxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.TwTxGNN = global.TwTxGNN || {};
  global.TwTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
