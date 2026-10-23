import React, { useState, useEffect, useRef } from 'react';
import { LegalAIService } from './services/geminiService';
import { Message, FileAttachment, CaseSession, UserRole, Hearing, CaseRegistry } from './types';
import { ChatBubble } from './components/ChatBubble';
import { InputArea } from './components/InputArea';
import { LegalDisclaimer } from './components/LegalDisclaimer';
import { TopBar } from './components/TopBar';
import { LoginScreen } from './components/LoginScreen';
import { ReauthModal } from './components/ReauthModal';
import { AdvocateDocketManager } from './components/AdvocateDocketManager';
import { ClientCaseViewer } from './components/ClientCaseViewer';

const QUICK_ACTIONS_ADVOCATE = [
  { label: 'Statutory Comparison: IPC vs BNS', query: 'Provide a structured section-by-section mapping of IPC 302, IPC 420, and IPC 406 to the corresponding provisions under Bharatiya Nyaya Sanhita 2023.' },
  { label: 'Draft: Regular Bail Petition', query: 'Draft the essential legal grounds for a regular bail petition under Section 483 of Bharatiya Nagarik Suraksha Sanhita, 2023 (formerly Section 439 CrPC).' },
  { label: 'BNSS 528 Quashing Petition Grounds', query: 'What are the procedural requirements and grounds for filing a petition for quashing an FIR in the High Court under Section 528 BNSS?' },
  { label: 'Digital Evidence under BSA 61', query: 'Detail the statutory admissibility criteria and certificate requirements for electronic records under Section 61 of the Bharatiya Sakshya Adhiniyam, 2023.' }
];

const QUICK_ACTIONS_CLIENT = [
  { label: 'Explain My Case Status', query: 'Can you explain what happens during a First Mention or Admission hearing in court in simple terms?' },
  { label: 'What Does Bail Mean For Me?', query: 'What is bail and what conditions do I need to follow if bail is granted by the court?' },
  { label: 'Understanding FIR and Charges', query: 'What should I do if an FIR is filed, and what are my basic legal rights as a citizen under Indian law?' },
  { label: 'Documents Needed For Court', query: 'What documents should I prepare and keep ready before meeting my advocate for a court proceeding?' }
];

interface AppNotification {
  id: string;
  title: string;
  message: string;
  type: 'info' | 'warning' | 'urgent';
  timestamp: Date;
}

// Initial seed data for immediate evaluation
const INITIAL_VAULT: CaseRegistry[] = [
  {
    id: 'case-101',
    caseNumber: 'CRL.A 421/2026',
    cnrNumber: 'DLHC01004212026',
    petitioner: 'Sunil Sharma',
    respondent: 'State of NCT of Delhi',
    courtName: 'Delhi High Court - Bench 14',
    status: 'active',
  },
  {
    id: 'case-102',
    caseNumber: 'ARB.P 118/2026',
    cnrNumber: 'DLHC01001182026',
    petitioner: 'Apex Infrastructure Ltd.',
    respondent: 'National Highway Consortium',
    courtName: 'High Court Commercial Division',
    status: 'active',
  },
  {
    id: 'case-103',
    caseNumber: 'BAIL.APPL 890/2026',
    cnrNumber: 'DLPH02008902026',
    petitioner: 'Rakesh Verma',
    respondent: 'State under BNSS 483',
    courtName: 'Sessions Court Patiala House',
    status: 'pending',
  }
];

const getTomorrowDate = () => {
  const d = new Date(Date.now() + 86400000 * 0.7);
  return d.toISOString().split('T')[0];
};

const getFutureDate = (days: number) => {
  const d = new Date(Date.now() + 86400000 * days);
  return d.toISOString().split('T')[0];
};

const INITIAL_HEARINGS: Hearing[] = [
  {
    id: 'h-101',
    caseId: 'case-102',
    title: 'Urgent Motion: Section 9 Arbitration Injunction',
    date: getTomorrowDate(),
    time: '10:30',
    court: 'High Court Commercial Division',
    details: 'Petitioner: Apex Infrastructure Ltd. vs Respondent: National Highway Consortium'
  },
  {
    id: 'h-102',
    caseId: 'case-101',
    title: 'Admission & Notice Hearing',
    date: getFutureDate(3),
    time: '11:15',
    court: 'Delhi High Court - Bench 14',
    details: 'Petitioner: Sunil Sharma vs Respondent: State of NCT of Delhi'
  },
  {
    id: 'h-103',
    caseId: 'case-103',
    title: 'Bail Arguments & Custody Verification',
    date: getFutureDate(5),
    time: '14:00',
    court: 'Sessions Court Patiala House',
    details: 'Petitioner: Rakesh Verma'
  }
];

export const App: React.FC = () => {
  const [sessions, setSessions] = useState<CaseSession[]>([]);
  const [currentSessionId, setCurrentSessionId] = useState<string | null>(null);
  const [userRole, setUserRole] = useState<UserRole | null>(null);
  const [activeView, setActiveView] = useState<'chat' | 'dockets'>('chat');
  const [hearings, setHearings] = useState<Hearing[]>([]);
  const [caseVault, setCaseVault] = useState<CaseRegistry[]>([]);
  const [loading, setLoading] = useState(false);
  const [notifications, setNotifications] = useState<AppNotification[]>([]);
  const [showReauthModal, setShowReauthModal] = useState(false);

  const scrollRef = useRef<HTMLDivElement>(null);
  const legalService = useRef(new LegalAIService());

  const currentSession = sessions.find((s) => s.id === currentSessionId);

  // Initialize Data & Session State
  useEffect(() => {
    const savedRole = sessionStorage.getItem('s2_session_role') as UserRole;
    if (savedRole === 'advocate' || savedRole === 'client') {
      setUserRole(savedRole);
    }

    const savedVault = localStorage.getItem('s2_case_vault');
    if (savedVault) {
      try {
        setCaseVault(JSON.parse(savedVault));
      } catch {
        setCaseVault(INITIAL_VAULT);
      }
    } else {
      setCaseVault(INITIAL_VAULT);
      localStorage.setItem('s2_case_vault', JSON.stringify(INITIAL_VAULT));
    }

    const savedHearings = localStorage.getItem('s2_hearings');
    if (savedHearings) {
      try {
        setHearings(JSON.parse(savedHearings));
      } catch {
        setHearings(INITIAL_HEARINGS);
      }
    } else {
      setHearings(INITIAL_HEARINGS);
      localStorage.setItem('s2_hearings', JSON.stringify(INITIAL_HEARINGS));
    }
  }, []);

  // 24H Hearing Alert Engine
  useEffect(() => {
    const checkUpcomingHearings = () => {
      const now = Date.now();
      const twentyFourHours = 24 * 60 * 60 * 1000;

      hearings.forEach((h) => {
        const hearingTime = new Date(`${h.date}T${h.time || '10:00'}`).getTime();
        const diff = hearingTime - now;

        if (diff > 0 && diff <= twentyFourHours) {
          const notificationId = `alert-${h.id}`;
          if (!notifications.some((n) => n.id === notificationId)) {
            const newNotif: AppNotification = {
              id: notificationId,
              title: '24-Hour Hearing Alert',
              message: `Hearing scheduled for "${h.title}" at ${h.court} commences in less than 24 hours.`,
              type: 'urgent',
              timestamp: new Date()
            };
            setNotifications((prev) => [newNotif, ...prev]);

            if (typeof window !== 'undefined' && 'Notification' in window && Notification.permission === 'granted') {
              try {
                new Notification(newNotif.title, { body: newNotif.message });
              } catch (e) {
                console.warn('Notification failed:', e);
              }
            }
          }
        }
      });
    };

    checkUpcomingHearings();
    const timer = setInterval(checkUpcomingHearings, 30000);
    return () => clearInterval(timer);
  }, [hearings, notifications]);

  // Create initial session when user role becomes active
  useEffect(() => {
    if (userRole && sessions.length === 0) {
      createNewSession(userRole);
    }
  }, [userRole]);

  // Auto-scroll chat on new message
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTo({ top: scrollRef.current.scrollHeight, behavior: 'smooth' });
    }
  }, [currentSession?.messages, loading]);

  const createNewSession = (role: UserRole) => {
    const newId = Date.now().toString();
    const roleTitle = role === 'advocate' ? 'Advocate' : 'Client';
    const newSession: CaseSession = {
      id: newId,
      title: `${roleTitle} Analysis #${sessions.length + 1}`,
      createdAt: new Date(),
      role,
      messages: [
        {
          id: 'welcome',
          role: 'assistant',
          content: `### Active Session: ${roleTitle}\n${
            role === 'advocate'
              ? 'Advocate Mode enabled. High-precision statutory concordance (BNS/BNSS/BSA), case docket registry, and procedural analysis ready.'
              : 'Client Mode enabled. Accessible legal explanations, document review, and read-only case status tracking ready.'
          }`,
          timestamp: new Date()
        }
      ]
    };
    setSessions((prev) => [newSession, ...prev]);
    setCurrentSessionId(newId);
  };

  // Login handler
  const handleSelectRole = (selectedRole: UserRole) => {
    setUserRole(selectedRole);
    sessionStorage.setItem('s2_session_role', selectedRole);
    setActiveView('chat');
  };

  // Re-authentication confirmation handler
  const handleConfirmReauth = () => {
    // 1. Clear session role
    sessionStorage.removeItem('s2_session_role');
    setUserRole(null);
    setShowReauthModal(false);
    setActiveView('chat');
    setSessions([]);
    setCurrentSessionId(null);
  };

  const handleSendMessage = async (text: string, attachments: FileAttachment[]) => {
    if (!currentSessionId || !userRole) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: text,
      timestamp: new Date(),
      attachments
    };

    setSessions((prev) =>
      prev.map((s) => (s.id === currentSessionId ? { ...s, messages: [...s.messages, userMessage] } : s))
    );

    setLoading(true);

    try {
      const result = await legalService.current.analyzeQuery(
        text,
        currentSession?.messages || [],
        userRole,
        attachments
      );

      const responseText = typeof result === 'string' ? result : (result?.text || '');
      const source = typeof result === 'object' ? result?.source : undefined;
      const confidenceScore = typeof result === 'object' ? result?.confidence_score : undefined;
      const citations = typeof result === 'object' ? result?.citations : undefined;

      // AI Hearing Extraction (Advocate only - clients do not mutate hearing registry)
      if (userRole === 'advocate') {
        try {
          const hearingMatch = responseText.match(/HEARING_DATA:\s*(\{.*?\})/);
          if (hearingMatch) {
            const data = JSON.parse(hearingMatch[1]);
            const newHearing: Hearing = {
              id: Date.now().toString(),
              title: data.title || 'Extracted Hearing Mention',
              date: data.date || getFutureDate(2),
              time: data.time || '10:30',
              court: data.court || 'Court of Record',
              details: 'AI Extracted Schedule'
            };
            setHearings((prev) => {
              const updated = [...prev, newHearing];
              localStorage.setItem('s2_hearings', JSON.stringify(updated));
              return updated;
            });
          }
        } catch (e) {
          console.warn('Hearing extraction parse error:', e);
        }

        // AI Case Extraction (Advocate only)
        try {
          const caseMatch = responseText.match(/CASE_METADATA:\s*(\{.*?\})/);
          if (caseMatch) {
            const data = JSON.parse(caseMatch[1]);
            if (data.caseNumber) {
              const entry: CaseRegistry = {
                id: Date.now().toString(),
                caseNumber: data.caseNumber,
                cnrNumber: data.cnrNumber || '',
                petitioner: data.petitioner || 'Petitioner',
                respondent: data.respondent || 'Respondent',
                courtName: data.courtName || 'Court of Record',
                status: 'active'
              };
              setCaseVault((prev) => {
                const updated = [...prev, entry];
                localStorage.setItem('s2_case_vault', JSON.stringify(updated));
                return updated;
              });
            }
          }
        } catch (e) {
          console.warn('Case metadata extraction error:', e);
        }
      }

      const cleanContent = responseText
        .replace(/HEARING_DATA:[\s\S]*?(?=(\n\n|$))/g, '')
        .replace(/CASE_METADATA:[\s\S]*?(?=(\n\n|$))/g, '')
        .trim();

      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: cleanContent || responseText,
        timestamp: new Date(),
        source,
        confidenceScore,
        citations,
      };

      setSessions((prev) =>
        prev.map((s) => (s.id === currentSessionId ? { ...s, messages: [...s.messages, aiMessage] } : s))
      );
    } catch (err) {
      console.error(err);
      const fallbackMsg: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: '### Notice\nAn unexpected connection issue occurred while communicating with the engine. Please try your request again.',
        timestamp: new Date()
      };
      setSessions((prev) =>
        prev.map((s) => (s.id === currentSessionId ? { ...s, messages: [...s.messages, fallbackMsg] } : s))
      );
    } finally {
      setLoading(false);
    }
  };

  // Advocate Docket Management Handlers
  const handleAddCase = (
    data: Partial<CaseRegistry & { hearingDate: string; hearingTime: string; hearingTitle: string }>
  ) => {
    if (userRole !== 'advocate') return;

    const caseId = Date.now().toString();
    const entry: CaseRegistry = {
      id: caseId,
      caseNumber: data.caseNumber || 'N/A',
      cnrNumber: data.cnrNumber || '',
      petitioner: data.petitioner || 'Petitioner',
      respondent: data.respondent || 'Respondent',
      courtName: data.courtName || 'Court of Record',
      status: 'active'
    };

    const updatedVault = [entry, ...caseVault];
    setCaseVault(updatedVault);
    localStorage.setItem('s2_case_vault', JSON.stringify(updatedVault));

    if (data.hearingDate) {
      const newHearing: Hearing = {
        id: (Date.now() + 1).toString(),
        caseId: caseId,
        title: `${data.hearingTitle || 'Mention'} - ${entry.caseNumber}`,
        date: data.hearingDate,
        time: data.hearingTime || '10:30',
        court: entry.courtName,
        details: `Petitioner: ${entry.petitioner} vs Respondent: ${entry.respondent}`
      };
      const updatedHearings = [newHearing, ...hearings];
      setHearings(updatedHearings);
      localStorage.setItem('s2_hearings', JSON.stringify(updatedHearings));
    }

    const regNotif: AppNotification = {
      id: `notif-${caseId}`,
      title: 'Case Registered',
      message: `Docket ${entry.caseNumber} has been committed to vault storage.`,
      type: 'info',
      timestamp: new Date()
    };
    setNotifications((prev) => [regNotif, ...prev]);
  };

  const handleDeleteCase = (id: string) => {
    if (userRole !== 'advocate') return;
    const updated = caseVault.filter((c) => c.id !== id);
    setCaseVault(updated);
    localStorage.setItem('s2_case_vault', JSON.stringify(updated));
  };

  const handleDeleteHearing = (id: string) => {
    if (userRole !== 'advocate') return;
    const updated = hearings.filter((h) => h.id !== id);
    setHearings(updated);
    localStorage.setItem('s2_hearings', JSON.stringify(updated));
  };

  const handleExportVault = () => {
    const dataToExport = {
      exportTimestamp: new Date().toISOString(),
      role: 'advocate',
      totalCases: caseVault.length,
      cases: caseVault,
      totalHearings: hearings.length,
      hearings: hearings
    };

    const blob = new Blob([JSON.stringify(dataToExport, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `s2_legal_dockets_${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const dismissNotification = (id: string) => {
    setNotifications((prev) => prev.filter((n) => n.id !== id));
  };

  // If unauthenticated, show mandatory Login / Role Selection Screen
  if (!userRole) {
    return <LoginScreen onSelectRole={handleSelectRole} />;
  }

  const quickActions = userRole === 'advocate' ? QUICK_ACTIONS_ADVOCATE : QUICK_ACTIONS_CLIENT;

  return (
    <div className="flex flex-col h-screen overflow-hidden bg-slate-950 text-slate-100">
      {/* Top Navigation Bar with Persistent Role Badge */}
      <TopBar
        userRole={userRole}
        onRequestRoleChange={() => setShowReauthModal(true)}
        activeView={activeView}
        onViewChange={setActiveView}
        vaultCount={caseVault.length}
        hearingCount={hearings.length}
      />

      {/* Main View Area */}
      <div className="flex-1 flex overflow-hidden relative">
        {/* Urgent Notification Stack */}
        <div className="fixed top-20 right-6 z-40 flex flex-col gap-3 max-w-sm w-full pointer-events-none">
          {notifications.map((n) => (
            <div
              key={n.id}
              className={`pointer-events-auto p-4 rounded-xl border shadow-xl bg-slate-900 animate-in slide-in-from-right duration-300 ${
                n.type === 'urgent' ? 'border-amber-500/60' : 'border-slate-700'
              }`}
            >
              <div className="flex items-start justify-between gap-2">
                <div>
                  <span
                    className={`text-[11px] font-bold uppercase tracking-wider block ${
                      n.type === 'urgent' ? 'text-amber-400' : 'text-indigo-400'
                    }`}
                  >
                    {n.title}
                  </span>
                  <p className="text-xs text-slate-200 mt-1 leading-relaxed">{n.message}</p>
                </div>
                <button
                  onClick={() => dismissNotification(n.id)}
                  className="text-slate-500 hover:text-white p-1"
                >
                  <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* View 1: Legal Inquiry & Chat */}
        {activeView === 'chat' && (
          <main className="flex-1 flex flex-col h-full overflow-hidden bg-slate-950">
            <div ref={scrollRef} className="flex-1 overflow-y-auto px-4 md:px-12 py-8">
              <div className="max-w-4xl mx-auto space-y-6">
                <LegalDisclaimer />

                {/* Quick Action Prompt Cards */}
                {currentSession?.messages.length === 1 && (
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">
                    {quickActions.map((action, i) => (
                      <button
                        key={i}
                        onClick={() => handleSendMessage(action.query, [])}
                        className="p-4 text-left rounded-xl bg-slate-900 border border-slate-800 hover:border-indigo-500/50 transition-all group"
                      >
                        <span className="block text-[10px] font-semibold text-indigo-400 uppercase tracking-wider mb-1">
                          {userRole === 'advocate' ? 'Procedural Directive' : 'Client Guide'}
                        </span>
                        <span className="text-xs font-semibold text-slate-200 group-hover:text-white">
                          {action.label}
                        </span>
                      </button>
                    ))}
                  </div>
                )}

                {/* Chat Stream */}
                {currentSession?.messages.map((msg) => (
                  <ChatBubble key={msg.id} message={msg} />
                ))}

                {/* Loading indicator */}
                {loading && (
                  <div className="flex justify-start my-6">
                    <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 flex items-center gap-4">
                      <div className="flex space-x-1.5">
                        <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce"></div>
                        <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce [animation-delay:0.2s]"></div>
                        <div className="w-2 h-2 bg-indigo-500 rounded-full animate-bounce [animation-delay:0.4s]"></div>
                      </div>
                      <span className="text-xs font-medium text-slate-400">
                        {userRole === 'advocate'
                          ? 'Analyzing statutory concordance and judicial precedent...'
                          : 'Processing legal guidance in accessible terms...'}
                      </span>
                    </div>
                  </div>
                )}
              </div>
            </div>

            <InputArea onSendMessage={handleSendMessage} disabled={loading} />
          </main>
        )}

        {/* View 2: Role-Segregated Docket Views */}
        {activeView === 'dockets' && (
          <>
            {userRole === 'advocate' ? (
              <AdvocateDocketManager
                caseVault={caseVault}
                hearings={hearings}
                onAddCase={handleAddCase}
                onDeleteCase={handleDeleteCase}
                onDeleteHearing={handleDeleteHearing}
                onExportVault={handleExportVault}
              />
            ) : (
              <ClientCaseViewer
                caseVault={caseVault}
                hearings={hearings}
                onSwitchToQuery={() => setActiveView('chat')}
              />
            )}
          </>
        )}
      </div>

      {/* Mandatory Re-Authentication Modal */}
      <ReauthModal
        isOpen={showReauthModal}
        currentRole={userRole}
        onCancel={() => setShowReauthModal(false)}
        onConfirmReauth={handleConfirmReauth}
      />
    </div>
  );
};

export default App;
