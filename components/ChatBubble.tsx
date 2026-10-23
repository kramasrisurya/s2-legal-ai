import React, { useState } from 'react';
import { Message } from '../types';

interface ChatBubbleProps {
  message: Message;
}

export const ChatBubble: React.FC<ChatBubbleProps> = ({ message }) => {
  const isUser = message.role === 'user';
  const [showCitations, setShowCitations] = useState(false);

  const renderFormattedContent = (content: string) => {
    const parts = content.split(/(```[\s\S]*?```|\|[\s\S]*?\|\n)/g);

    return parts.map((part, index) => {
      if (part.startsWith('```')) {
        const cleanCode = part.replace(/```(markdown|text|legal)?/g, '').trim();
        return (
          <div key={index} className="relative group my-4">
            <pre className="whitespace-pre-wrap bg-slate-950/90 p-4 rounded-xl border border-white/10 text-xs font-mono text-cyan-200">
              {cleanCode}
            </pre>
            <button
              onClick={() => {
                if (navigator.clipboard?.writeText) {
                  navigator.clipboard.writeText(cleanCode).catch(() => {});
                }
              }}
              className="absolute top-3 right-3 bg-cyan-500/20 hover:bg-cyan-500 text-cyan-300 hover:text-white text-[10px] font-black px-2.5 py-1 rounded-lg transition-all opacity-0 group-hover:opacity-100 uppercase tracking-widest border border-cyan-500/30"
            >
              Copy Draft
            </button>
          </div>
        );
      }

      if (part.startsWith('|')) {
        const rows = part.trim().split('\n');
        const headerRow = rows[0].split('|').filter((c) => c.trim() !== '');
        const dataRows = rows.slice(2).map((r) => r.split('|').filter((c) => c.trim() !== ''));

        return (
          <div key={index} className="overflow-x-auto my-6 rounded-xl border border-white/10 bg-white/[0.02]">
            <table className="w-full text-left border-collapse text-xs">
              <thead>
                <tr className="border-b border-white/10 bg-white/5">
                  {headerRow.map((h, i) => (
                    <th key={i} className="p-3 font-bold text-cyan-300 uppercase tracking-wider">
                      {h.trim()}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-white/5">
                {dataRows.map((row, i) => (
                  <tr key={i} className="hover:bg-white/[0.02] transition-colors">
                    {row.map((cell, j) => (
                      <td key={j} className="p-3 text-slate-300">
                        {cell.trim()}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        );
      }

      return part.split('\n').map((line, i) => {
        if (line.startsWith('###')) {
          return (
            <h3 key={`${index}-${i}`} className="text-base font-bold text-white mt-5 mb-2 flex items-center gap-2">
              <span className="w-1.5 h-4 bg-cyan-400 rounded-full inline-block"></span>
              {line.replace('###', '').trim()}
            </h3>
          );
        }
        if (line.includes('Confidence:') || line.includes('Confidence Score') || line.includes('Confidence')) {
          const match = line.match(/\b(\d{1,3})\b/);
          const score = match ? Math.min(100, Math.max(0, parseInt(match[1]))) : 92;
          return (
            <div key={`${index}-${i}`} className="mt-6 p-4 rounded-2xl bg-white/5 border border-white/10">
              <div className="flex justify-between text-[10px] font-black text-indigo-400 uppercase tracking-[0.2em] mb-2">
                <span>Agent Validation Protocol</span>
                <span>{score}% Ready</span>
              </div>
              <div className="h-2 w-full bg-white/5 rounded-full overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 transition-all duration-1000"
                  style={{ width: `${score}%` }}
                ></div>
              </div>
            </div>
          );
        }
        if (line.trim().startsWith('- ') || line.trim().startsWith('* ')) {
          return (
            <li key={`${index}-${i}`} className="ml-4 list-disc text-[14px] text-slate-200 mb-1 leading-relaxed">
              {line.replace(/^[-*]\s*/, '')}
            </li>
          );
        }
        return (
          <p key={`${index}-${i}`} className="mb-2.5 opacity-90 leading-relaxed text-[14px]">
            {line}
          </p>
        );
      });
    });
  };

  return (
    <div className={`flex w-full mb-10 ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`relative max-w-[92%] md:max-w-[82%] p-7 transition-all ${
          isUser
            ? 'bg-gradient-to-br from-indigo-600 to-fuchsia-700 text-white rounded-[2rem] rounded-tr-none shadow-[0_15px_40px_rgba(79,70,229,0.3)]'
            : 'glass-ultra border-l-4 border-l-cyan-500 text-slate-100 rounded-[2rem] rounded-tl-none bg-slate-950/80 border border-slate-800'
        }`}
      >
        {/* Stream / Origin Header */}
        <div className={`absolute -top-7 ${isUser ? 'right-4' : 'left-4'} flex items-center gap-2`}>
          <div className={`w-2 h-2 rounded-full ${isUser ? 'bg-fuchsia-400' : 'bg-cyan-400 animate-pulse'}`}></div>
          <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">
            {isUser ? 'Petitioner Entry' : 'S2 AI Agent Stream'}
          </span>
        </div>

        {/* Trust & Verification Badge for AI Messages */}
        {!isUser && (
          <div className="mb-5 flex flex-wrap items-center gap-2.5">
            {message.source === 'local_rag' && (
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-950/90 text-emerald-300 border border-emerald-500/40 shadow-[0_0_15px_rgba(16,185,129,0.2)]">
                {/* Lock Icon */}
                <svg className="w-3.5 h-3.5 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2" strokeWidth="2.5" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" strokeWidth="2.5" strokeLinecap="round" />
                </svg>
                <span>Local RAG (Constitutional Database)</span>
                {typeof message.confidenceScore === 'number' && (
                  <span className="ml-1 px-1.5 py-0.5 rounded-md bg-emerald-900/60 text-emerald-200 text-[10px] font-mono">
                    {(message.confidenceScore * 100).toFixed(0)}% Match
                  </span>
                )}
              </div>
            )}

            {message.source === 'gemini_fallback' && (
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-sky-950/90 text-sky-300 border border-sky-500/40 shadow-[0_0_15px_rgba(56,189,248,0.2)]">
                {/* Cloud Icon */}
                <svg className="w-3.5 h-3.5 text-sky-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
                <span>Cloud API (Web Grounded)</span>
                {typeof message.confidenceScore === 'number' && (
                  <span className="ml-1 px-1.5 py-0.5 rounded-md bg-sky-900/60 text-sky-200 text-[10px] font-mono">
                    {(message.confidenceScore * 100).toFixed(0)}% Score
                  </span>
                )}
              </div>
            )}

            {!message.source && (
              <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-950/70 text-indigo-300 border border-indigo-500/30">
                <span>Hybrid Intelligence Engine</span>
              </div>
            )}
          </div>
        )}

        {/* Message Legal Content */}
        <div className="legal-content">
          {isUser ? <p className="whitespace-pre-wrap">{message.content}</p> : renderFormattedContent(message.content)}
        </div>

        {/* Source Citations Collapsible Accordion (for verifiable AI) */}
        {!isUser && message.citations && message.citations.length > 0 && (
          <div className="mt-6 pt-4 border-t border-white/10">
            <button
              onClick={() => setShowCitations(!showCitations)}
              className="w-full flex items-center justify-between px-4 py-2.5 rounded-xl bg-slate-900/70 hover:bg-slate-900 border border-white/10 transition-colors text-left group"
            >
              <div className="flex items-center gap-2">
                <svg className="w-4 h-4 text-cyan-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
                <span className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                  Source Citations
                </span>
                <span className="px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 text-[10px] font-black border border-cyan-500/30">
                  {message.citations.length}
                </span>
              </div>

              <div className="flex items-center gap-1.5 text-[11px] font-semibold text-slate-400 group-hover:text-cyan-300">
                <span>{showCitations ? 'Collapse' : 'Verify Sources'}</span>
                <svg
                  className={`w-3.5 h-3.5 transition-transform duration-200 ${showCitations ? 'rotate-180' : ''}`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path d="M19 9l-7 7-7-7" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </div>
            </button>

            {showCitations && (
              <div className="mt-3 space-y-2 max-h-64 overflow-y-auto pr-1">
                {message.citations.map((citation, cIdx) => {
                  const urlMatch = citation.match(/(https?:\/\/[^\s]+)/);
                  const url = urlMatch ? urlMatch[0] : null;

                  return (
                    <div
                      key={cIdx}
                      className="p-3 rounded-xl bg-slate-950/90 border border-slate-800 text-xs text-slate-300 leading-relaxed font-mono"
                    >
                      <div className="flex items-start gap-2.5">
                        <span className="text-cyan-400 font-bold shrink-0">[{cIdx + 1}]</span>
                        <div className="flex-1 overflow-hidden break-words">
                          <p>{citation}</p>
                          {url && (
                            <a
                              href={url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="inline-flex items-center gap-1 mt-1.5 text-cyan-400 hover:text-cyan-300 underline text-[11px]"
                            >
                              <span>Inspect Grounded Source</span>
                              <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path
                                  d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
                                  strokeWidth="2"
                                  strokeLinecap="round"
                                  strokeLinejoin="round"
                                />
                              </svg>
                            </a>
                          )}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </div>
        )}

        {/* Attachments Section */}
        {message.attachments && message.attachments.length > 0 && (
          <div className="mt-6 pt-5 border-t border-white/5 flex flex-wrap gap-2">
            {message.attachments.map((file, idx) => (
              <div
                key={idx}
                className="flex items-center gap-3 px-4 py-2 bg-white/5 border border-white/10 rounded-2xl text-[10px] font-black text-slate-300 uppercase tracking-tight"
              >
                <svg className="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" strokeWidth="2.5" />
                </svg>
                {file.name}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
