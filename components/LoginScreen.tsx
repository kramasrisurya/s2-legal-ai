import React from 'react';
import { UserRole } from '../types';

interface LoginScreenProps {
  onSelectRole: (role: UserRole) => void;
}

export const LoginScreen: React.FC<LoginScreenProps> = ({ onSelectRole }) => {
  return (
    <div className="min-h-screen bg-slate-950 flex flex-col justify-center items-center p-6 text-slate-100">
      <div className="w-full max-w-xl bg-slate-900 border border-slate-800 rounded-3xl p-8 sm:p-10 shadow-2xl">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="w-14 h-14 bg-indigo-600/20 border border-indigo-500/30 rounded-2xl mx-auto mb-4 flex items-center justify-center text-indigo-400">
            <svg className="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2" />
            </svg>
          </div>
          <h1 className="text-2xl font-bold text-white tracking-tight">
            S2 Legal Pro
          </h1>
          <p className="text-xs text-slate-400 uppercase tracking-widest mt-1">
            Access Control Authentication
          </p>
          <p className="text-sm text-slate-300 mt-4 leading-relaxed max-w-md mx-auto">
            Select your procedural role to authenticate. Operating boundaries, permissions, and tools are strictly isolated based on your selected credential.
          </p>
        </div>

        {/* Role Selection Buttons (Mandatory) */}
        <div className="space-y-4">
          {/* Advocate Mode Option */}
          <div className="p-5 rounded-2xl bg-slate-800/60 border border-slate-700 hover:border-indigo-500/60 transition-all flex flex-col justify-between gap-4">
            <div>
              <div className="flex items-center justify-between">
                <span className="text-xs font-semibold text-indigo-400 uppercase tracking-wider">
                  Professional Practice
                </span>
                <span className="text-[11px] text-slate-400 font-mono">
                  Full Docket Authority
                </span>
              </div>
              <h2 className="text-lg font-bold text-white mt-1">
                Advocate Mode
              </h2>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                Complete access to Case Registration, Docket Vault management, Hearing Calendars, 24-hour reminder alerts, statutory comparison, and docket export.
              </p>
            </div>
            <button
              type="button"
              onClick={() => onSelectRole('advocate')}
              className="w-full py-3 px-4 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm rounded-xl transition-all shadow-md shadow-indigo-600/30 text-center"
            >
              Login as Advocate
            </button>
          </div>

          {/* Client Mode Option */}
          <div className="p-5 rounded-2xl bg-slate-800/60 border border-slate-700 hover:border-teal-500/60 transition-all flex flex-col justify-between gap-4">
            <div>
              <div className="flex items-center justify-between">
                <span className="text-xs font-semibold text-teal-400 uppercase tracking-wider">
                  Petitioner / Respondent
                </span>
                <span className="text-[11px] text-slate-400 font-mono">
                  Read-Only Transparency
                </span>
              </div>
              <h2 className="text-lg font-bold text-white mt-1">
                Client Mode
              </h2>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                Accessible legal inquiry engine, document upload, and comprehensive read-only case status tracking. Docket editing and case registration are strictly disabled.
              </p>
            </div>
            <button
              type="button"
              onClick={() => onSelectRole('client')}
              className="w-full py-3 px-4 bg-teal-600 hover:bg-teal-500 text-white font-semibold text-sm rounded-xl transition-all shadow-md shadow-teal-600/30 text-center"
            >
              Login as Client
            </button>
          </div>
        </div>

        {/* Security Policy Notice */}
        <div className="mt-8 pt-6 border-t border-slate-800 text-center">
          <p className="text-xs text-slate-500 leading-relaxed">
            Security Notice: Silent role escalation is prohibited. Role selection is verified per session. To change roles later, explicit re-authentication will be required.
          </p>
        </div>
      </div>
    </div>
  );
};
