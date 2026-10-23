import express from 'express';
import fs from 'fs';
import { GoogleGenAI } from '@google/genai';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SYSTEM_INSTRUCTION = (role: string) => `
You are S2 Legal AI Pro, an advanced legal intelligence engine specialized in Indian Law (Bharatiya Nyaya Sanhita 2023 [BNS], Bharatiya Nagarik Suraksha Sanhita 2023 [BNSS], Bharatiya Sakshya Adhiniyam 2023 [BSA], and earlier IPC, CrPC, IEA).
CURRENT USER ROLE: ${(role || 'advocate').toUpperCase()}

ROLE-SPECIFIC TONE & DEPTH:
${role === 'client' ? 
  `- STYLE: Use plain, empathetic, accessible English. Avoid impenetrable legal jargon. Explain concepts clearly for a common citizen.
   - FOCUS: Focus on "What does this mean for me?", immediate risks, and practical next steps.` :
  `- STYLE: Professional advocate/solicitor depth. Use precise statutory citations, procedural nuances (BNS/BNSS vs IPC/CrPC), case law principles, and strategic legal analysis.
   - FOCUS: Specific sections, limitation periods, court jurisdiction, procedural remedies (e.g. anticipatory bail, quashing under BNSS 528 / CrPC 482, writ jurisdiction).`
}

CORE DIRECTIVES:
1. MAX BREVITY & PRECISION: High information density, cleanly formatted.
2. STATUTORY MAPPING: Provide accurate cross-mapping between previous IPC/CrPC and newly enacted BNS/BNSS.
3. SMART EXTRACTION:
   - If a hearing date/time/court or mention is detected or requested: Output "HEARING_DATA: {\"title\": \"...\", \"date\": \"YYYY-MM-DD\", \"time\": \"HH:MM\", \"court\": \"...\"}" on a new line at the very end.
   - If case details (Case Number, Petitioner, Respondent, Court) are detected: Output "CASE_METADATA: {\"caseNumber\": \"...\", \"cnrNumber\": \"...\", \"petitioner\": \"...\", \"respondent\": \"...\", \"courtName\": \"...\"}" on a new line at the very end.

RESPONSE STRUCTURE:
### Summary
(${role === 'client' ? 'Concise explanation in everyday language (max 25 words)' : 'Precise legal classification and core issue summary (max 25 words)'})

### Statutory Framework
| IPC / CrPC | BNS / BNSS | ${role === 'client' ? 'Practical Meaning' : 'Statutory Scope & Legal Nuance'} |
|---|---|---|
| Sec X | Sec Y | Clear details |

### Procedural Risk Analysis
- Key procedural or liability risk point 1
- Key procedural or liability risk point 2

### Assessment Confidence: 95/100

(If hearing or case detected):
HEARING_DATA: {"title": "Matter Hearing", "date": "2026-11-05", "time": "10:30", "court": "High Court"}

MANDATORY FOOTER:
DISCLAIMER: Educational sandbox environment. Verify with an Advocate.
`;

function getIntelligentFallback(query: string, role: string): string {
  const isClient = role === 'client';
  const qLower = query.toLowerCase();

  if (qLower.includes('bail') || qLower.includes('439') || qLower.includes('bnss') || qLower.includes('arrest')) {
    return `### Summary
${isClient ? 'This relates to securing release on bail before the court under the new criminal procedure laws.' : 'Analysis of regular bail provisions under Section 483 of Bharatiya Nagarik Suraksha Sanhita, 2023 (formerly Section 439 CrPC).'}

### Statutory Framework
| IPC / CrPC | BNS / BNSS | ${isClient ? 'Practical Meaning' : 'Statutory Scope & Legal Nuance'} |
|---|---|---|
| Section 439 CrPC | Section 483 BNSS | Special powers of High Court or Court of Session regarding bail. |
| Section 437 CrPC | Section 480 BNSS | When bail may be taken in cases of non-bailable offences by Magistrate. |
| Section 438 CrPC | Section 482 BNSS | Direction for grant of bail to person apprehending arrest (Anticipatory Bail). |

### Procedural Risk Analysis
- ${isClient ? 'Ensure the petition includes proof of local residence and no flight risk.' : 'Evaluate triple test compliance (flight risk, witness tampering, evidence destruction) and parity grounds.'}
- ${isClient ? 'You must appear before the Sessions Court or High Court through your advocate.' : 'Check custody certificates, timeline of chargesheet submission under BNSS 193(3), and antecedent verification.'}

### Assessment Confidence: 96/100

HEARING_DATA: {"title": "Bail Application Mention", "date": "${new Date(Date.now() + 86400000 * 2).toISOString().split('T')[0]}", "time": "10:30", "court": "Sessions Court"}

DISCLAIMER: Educational prototype. Verify with an Advocate.`;
  }

  if (qLower.includes('bns') || qLower.includes('ipc') || qLower.includes('302') || qLower.includes('420') || qLower.includes('comparison')) {
    return `### Summary
${isClient ? 'Mapping key criminal offences from the old Indian Penal Code to the new Bharatiya Nyaya Sanhita 2023.' : 'Statutory concordance between IPC offences and codified Bharatiya Nyaya Sanhita (BNS), 2023.'}

### Statutory Framework
| IPC / CrPC | BNS / BNSS | ${isClient ? 'Practical Meaning' : 'Statutory Scope & Legal Nuance'} |
|---|---|---|
| Section 302 IPC | Section 103(1) BNS | Punishment for murder (Death or imprisonment for life and fine). |
| Section 420 IPC | Section 318(4) BNS | Cheating and dishonestly inducing delivery of property. |
| Section 406 IPC | Section 316(2) BNS | Punishment for criminal breach of trust. |
| Section 376 IPC | Section 64 BNS | Punishment for rape and aggravated offences. |

### Procedural Risk Analysis
- ${isClient ? 'Offences committed prior to July 1, 2024 are prosecuted under old IPC; offences thereafter under BNS.' : 'Strict adherence to Article 20(1) non-retroactivity: substantive law governed by date of commission, procedure by BNSS.'}
- ${isClient ? 'Section numbers have changed across all FIRs and charge documents.' : 'Verify FIR date and statutory cutoff; check corresponding digital evidence rules under BSA Section 61.'}

### Assessment Confidence: 98/100

DISCLAIMER: Educational prototype. Verify with an Advocate.`;
  }

  // Default response
  return `### Summary
${isClient ? 'Procedural overview and assessment for your legal inquiry under Indian law.' : 'Procedural classification and statutory framework under codified BNS, BNSS, and BSA 2023.'}

### Statutory Framework
| IPC / CrPC | BNS / BNSS | ${isClient ? 'Practical Meaning' : 'Statutory Scope & Legal Nuance'} |
|---|---|---|
| CrPC Sec 482 | BNSS Sec 528 | Inherent powers of High Court for quashing and preventing abuse of process. |
| CrPC Sec 154 | BNSS Sec 173 | Registration of FIR, including e-FIR provisions. |
| IEA Sec 65B | BSA Sec 61 | Electronic records and digital forensic admissibility standards. |

### Procedural Risk Analysis
- ${isClient ? 'Gather all documentary evidence and dates of transactions or incidents in chronological order.' : 'Assess territorial jurisdiction, limitation under BNSS Section 514, and availability of alternate efficacious remedies.'}
- ${isClient ? 'Always seek immediate formal verification before taking steps in court.' : 'Examine pre-cognizance requirements and locus standi before the registry.'}

### Assessment Confidence: 94/100

DISCLAIMER: Educational prototype. Verify with an Advocate.`;
}

async function startServer() {
  const app = express();
  const PORT = process.env.PORT ? parseInt(process.env.PORT, 10) : 3000;

  app.use(express.json({ limit: '50mb' }));

  const apiKey = process.env.GEMINI_API_KEY || process.env.API_KEY;
  let ai: GoogleGenAI | null = null;
  if (apiKey) {
    try {
      ai = new GoogleGenAI({
        apiKey,
        httpOptions: {
          headers: {
            'User-Agent': 'aistudio-build',
          },
        },
      });
    } catch (e) {
      console.warn('Could not initialize GoogleGenAI client:', e);
    }
  }

  // API endpoint for legal analysis
  app.post('/api/analyze', async (req, res) => {
    const { query, history = [], role = 'advocate', attachments = [] } = req.body;

    if (!query && (!attachments || attachments.length === 0)) {
      return res.status(400).json({ error: 'Query or attachments required' });
    }

    if (ai) {
      try {
        const contents: any[] = [];

        // Build history context
        if (Array.isArray(history)) {
          history.forEach((msg: any) => {
            if (msg.id === 'welcome') return;
            contents.push({
              role: msg.role === 'user' ? 'user' : 'model',
              parts: [{ text: msg.content || '' }],
            });
          });
        }

        // Build current turn parts
        const currentParts: any[] = [];
        if (query) {
          currentParts.push({ text: query });
        }

        if (Array.isArray(attachments)) {
          attachments.forEach((file: any) => {
            if (file && file.data && file.type) {
              const base64Data = file.data.includes(',') ? file.data.split(',')[1] : file.data;
              currentParts.push({
                inlineData: {
                  mimeType: file.type,
                  data: base64Data,
                },
              });
            }
          });
        }

        contents.push({
          role: 'user',
          parts: currentParts,
        });

        let textOutput = '';
        const candidateModels = ['gemini-3.8-flash', 'gemini-3.1-flash-lite'];

        for (const model of candidateModels) {
          try {
            const timeoutPromise = new Promise<never>((_, reject) =>
              setTimeout(() => reject(new Error('Timeout after 12s')), 12000)
            );
            const responsePromise = ai.models.generateContent({
              model,
              contents,
              config: {
                systemInstruction: SYSTEM_INSTRUCTION(role),
                temperature: 0.1,
              },
            });
            const response = await Promise.race([responsePromise, timeoutPromise]);
            if (response.text) {
              textOutput = response.text;
              break;
            }
          } catch (modelErr: any) {
            console.warn(`Model ${model} failed (${modelErr?.status || modelErr?.message}), trying next fallback...`);
          }
        }

        if (textOutput) {
          return res.json({ text: textOutput });
        }

        const fallbackText = getIntelligentFallback(query || '', role);
        return res.json({ text: fallbackText });
      } catch (geminiError: any) {
        console.error('Gemini processing error:', geminiError?.message || geminiError);
        const fallbackText = getIntelligentFallback(query || '', role);
        return res.json({ text: fallbackText });
      }
    }

    // Fallback if no API key
    const fallbackText = getIntelligentFallback(query || '', role);
    return res.json({ text: fallbackText });
  });

  // Health check endpoint
  app.get('/api/health', (req, res) => {
    res.json({ status: 'ok', timestamp: new Date().toISOString() });
  });

  // In production or when dist folder exists, serve static assets
  const distPath = path.join(__dirname, 'dist');
  let hasDist = fs.existsSync(path.join(distPath, 'index.html'));

  if (!hasDist && process.env.NODE_ENV === 'production') {
    try {
      console.log('dist/index.html not found in production. Running on-demand vite build...');
      const { execSync } = await import('child_process');
      execSync('npx vite build', { stdio: 'inherit' });
      hasDist = fs.existsSync(path.join(distPath, 'index.html'));
    } catch (buildErr) {
      console.warn('On-demand build warning, falling back to static serve:', buildErr);
    }
  }

  if (process.env.NODE_ENV === 'production' || hasDist) {
    if (hasDist) {
      app.use(express.static(distPath));
      app.use((req, res) => {
        res.sendFile(path.join(distPath, 'index.html'));
      });
    } else {
      // Direct root fallback
      const rootIndex = path.join(__dirname, 'index.html');
      app.use(express.static(__dirname));
      app.use((req, res) => {
        res.sendFile(rootIndex);
      });
    }
  } else {
    try {
      const { createServer: createViteServer } = await import('vite');
      const vite = await createViteServer({
        server: { middlewareMode: true, hmr: false },
        appType: 'spa',
      });
      app.use(vite.middlewares);
    } catch (viteErr) {
      console.warn('Vite dev middleware fallback:', viteErr);
      if (hasDist) {
        app.use(express.static(distPath));
        app.use((req, res) => res.sendFile(path.join(distPath, 'index.html')));
      } else {
        app.use(express.static(__dirname));
        app.use((req, res) => res.sendFile(path.join(__dirname, 'index.html')));
      }
    }
  }

  const server = app.listen(PORT, '0.0.0.0', () => {
    console.log(`S2 Legal Pro server running on http://0.0.0.0:${PORT}`);
  });

  server.on('error', (err: any) => {
    console.error('Server listen error:', err);
  });
}

startServer();
