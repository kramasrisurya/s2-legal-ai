import React from 'react';
import { UserRole } from '../types';

interface TopBarProps {
  userRole: UserRole;
  onRequestRoleChange: () => void;
  activeView: 'chat' | 'dockets';
  onViewChange: (view: 'chat' | 'dockets') => void;
  vaultCount: number;
  hearingCount: number;
}

export const TopBar: React.FC<TopBarProps> = ({
  userRole,
  onRequestRoleChange,
  activeView,
  onViewChange,
  vaultCount,
  hearingCount,
}) => {
  const isAdvocate = userRole === 'advocate';
  const roleLabel = isAdvocate ? 'Logged in as: Advocate' : 'Logged in as: Client';

  return (
    <header className="h-16 px-6 bg-slate-900/90 border-b border-white/10 flex items-center justify-between gap-6 shrink-0 z-40 backdrop-blur-md">
      {/* Brand & Active Role Badge */}
      <div className="flex items-center gap-4">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-indigo-600/30 border border-indigo-400/40 flex items-center justify-center text-indigo-400">
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2" />
            </svg>
          </div>
          <span className="text-base font-bold text-white tracking-tight whitespace-nowrap">
            S2 Legal Pro
          </span>
        </div>

        {/* Vertical divider */}
        <div className="h-5 w-px bg-white/15 hidden sm:block" />

        {/* Mandatory Title Bar Role Badge - Always visible, unambiguous, clickable */}
        <button
          onClick={onRequestRoleChange}
          title="Click to request role re-authentication"
          className={`flex items-center gap-2 px-3.5 py-1.5 rounded-lg border text-xs font-semibold tracking-wide transition-all group ${
            isAdvocate
              ? 'bg-indigo-950/60 border-indigo-500/50 text-indigo-200 hover:bg-indigo-900/80 hover:border-indigo-400'
              : 'bg-teal-950/60 border-teal-500/50 text-teal-200 hover:bg-teal-900/80 hover:border-teal-400'
          }`}
        >
          <span className="w-2 h-2 rounded-full bg-current opacity-80" />
          <span className="whitespace-nowrap font-medium">{roleLabel}</span>
          <span className="text-[10px] opacity-60 group-hover:opacity-100 uppercase tracking-wider ml-1 hidden md:inline">
            (Change Role)
          </span>
        </button>
      </div>

      {/* Navigation Switch & Actions */}
      <div className="flex items-center gap-3">
        {/* View Segmented Tabs */}
        <div className="flex items-center p-1 bg-slate-950/70 border border-white/10 rounded-lg">
          <button
            onClick={() => onViewChange('chat')}
            className={`px-3 py-1 text-xs font-medium rounded-md transition-colors whitespace-nowrap ${
              activeView === 'chat'
                ? 'bg-white/15 text-white shadow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            Legal Inquiry
          </button>
          <button
            onClick={() => onViewChange('dockets')}
            className={`px-3 py-1 text-xs font-medium rounded-md transition-colors whitespace-nowrap flex items-center gap-1.5 ${
              activeView === 'dockets'
                ? 'bg-white/15 text-white shadow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <span>{isAdvocate ? 'Docket Vault' : 'Case Status'}</span>
            <span className="text-[10px] px-1.5 py-0.2 rounded bg-white/10 font-mono">
              {vaultCount}
            </span>
          </button>
        </div>

        {/* Change Role Action Button */}
        <button
          onClick={onRequestRoleChange}
          className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-300 hover:text-white bg-slate-800/80 hover:bg-slate-700/80 border border-white/10 rounded-lg transition-colors whitespace-nowrap"
          title="To change your role, you must re-authenticate."
        >
          <svg className="w-3.5 h-3.5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
          </svg>
          <span className="hidden sm:inline">Change Role</span>
        </button>
      </div>
    </header>
  );
};
