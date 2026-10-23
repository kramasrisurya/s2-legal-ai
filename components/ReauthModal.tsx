import React from 'react';
import { UserRole } from '../types';

interface ReauthModalProps {
  isOpen: boolean;
  currentRole: UserRole;
  onCancel: () => void;
  onConfirmReauth: () => void;
}

export const ReauthModal: React.FC<ReauthModalProps> = ({
  isOpen,
  currentRole,
  onCancel,
  onConfirmReauth,
}) => {
  if (!isOpen) return null;

  const currentRoleTitle = currentRole === 'advocate' ? 'Advocate' : 'Client';

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="w-full max-w-md bg-slate-900 border border-slate-700/80 rounded-2xl p-6 shadow-2xl">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/30 flex items-center justify-center text-amber-400">
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
          </div>
          <div>
            <h3 className="text-base font-semibold text-white">
              Role Re-Authentication Required
            </h3>
            <p className="text-xs text-slate-400">
              Active Session: {currentRoleTitle}
            </p>
          </div>
        </div>

        {/* Mandatory exact notification copy */}
        <div className="my-5 p-4 rounded-xl bg-slate-800/80 border border-slate-700">
          <p className="text-sm font-medium text-slate-200 leading-relaxed">
            To change your role, you must re-authenticate.
          </p>
          <p className="text-xs text-slate-400 mt-2 leading-relaxed">
            Direct role switching is restricted by access control policy. Confirming will end your active session and redirect you to the role verification screen.
          </p>
        </div>

        <div className="flex items-center justify-end gap-3 mt-6 pt-4 border-t border-slate-800">
          <button
            type="button"
            onClick={onCancel}
            className="px-4 py-2 text-xs font-semibold text-slate-300 hover:text-white bg-slate-800 hover:bg-slate-700 rounded-lg transition-colors"
          >
            Cancel
          </button>
          <button
            type="button"
            onClick={onConfirmReauth}
            className="px-4 py-2 text-xs font-semibold text-white bg-indigo-600 hover:bg-indigo-500 rounded-lg transition-colors shadow-md shadow-indigo-600/30"
          >
            Re-Authenticate
          </button>
        </div>
      </div>
    </div>
  );
};
