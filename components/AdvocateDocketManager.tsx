import React, { useState } from 'react';
import { CaseRegistry, Hearing } from '../types';

interface AdvocateDocketManagerProps {
  caseVault: CaseRegistry[];
  hearings: Hearing[];
  onAddCase: (caseData: Partial<CaseRegistry & { hearingDate: string; hearingTime: string; hearingTitle: string }>) => void;
  onDeleteCase: (caseId: string) => void;
  onDeleteHearing: (hearingId: string) => void;
  onExportVault: () => void;
}

export const AdvocateDocketManager: React.FC<AdvocateDocketManagerProps> = ({
  caseVault,
  hearings,
  onAddCase,
  onDeleteCase,
  onDeleteHearing,
  onExportVault,
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [activeTab, setActiveTab] = useState<'vault' | 'hearings'>('vault');

  // Form State
  const [formState, setFormState] = useState({
    caseNumber: '',
    cnrNumber: '',
    petitioner: '',
    respondent: '',
    courtName: '',
    status: 'active' as const,
    hearingDate: '',
    hearingTime: '10:30',
    hearingTitle: 'First Mention / Admission',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!formState.caseNumber || !formState.petitioner || !formState.respondent) return;
    onAddCase(formState);
    setFormState({
      caseNumber: '',
      cnrNumber: '',
      petitioner: '',
      respondent: '',
      courtName: '',
      status: 'active',
      hearingDate: '',
      hearingTime: '10:30',
      hearingTitle: 'First Mention / Admission',
    });
    setShowModal(false);
  };

  const filteredCases = caseVault.filter((c) => {
    const q = searchTerm.toLowerCase();
    return (
      c.caseNumber.toLowerCase().includes(q) ||
      (c.cnrNumber && c.cnrNumber.toLowerCase().includes(q)) ||
      c.petitioner.toLowerCase().includes(q) ||
      c.respondent.toLowerCase().includes(q) ||
      c.courtName.toLowerCase().includes(q)
    );
  });

  return (
    <div className="flex-1 overflow-y-auto p-6 md:p-10 bg-slate-950 text-slate-100">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Header Bar */}
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-semibold text-indigo-400 uppercase tracking-wider">
                Advocate Management Console
              </span>
              <span className="text-xs text-slate-500">|</span>
              <span className="text-xs text-slate-400">Full Docket Authority</span>
            </div>
            <h1 className="text-2xl font-bold text-white tracking-tight mt-1">
              Case Vault & Docket Operations
            </h1>
          </div>

          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={onExportVault}
              className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold rounded-lg border border-slate-700 transition-colors flex items-center gap-2"
              title="Export docket database to JSON"
            >
              <svg className="w-4 h-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              <span>Export Docket JSON</span>
            </button>
            <button
              type="button"
              onClick={() => setShowModal(true)}
              className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg transition-colors flex items-center gap-2 shadow-md shadow-indigo-600/30"
            >
              <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
              </svg>
              <span>Register New Case</span>
            </button>
          </div>
        </div>

        {/* Metric Overview Strip */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="p-4 rounded-xl bg-slate-900 border border-slate-800">
            <span className="text-xs font-medium text-slate-400">Total Cases</span>
            <p className="text-2xl font-bold text-white font-mono mt-1">{caseVault.length}</p>
          </div>
          <div className="p-4 rounded-xl bg-slate-900 border border-slate-800">
            <span className="text-xs font-medium text-slate-400">Active Matters</span>
            <p className="text-2xl font-bold text-indigo-400 font-mono mt-1">
              {caseVault.filter(c => c.status === 'active').length}
            </p>
          </div>
          <div className="p-4 rounded-xl bg-slate-900 border border-slate-800">
            <span className="text-xs font-medium text-slate-400">Scheduled Hearings</span>
            <p className="text-2xl font-bold text-white font-mono mt-1">{hearings.length}</p>
          </div>
          <div className="p-4 rounded-xl bg-slate-900 border border-slate-800">
            <span className="text-xs font-medium text-slate-400">24H Reminders</span>
            <p className="text-2xl font-bold text-amber-400 font-mono mt-1">
              {hearings.filter(h => {
                const diff = new Date(`${h.date}T${h.time || '10:00'}`).getTime() - Date.now();
                return diff > 0 && diff <= 86400000;
              }).length}
            </p>
          </div>
        </div>

        {/* Tab Selector & Search */}
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4">
          <div className="flex items-center gap-2 p-1 bg-slate-900 rounded-lg border border-slate-800">
            <button
              onClick={() => setActiveTab('vault')}
              className={`px-4 py-1.5 text-xs font-semibold rounded-md transition-colors ${
                activeTab === 'vault' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-white'
              }`}
            >
              Case Docket Table ({filteredCases.length})
            </button>
            <button
              onClick={() => setActiveTab('hearings')}
              className={`px-4 py-1.5 text-xs font-semibold rounded-md transition-colors ${
                activeTab === 'hearings' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-white'
              }`}
            >
              Hearing Calendar ({hearings.length})
            </button>
          </div>

          <div className="relative max-w-sm w-full">
            <input
              type="text"
              placeholder="Filter by Case No, Party, or Court..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-slate-900 border border-slate-800 rounded-lg pl-9 pr-4 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
            />
            <svg
              className="w-4 h-4 text-slate-500 absolute left-3 top-2.5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
        </div>

        {/* Tab 1: Case Vault Table */}
        {activeTab === 'vault' && (
          <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl">
            {filteredCases.length === 0 ? (
              <div className="p-12 text-center">
                <p className="text-sm text-slate-400 font-medium">No cases found in docket storage.</p>
                <p className="text-xs text-slate-500 mt-1">Register a new case or clear active search filters.</p>
              </div>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-800/80 border-b border-slate-700/80 text-slate-400 font-semibold uppercase tracking-wider">
                    <tr>
                      <th className="p-4">Case ID / Number</th>
                      <th className="p-4">Parties</th>
                      <th className="p-4">Court / Bench</th>
                      <th className="p-4">Status</th>
                      <th className="p-4 text-right">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800 text-slate-300">
                    {filteredCases.map((c) => (
                      <tr key={c.id} className="hover:bg-slate-800/50 transition-colors">
                        <td className="p-4 font-mono font-semibold text-white whitespace-nowrap">
                          {c.caseNumber}
                          {c.cnrNumber && (
                            <span className="block text-[11px] text-slate-500 font-normal">
                              CNR: {c.cnrNumber}
                            </span>
                          )}
                        </td>
                        <td className="p-4">
                          <span className="font-medium text-slate-200">{c.petitioner}</span>
                          <span className="text-slate-500 text-[10px] mx-1">vs</span>
                          <span className="font-medium text-slate-200">{c.respondent}</span>
                        </td>
                        <td className="p-4 text-slate-400">{c.courtName}</td>
                        <td className="p-4">
                          <span className={`inline-block px-2.5 py-0.5 rounded text-[10px] font-semibold tracking-wide uppercase ${
                            c.status === 'active'
                              ? 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                              : 'bg-slate-800 text-slate-400 border border-slate-700'
                          }`}>
                            {c.status}
                          </span>
                        </td>
                        <td className="p-4 text-right">
                          <button
                            onClick={() => onDeleteCase(c.id)}
                            className="px-2.5 py-1 text-[11px] font-medium text-rose-400 hover:text-white hover:bg-rose-600/80 border border-rose-500/30 rounded transition-colors"
                          >
                            Delete
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}

        {/* Tab 2: Hearing Schedule List */}
        {activeTab === 'hearings' && (
          <div className="space-y-3">
            {hearings.length === 0 ? (
              <div className="p-12 text-center bg-slate-900 border border-slate-800 rounded-2xl">
                <p className="text-sm text-slate-400 font-medium">No hearings currently scheduled.</p>
                <p className="text-xs text-slate-500 mt-1">Schedule hearing dates via case registration or AI analysis.</p>
              </div>
            ) : (
              hearings.map((h) => {
                const hearingDateTime = new Date(`${h.date}T${h.time || '10:00'}`);
                const isUpcoming = hearingDateTime.getTime() - Date.now() > 0 && hearingDateTime.getTime() - Date.now() <= 86400000;
                return (
                  <div
                    key={h.id}
                    className={`p-5 rounded-2xl bg-slate-900 border transition-all flex flex-col sm:flex-row sm:items-center justify-between gap-4 ${
                      isUpcoming ? 'border-amber-500/60 bg-amber-950/10' : 'border-slate-800'
                    }`}
                  >
                    <div>
                      <div className="flex items-center gap-3">
                        <span className="text-sm font-semibold text-white">{h.title}</span>
                        {isUpcoming && (
                          <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40 uppercase tracking-wider">
                            24H Reminder Active
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-slate-400 mt-1">{h.details}</p>
                      <p className="text-xs text-slate-500 mt-1 font-medium">{h.court}</p>
                    </div>

                    <div className="flex items-center gap-4 self-end sm:self-auto">
                      <div className="text-right">
                        <span className="block text-xs font-mono font-semibold text-white">{h.date}</span>
                        <span className="block text-xs font-mono text-slate-400">{h.time}</span>
                      </div>
                      <button
                        onClick={() => onDeleteHearing(h.id)}
                        className="px-2.5 py-1 text-xs text-rose-400 hover:text-white hover:bg-rose-600/80 border border-rose-500/30 rounded transition-colors"
                      >
                        Remove
                      </button>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        )}

        {/* Modal: Register New Case */}
        {showModal && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-in fade-in duration-200">
            <div className="w-full max-w-lg bg-slate-900 border border-slate-700 rounded-3xl p-6 sm:p-8 shadow-2xl max-h-[90vh] overflow-y-auto">
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <div>
                  <h3 className="text-lg font-bold text-white">Register Case Docket</h3>
                  <p className="text-xs text-indigo-400 font-medium">Advocate Privilege: Direct Registry Storage</p>
                </div>
                <button
                  onClick={() => setShowModal(false)}
                  className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800"
                >
                  <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>

              <form onSubmit={handleSubmit} className="space-y-4 mt-6">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">
                      Case Number <span className="text-rose-400">*</span>
                    </label>
                    <input
                      required
                      placeholder="e.g. CRL.A 421/2026"
                      value={formState.caseNumber}
                      onChange={(e) => setFormState({ ...formState, caseNumber: e.target.value })}
                      className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">
                      CNR Number (Optional)
                    </label>
                    <input
                      placeholder="e.g. DLHC010023452026"
                      value={formState.cnrNumber}
                      onChange={(e) => setFormState({ ...formState, cnrNumber: e.target.value })}
                      className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                    />
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">
                      Petitioner <span className="text-rose-400">*</span>
                    </label>
                    <input
                      required
                      placeholder="Full Name"
                      value={formState.petitioner}
                      onChange={(e) => setFormState({ ...formState, petitioner: e.target.value })}
                      className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-slate-300 mb-1">
                      Respondent <span className="text-rose-400">*</span>
                    </label>
                    <input
                      required
                      placeholder="Full Name"
                      value={formState.respondent}
                      onChange={(e) => setFormState({ ...formState, respondent: e.target.value })}
                      className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">
                    Court / Bench
                  </label>
                  <input
                    placeholder="e.g. Delhi High Court / Court 14"
                    value={formState.courtName}
                    onChange={(e) => setFormState({ ...formState, courtName: e.target.value })}
                    className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                  />
                </div>

                <div className="p-4 rounded-2xl bg-indigo-950/20 border border-indigo-500/30 space-y-3">
                  <span className="text-xs font-semibold text-indigo-300 block">
                    Optional Hearing Integration
                  </span>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label className="block text-[11px] text-slate-400 mb-1">Date</label>
                      <input
                        type="date"
                        value={formState.hearingDate}
                        onChange={(e) => setFormState({ ...formState, hearingDate: e.target.value })}
                        className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white focus:outline-none focus:border-indigo-500"
                      />
                    </div>
                    <div>
                      <label className="block text-[11px] text-slate-400 mb-1">Time</label>
                      <input
                        type="time"
                        value={formState.hearingTime}
                        onChange={(e) => setFormState({ ...formState, hearingTime: e.target.value })}
                        className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white focus:outline-none focus:border-indigo-500"
                      />
                    </div>
                  </div>
                </div>

                <div className="flex items-center justify-end gap-3 pt-4 border-t border-slate-800">
                  <button
                    type="button"
                    onClick={() => setShowModal(false)}
                    className="px-4 py-2 text-xs font-semibold text-slate-300 hover:text-white bg-slate-800 rounded-xl"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="px-5 py-2 text-xs font-semibold text-white bg-indigo-600 hover:bg-indigo-500 rounded-xl transition-colors shadow-md shadow-indigo-600/30"
                  >
                    Commit to Vault
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
