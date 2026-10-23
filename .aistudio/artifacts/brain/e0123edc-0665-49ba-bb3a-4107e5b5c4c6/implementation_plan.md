# S2 Legal AI: Strict Role-Based Access Control & Case Management

S2 Legal AI provides an enterprise legal assistant and docket manager with strict role-based access control (RBAC). The application isolates Advocate Mode (full docket registration, scheduling, alerts, and export) from Client Mode (plain-English legal analysis, document upload, and comprehensive read-only case tracking), enforcing mandatory role authentication and zero unauthenticated role switching.

## User Review & Critical Decisions

> [!IMPORTANT]
> The following confirmed decisions govern this implementation based on user feedback:

- **Confirmed Decision 1: Client Mode Case Visibility**: As confirmed ("everything"), clients have complete read-only visibility into case dockets, upcoming court dates, procedural timelines, and CNR search, with all case registration and vault mutation controls strictly disabled.
- **Confirmed Decision 2: Case Vault Persistence & Export**: Advocate dockets and hearings persist in local storage with one-click JSON docket export and backup functionality.
- **Confirmed Decision 3: Mandatory Re-Authentication Barrier**: Users cannot switch roles directly from the dashboard. Clicking the visible title bar role badge or selecting "Change Role" presents a security confirmation modal with exact text: `"To change your role, you must re-authenticate."`, clears the active session role, and redirects to the Login screen with explicit `[ Login as Advocate ]` and `[ Login as Client ]` actions.
- **Confirmed Decision 4: No Emojis in Security/Role Contexts**: All role identifiers, security prompts, badges, and system notifications adhere to professional, non-symbolic legal formatting.

---

## 1. Overview & Core Concept

- **What It Does**: Establishes an uncompromised two-tier legal platform where Advocates possess administrative docket authority (case creation, hearing calendar, alerts, docket backup) and Clients possess client-centric legal inquiry tools with read-only case tracking.
- **Target Audience / Persona**:
  - *Advocates*: Legal practitioners managing litigation dockets, client files, court hearing calendars, and BNS/BNSS statutory research.
  - *Clients*: Petitioners and respondents seeking understandable statutory explanations, document verification, and status monitoring of their ongoing matters.
- **Key Value**: Enforces legal boundary integrity, eliminating accidental docket manipulation by clients while keeping both roles aligned on real-time statutory research powered by Gemini on the server.

---

## 2. User Experience & Visual Design

### Key User Flows

1. **Authentication & Protocol Selection (Login Screen)**:
   - Zero-state view if no active session role exists.
   - Professional legal header with clear role selection options:
     - `[ Login as Advocate ]`: High-density professional workspace.
     - `[ Login as Client ]`: Plain-language guided legal interface.
   - Mandatory selection before any dashboard access is granted.

2. **Top Navigation Bar Contract**:
   - Single-row header with three zones:
     - *Brand Zone*: `S2 Legal Pro` (display face, single line).
     - *Role Identification Zone*: Non-ambiguous badge displayed prominently:
       - `Logged in as: Advocate` (distinctive slate/indigo border).
       - `Logged in as: Client` (distinctive neutral/cyan border).
       - Clicking the badge triggers the Re-Authentication Confirmation Flow.
     - *Primary Action Zone*: Quick action button ("New Query" or "Export Docket" for Advocate) + "Change Role" button with lock icon.

3. **Role Switching & Re-Authentication Flow**:
   - Triggered by clicking the title bar role badge or the "Change Role" action.
   - Displays modal dialog:
     - Title: `Authentication Required`
     - Notice: `"To change your role, you must re-authenticate."`
     - Action: `[ Proceed to Re-Authenticate ]` and `[ Return to Workspace ]`.
   - On confirmation: clears the session role immediately, resets memory, and presents the Login / Role Selection screen.

4. **Advocate Mode Experience**:
   - Case Vault sidebar and docket table enabled.
   - "Register Case" button with docket modal (Case Number, CNR, Petitioner, Respondent, Court, Next Hearing).
   - "Export Docket" JSON backup utility.
   - 24-hour hearing reminder engine with urgency tags.
   - Technical statutory framework analysis (BNS/BNSS vs IPC/CrPC citations).

5. **Client Mode Experience**:
   - Case registration form completely hidden and blocked in state.
   - Read-only Case Status & Hearing Schedule panel (searchable by case number or party name).
   - Document upload for query analysis.
   - Plain-English legal breakdowns focusing on practical client implications.

### Visual Identity & Theme

- **Palette**: Deep slate canvas (`#020617`), structural cards with hairline borders (`#1E293B` / `border-white/10`), crisp neutral typography (`#F8FAFC`, `#94A3B8`).
- **Typography**: Display typography using `Plus Jakarta Sans` with uppercase tracking for section labels, and tabular figures (`tabular-nums`) for case numbers, CNR numbers, and court hearing dates.
- **Restraint**: Zero emojis in badges, titles, security dialogues, or system alerts. Clean SVG icons strictly used for functional affordances.

---

## 3. Key Product Decisions & Trade-Offs

- **Decision 1: Hardened Role Isolation in React State & UI Rendering**:
  - *Chosen Approach*: Role-specific view components (`AdvocateView` vs `ClientView`) rendered strictly based on the authenticated `userRole` state.
  - *Why*: Guarantees that Advocate docket mutation methods (`handleManualCaseSubmit`, docket delete, export) cannot be triggered or mounted in Client mode.
- **Decision 2: Re-Authentication Security Gateway**:
  - *Chosen Approach*: Intercept any role-change intent with a confirmation dialog requiring explicit user re-login rather than hot-switching roles in the active dashboard.
  - *Why*: Complies strictly with the security rule against silent escalation (Client → Advocate) and maintains strict session integrity.
- **Decision 3: Express 5 Catch-All Route Compatibility**:
  - *Chosen Approach*: Replace legacy `app.get('*')` with catch-all middleware `app.use((req, res) => res.sendFile(...))` in `server.ts`.
  - *Why*: Eliminates `path-to-regexp` v6 syntax error during production Cloud Run deployments.

---

## 4. Technical Architecture & Data Strategy

### System Architecture Diagram

```
┌────────────────────────────────────────────────────────────────────────┐
│                          S2 Legal AI Platform                          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
            ┌───────────────────────┴───────────────────────┐
            │                                               │
            ▼                                               ▼
┌───────────────────────┐                       ┌───────────────────────┐
│     Unauthenticated   │                       │      Authenticated    │
│  Role Selection Screen│                       │   Top Navigation Bar  │
│                       │                       │                       │
│ [ Login as Advocate ] │                       │ Badge:                │
│ [ Login as Client ]   │                       │ "Logged in as: ..."   │
└───────────┬───────────┘                       │ [ Change Role ]       │
            │                                   └───────────┬───────────┘
            │                                               │
            ▼                                               ▼
┌───────────────────────┐                       ┌───────────────────────┐
│ Set Session Role State│                       │ Re-Auth Modal:        │
│ advocate | client     │                       │ "To change your role, │
└───────────┬───────────┘                       │ you must re-auth."    │
            │                                   └───────────┬───────────┘
            │                                               │
            ├───────────────────────┐                       ▼
            │                       │           ┌───────────────────────┐
            ▼                       ▼           │ Clear Session Role &  │
┌───────────────────────┐ ┌───────────────────┐ │ Redirect to Login     │
│     Advocate Mode     │ │    Client Mode    │ └───────────────────────┘
│                       │ │                   │
│ - Register New Case   │ │ - Legal Chat & AI │
│ - Case Vault & Delete │ │ - Upload Doc      │
│ - Hearing Scheduling  │ │ - Read-Only Cases │
│ - 24H Alert Engine    │ │ - Status Tracker  │
│ - Docket JSON Export  │ │ - Plain English   │
└───────────┬───────────┘ └─────────┬─────────┘
            │                       │
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │ Express Backend Proxy │
            │      (server.ts)      │
            │                       │
            │ POST /api/analyze     │
            │  └─ Gemini Cascade    │
            │  └─ Legal Fallback    │
            └───────────────────────┘
```

### Component & State Mapping

- `App.tsx`:
  - `userRole: 'advocate' | 'client' | null`
  - `showReauthModal: boolean` (controls re-authentication confirmation dialog)
  - `activeTab: 'chat' | 'dockets' | 'schedule'`
  - Top title bar with badge: `"Logged in as: Advocate"` or `"Logged in as: Client"`
- `components/LoginScreen.tsx`:
  - Dedicated role selection view presenting `[ Login as Advocate ]` and `[ Login as Client ]`.
- `components/TopBar.tsx`:
  - Displays wordmark, active role badge with hover state, and `Change Role` trigger.
- `components/ReauthModal.tsx`:
  - Dedicated confirmation modal enforcing `"To change your role, you must re-authenticate."`.
- `components/ClientCaseViewer.tsx`:
  - Read-only docket and hearing viewer tailored for petitioners and clients with search and filter.
- `components/AdvocateDocketManager.tsx`:
  - Full registration, management, deletion, and export suite.
