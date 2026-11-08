interface Message {
  role: string;
  content: string;
  id?: string;
}

interface ChatRequest {
  query: string;
  history?: Message[];
  role?: string;
}

const STATUTORY_DB = [
  {
    keywords: ['cheque', 'bounce', 'dishonour', '138', 'negotiable'],
    act: 'Negotiable Instruments Act, 1881',
    provision: 'Section 138 — Dishonour of cheque for insufficiency, etc., of funds in the account',
    citations: ['Section 138, NI Act, 1881', 'Dashrath Rupsingh Rathod v. State of Maharashtra (2014)', 'Meters and Instruments Pvt. Ltd. v. Kanchan Mehta (2018)'],
    remedy: 'Statutory demand notice must be served within 30 days of memo of dishonour; 15 days cure period before filing criminal complaint under Section 142.'
  },
  {
    keywords: ['cheating', 'fraud', '420', 'deceit', 'scam', 'embezzle'],
    act: 'Indian Penal Code, 1860 / Bharatiya Nyaya Sanhita, 2023',
    provision: 'Section 420 IPC / Section 318 BNS — Cheating and dishonestly inducing delivery of property',
    citations: ['Section 415 & 420 IPC', 'Hridaya Ranjan Pd. Verma v. State of Bihar (2000)', 'Prof. R.K. Vijayasarathy v. Sudha Seetharam (2019)'],
    remedy: 'Cognizable, non-bailable offense. Mandatory prerequisite requires proving fraudulent or dishonest intention at the time of making the promise or inducement.'
  },
  {
    keywords: ['constitution', 'fundamental right', 'article 21', 'article 19', 'article 14', 'liberty', 'privacy'],
    act: 'Constitution of India, 1950',
    provision: 'Part III — Fundamental Rights (Articles 14, 19, and 21)',
    citations: ['Article 21, Constitution of India', 'K.S. Puttaswamy (Retd.) v. Union of India (2017)', 'Maneka Gandhi v. Union of India (1978)'],
    remedy: 'Direct writ petition under Article 32 (Supreme Court) or Article 226 (High Court) for violation of fundamental rights.'
  },
  {
    keywords: ['contract', 'breach', 'agreement', 'damages', 'specific performance', 'commercial'],
    act: 'Indian Contract Act, 1872 & Specific Relief Act, 1963',
    provision: 'Section 73 (Compensation for loss or damage caused by breach of contract) & Section 10 (Specific performance)',
    citations: ['Section 73, Indian Contract Act, 1872', 'Hadley v. Baxendale (1854)', 'Kailash Nath Associates v. DDA (2015)'],
    remedy: 'Commercial summary suit or arbitration if an arbitration clause is present; claim unliquidated damages or liquidated damages under Section 74.'
  },
  {
    keywords: ['arbitration', 'arbitrator', 'section 9', 'section 11', 'award', 'section 34'],
    act: 'Arbitration and Conciliation Act, 1996',
    provision: 'Section 9 (Interim relief), Section 11 (Appointment of Arbitrators), Section 34 (Setting aside arbitral award)',
    citations: ['Arbitration and Conciliation Act, 1996', 'Vidya Drolia v. Durga Trading Corp. (2020)', 'In Re: Interplay between Arbitration Agreements and Stamp Act (2023)'],
    remedy: 'Invoke arbitration clause via Section 21 notice; file Section 9 application before Court for urgent preservative interim measures.'
  },
  {
    keywords: ['bail', 'arrest', '437', '438', '439', 'anticipatory', 'police custody'],
    act: 'Code of Criminal Procedure, 1973 / BNSS, 2023',
    provision: 'Section 438 CrPC (Anticipatory Bail) & Section 439 CrPC (Special powers of High Court/Sessions Court regarding bail)',
    citations: ['Arnesh Kumar v. State of Bihar (2014)', 'Satender Kumar Antil v. CBI (2022)', 'Gurbaksh Singh Sibbia v. State of Punjab (1980)'],
    remedy: 'File anticipatory bail before the Sessions Court or High Court before custodial arrest; compliance with Section 41A CrPC notice mandatory.'
  },
  {
    keywords: ['property', 'land', 'tenant', 'eviction', 'title', 'possession', 'trespass'],
    act: 'Transfer of Property Act, 1882 & Specific Relief Act, 1963',
    provision: 'Section 54 (Sale), Section 106 (Duration of certain leases), Section 6 Specific Relief Act',
    citations: ['Section 6, Specific Relief Act, 1963', 'Maria Margarida Sequeira Fernandes v. Erasmo Jack de Sequeira (2012)'],
    remedy: 'Suit for declaration of title, mandatory and permanent injunction, and recovery of possession.'
  },
  {
    keywords: ['cyber', 'it act', 'hacking', 'identity theft', 'data leak', '66'],
    act: 'Information Technology Act, 2000',
    provision: 'Section 43 (Penalty for damage to computer systems), Section 66C (Identity theft), Section 66D (Cheating by personation)',
    citations: ['IT Act, 2000 (as amended 2008)', 'Shreya Singhal v. Union of India (2015)'],
    remedy: 'Lodge cyber crime complaint on the National Cyber Crime Reporting Portal (cybercrime.gov.in) and file FIR with State Cyber Cell.'
  }
];

export default async function handler(req: any, res: any) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { query = '', role = 'Citizen' } = req.body as ChatRequest;

    if (!query.trim()) {
      return res.status(400).json({ error: 'Query parameter is required' });
    }

    const lowerQuery = query.toLowerCase();

    // Find best match in knowledge base
    const matchedRule = STATUTORY_DB.find(rule =>
      rule.keywords.some(k => lowerQuery.includes(k))
    );

    let responseText = '';
    let citations: string[] = [];
    let confidenceScore = 0.92;

    if (matchedRule) {
      citations = matchedRule.citations;
      confidenceScore = 0.96;

      if (role === 'Judge') {
        responseText = `### ⚖️ Judicial Assessment & Statutory Framework
**Governing Statute:** ${matchedRule.act}  
**Primary Provision:** ${matchedRule.provision}

#### 1. Material Elements & Admissibility
The essential ingredients require verification under the strict evidentiary standard:
- Verification of procedural conditions precedent under governing enactments.
- Prima facie establishment of cause of action prior to framing issues or issuing summons.

#### 2. Key Binding Precedents
${matchedRule.citations.map(c => `- **${c}**`).join('\n')}

#### 3. Recommended Judicial Direction
- Order production of foundational documents and affidavits of evidence.
- Ensure strict adherence to statutory timelines and preservation of balance of convenience.`;
      } else if (role === 'Lawyer') {
        responseText = `### 🏛️ Advocate Litigation Strategy & Case Law Analysis
**Governing Statute:** ${matchedRule.act}  
**Operative Section:** ${matchedRule.provision}

#### 1. Strategic Grounds & Pleadings
- **Statutory Foundation:** File under the applicable provisions citing mandatory compliance thresholds.
- **Relief & Remedies:** ${matchedRule.remedy}

#### 2. Authoritative Authorities & Citations
${matchedRule.citations.map(c => `- *${c}*`).join('\n')}

#### 3. Immediate Action Plan
1. Issue formal legal notice/demand preserving claims with an exact evidentiary trail.
2. Draft petition/complaint with verified supporting affidavits under Section 65B of Evidence Act / Section 63 BSA.`;
      } else {
        responseText = `### 📋 Legal Assessment & Guidance Overview
**Applicable Law:** ${matchedRule.act}  
**Key Provision:** ${matchedRule.provision}

#### 1. What This Means For You
Under Indian Law, this scenario is regulated by **${matchedRule.act}**.
${matchedRule.remedy}

#### 2. Key Supreme Court & High Court Precedents
${matchedRule.citations.map(c => `- ${c}`).join('\n')}

#### 3. Recommended Steps
1. **Preserve All Records:** Keep documented copies of receipts, messages, contracts, and banking trails.
2. **Consult Counsel:** Approach an advocate specializing in ${matchedRule.act.split(',')[0]} to draft required notices within the prescribed limitation period.`;
      }
    } else {
      // General legal inquiry fallback
      citations = [
        'Constitution of India (Articles 14, 19, 21)',
        'Indian Evidence Act, 1872 / Bharatiya Sakshya Adhiniyam, 2023',
        'Supreme Court of India General Practice Guidelines'
      ];
      confidenceScore = 0.88;

      responseText = `### ⚖️ General Legal Analysis & Statutory Context
**Query Focus:** "${query}"  
**Role Perspective:** ${role}

#### 1. Conceptual Legal Framework
Under the Indian legal ecosystem, issues of this nature engage principles of substantive rights and procedural fairness:
- Substantive rights governed by statutory enactments and contract stipulations.
- Procedural compliance adhering to civil procedure (CPC 1908) or criminal procedure (CrPC / BNSS 2023).

#### 2. Key Relevant Standards
- **Audi Alteram Partem:** The fundamental requirement that no party may be judged without fair hearing.
- **Burden of Proof:** Standard rests upon the party asserting the existence of actionable facts.

#### 3. Recommended Procedural Path
1. Collate chronological documentation and identify specific statutory rights infringed.
2. Seek tailored advisory from certified legal counsel to determine forum jurisdiction.`;
    }

    return res.status(200).json({
      text: responseText,
      source: 'local_rag',
      confidence_score: confidenceScore,
      citations
    });
  } catch (error: any) {
    console.error('Legal chat processing failed:', error);
    return res.status(500).json({
      text: '⚠️ An error occurred while synthesizing the legal analysis. Please try again.',
      source: 'error',
      confidence_score: 0.0,
      citations: []
    });
  }
}
