import React, { useState } from 'react';
import { CaseRegistry, Hearing } from '../types';

interface ClientCaseViewerProps {
  caseVault: CaseRegistry[];
  hearings: Hearing[];
  onSwitchToQuery: () => void;
}

export const ClientCaseViewer: React.FC<ClientCaseViewerProps> = ({
  caseVault,
  hearings,
  onSwitchToQuery,
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCaseId, setSelectedCaseId] = useState<string | null>(null);

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

  const selectedCase = caseVault.find((c) => c.id === selectedCaseId) || filteredCases[0];

  return (
    <div className="flex-1 overflow-y-auto p-6 md:p-10 bg-slate-950 text-slate-100">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Client Header Notice */}
        <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-semibold text-teal-400 uppercase tracking-wider">
                Client Case Status Directory
              </span>
              <span className="text-xs text-slate-500">|</span>
              <span className="text-xs text-slate-400">Read-Only Transparency Mode</span>
            </div>
            <h1 className="text-xl font-bold text-white mt-1">
              Active Matter Records & Hearing Timelines
            </h1>
            <p className="text-xs text-slate-400 mt-2 max-w-xl">
              Track your court proceedings, upcoming dates, and bench assignments. Docket registration and modification are managed strictly by your Advocate.
            </p>
          </div>

          <button
            type="button"
            onClick={onSwitchToQuery}
            className="px-4 py-2 bg-teal-600 hover:bg-teal-500 text-white text-xs font-semibold rounded-xl transition-colors self-start sm:self-auto shadow-md shadow-teal-600/30 whitespace-nowrap"
          >
            Ask Legal Question
          </button>
        </div>

        {/* Search Bar */}
        <div className="relative max-w-md w-full">
          <input
            type="text"
            placeholder="Search by Case Number, Party Name, or Court..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-slate-900 border border-slate-800 rounded-xl pl-9 pr-4 py-2.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-teal-500 transition-colors"
          />
          <svg
            className="w-4 h-4 text-slate-500 absolute left-3 top-3"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>

        {/* Master-Detail / Responsive Grid */}
        {filteredCases.length === 0 ? (
          <div className="p-12 text-center bg-slate-900 border border-slate-800 rounded-2xl">
            <p className="text-sm text-slate-300 font-medium">No active matter records found.</p>
            <p className="text-xs text-slate-500 mt-1">
              Your advocate has not registered any cases under this docket, or your search filter has no matching entries.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Left Column: Matter Cards */}
            <div className="space-y-3 lg:col-span-1">
              <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-2">
                Matter Directory ({filteredCases.length})
              </span>
              {filteredCases.map((c) => {
                const isSelected = selectedCase?.id === c.id;
                return (
                  <div
                    key={c.id}
                    onClick={() => setSelectedCaseId(c.id)}
                    className={`p-4 rounded-xl border cursor-pointer transition-all ${
                      isSelected
                        ? 'bg-teal-950/30 border-teal-500/60 shadow-lg'
                        : 'bg-slate-900 border-slate-800 hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-mono text-xs font-bold text-white">{c.caseNumber}</span>
                      <span className={`px-2 py-0.5 rounded text-[9px] font-semibold uppercase ${
                        c.status === 'active'
                          ? 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                          : 'bg-slate-800 text-slate-400 border border-slate-700'
                      }`}>
                        {c.status}
                      </span>
                    </div>
                    <p className="text-xs text-slate-300 font-medium">
                      {c.petitioner} vs {c.respondent}
                    </p>
                    <p className="text-[11px] text-slate-500 mt-1">{c.courtName}</p>
                  </div>
                );
              })}
            </div>

            {/* Right Column: Detailed Timeline & Hearing View */}
            <div className="lg:col-span-2 space-y-6">
              {selectedCase && (
                <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-6">
                  {/* Case Header */}
                  <div className="pb-4 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                    <div>
                      <span className="text-[11px] text-slate-400 font-mono uppercase tracking-wider">
                        Docket Record
                      </span>
                      <h2 className="text-xl font-bold text-white font-mono mt-0.5">
                        {selectedCase.caseNumber}
                      </h2>
                    </div>
                    <div className="text-left sm:text-right">
                      <span className="text-xs text-slate-400 block">Court Assignment</span>
                      <span className="text-xs font-semibold text-teal-300">{selectedCase.courtName}</span>
                    </div>
                  </div>

                  {/* Parties Overview */}
                  <div className="grid grid-cols-2 gap-4 p-4 rounded-xl bg-slate-800/60 border border-slate-700/60">
                    <div>
                      <span className="text-[11px] font-medium text-slate-400 uppercase tracking-wider block">
                        Petitioner
                      </span>
                      <span className="text-sm font-semibold text-white mt-1 block">
                        {selectedCase.petitioner}
                      </span>
                    </div>
                    <div>
                      <span className="text-[11px] font-medium text-slate-400 uppercase tracking-wider block">
                        Respondent
                      </span>
                      <span className="text-sm font-semibold text-white mt-1 block">
                        {selectedCase.respondent}
                      </span>
                    </div>
                  </div>

                  {/* Hearings Associated */}
                  <div>
                    <h3 className="text-xs font-semibold text-slate-300 uppercase tracking-wider mb-3">
                      Scheduled Court Appearances
                    </h3>
                    {hearings.length === 0 ? (
                      <p className="text-xs text-slate-500 italic p-4 bg-slate-800/40 rounded-xl">
                        No upcoming hearing dates have been scheduled for this case yet.
                      </p>
                    ) : (
                      <div className="space-y-3">
                        {hearings.map((h) => (
                          <div
                            key={h.id}
                            className="p-4 rounded-xl bg-slate-800/70 border border-slate-700/80 flex items-center justify-between"
                          >
                            <div>
                              <span className="text-xs font-semibold text-white">{h.title}</span>
                              <p className="text-[11px] text-slate-400 mt-0.5">{h.court}</p>
                            </div>
                            <div className="text-right">
                              <span className="font-mono text-xs font-bold text-teal-300 block">{h.date}</span>
                              <span className="font-mono text-[11px] text-slate-400">{h.time}</span>
                            </div>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>

                  {/* Policy reminder */}
                  <div className="p-3.5 rounded-xl bg-slate-800/40 border border-slate-700/50 text-[11px] text-slate-400 leading-relaxed">
                    Note: Hearing schedules and listed bench updates are provided by your Advocate. If you notice any discrepancy, please consult your Advocate directly.
                  </div>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
