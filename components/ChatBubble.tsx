import React, { useState } from 'react';
import { Message } from '../types';

interface ChatBubbleProps {
  message: Message;
}

/**
 * Parses inline Markdown tokens: **bold**, *italic*, `code` into styled React elements.
 * Prevents raw asterisks (**) from rendering on the screen.
 */
const formatInlineText = (text: string): React.ReactNode => {
  if (!text.includes('**') && !text.includes('*') && !text.includes('`') && !text.includes('__')) {
    return text;
  }

  const tokens = text.split(/(\*\*.*?\*\*|__.*?__|`.*?`|\*.*?\*)/g);

  return tokens.map((token, idx) => {
    if ((token.startsWith('**') && token.endsWith('**')) || (token.startsWith('__') && token.endsWith('__'))) {
      const inner = token.slice(2, -2);
      return (
        <strong key={idx} className="font-bold text-white tracking-wide">
          {inner}
        </strong>
      );
    }
    if (token.startsWith('`') && token.endsWith('`')) {
      const inner = token.slice(1, -1);
      return (
        <code
          key={idx}
          className="px-1.5 py-0.5 mx-0.5 rounded-md bg-slate-800 text-cyan-300 font-mono text-[12px] border border-cyan-500/20"
        >
          {inner}
        </code>
      );
    }
    if (token.startsWith('*') && token.endsWith('*') && token.length > 2) {
      const inner = token.slice(1, -1);
      return (
        <em key={idx} className="italic text-slate-200">
          {inner}
        </em>
      );
    }
    return token;
  });
};

export const ChatBubble: React.FC<ChatBubbleProps> = ({ message }) => {
  const isUser = message.role === 'user';
  const [showCitations, setShowCitations] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleCopyMessage = () => {
    if (navigator.clipboard?.writeText) {
      navigator.clipboard.writeText(message.content).then(() => {
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
      }).catch(() => {});
    }
  };

  const renderFormattedContent = (content: string) => {
    // Split into code blocks, tables, and standard prose blocks
    const parts = content.split(/(```[\s\S]*?```|\|[\s\S]*?\|\n)/g);

    return parts.map((part, index) => {
      // 1. Code Block Formatting
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

      // 2. Markdown Table Formatting with Inline Bold Support
      if (part.startsWith('|')) {
        const rows = part.trim().split('\n');
        const headerRow = rows[0].split('|').filter((c) => c.trim() !== '');
        const dataRows = rows.slice(2).map((r) => r.split('|').filter((c) => c.trim() !== ''));

        return (
          <div key={index} className="overflow-x-auto my-5 rounded-xl border border-slate-700/60 bg-slate-900/60 shadow-md">
            <table className="w-full text-left border-collapse text-xs">
              <thead>
                <tr className="border-b border-slate-700/80 bg-slate-800/80">
                  {headerRow.map((h, i) => (
                    <th key={i} className="p-3 font-bold text-cyan-300 uppercase tracking-wider">
                      {formatInlineText(h.trim())}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {dataRows.map((row, i) => (
                  <tr key={i} className="hover:bg-slate-800/40 transition-colors">
                    {row.map((cell, j) => (
                      <td key={j} className="p-3 text-slate-200 leading-relaxed">
                        {formatInlineText(cell.trim())}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        );
      }

      // 3. Line-by-Line Markdown Formatting
      return part.split('\n').map((line, i) => {
        const trimmed = line.trim();

        // Empty lines
        if (!trimmed) {
          return <div key={`${index}-${i}`} className="h-2" />;
        }

        // Horizontal rules
        if (trimmed === '---' || trimmed === '___' || trimmed === '***') {
          return <hr key={`${index}-${i}`} className="my-5 border-t border-slate-700/50" />;
        }

        // Major Headings (###)
        if (line.startsWith('###')) {
          const headerText = line.replace(/^###\s*/, '').trim();
          return (
            <h3
              key={`${index}-${i}`}
              className="text-[15px] font-bold text-white mt-5 mb-2.5 flex items-center gap-2 border-b border-white/5 pb-1"
            >
              <span className="w-1.5 h-4 bg-cyan-400 rounded-full inline-block shrink-0"></span>
              <span>{formatInlineText(headerText)}</span>
            </h3>
          );
        }

        // Section Headings (##)
        if (line.startsWith('##')) {
          const headerText = line.replace(/^##\s*/, '').trim();
          return (
            <h2
              key={`${index}-${i}`}
              className="text-[16px] font-extrabold text-cyan-300 mt-6 mb-3 flex items-center gap-2 pb-1 border-b border-cyan-500/20"
            >
              <span>{formatInlineText(headerText)}</span>
            </h2>
          );
        }

        // Top-Level Headings (#)
        if (line.startsWith('#')) {
          const headerText = line.replace(/^#\s*/, '').trim();
          return (
            <h1
              key={`${index}-${i}`}
              className="text-[18px] font-black text-white mt-6 mb-3"
            >
              {formatInlineText(headerText)}
            </h1>
          );
        }

        // Blockquotes or Disclaimer Callouts
        if (trimmed.startsWith('>') || trimmed.startsWith('DISCLAIMER:')) {
          const calloutText = trimmed.replace(/^>\s*/, '').trim();
          return (
            <div
              key={`${index}-${i}`}
              className="mt-4 mb-2 p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 text-xs text-slate-300 flex items-start gap-2.5 shadow-inner"
            >
              <svg className="w-4 h-4 text-cyan-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              <div className="leading-relaxed">{formatInlineText(calloutText)}</div>
            </div>
          );
        }

        // Numbered list items (e.g., "1. **Deception**: ...")
        const numberedMatch = trimmed.match(/^(\d+)\.\s+(.*)$/);
        if (numberedMatch) {
          const num = numberedMatch[1];
          const rest = numberedMatch[2];
          return (
            <div key={`${index}-${i}`} className="flex items-start gap-2.5 my-2 ml-1">
              <span className="shrink-0 w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 text-[11px] font-bold flex items-center justify-center mt-0.5">
                {num}
              </span>
              <div className="text-[14px] text-slate-200 leading-relaxed flex-1">
                {formatInlineText(rest)}
              </div>
            </div>
          );
        }

        // Bullet list items (e.g., "- ...", "* ...", "• ...")
        if (trimmed.startsWith('- ') || trimmed.startsWith('* ') || trimmed.startsWith('• ')) {
          const bulletText = trimmed.replace(/^[-*•]\s*/, '');
          return (
            <div key={`${index}-${i}`} className="flex items-start gap-2.5 my-1.5 ml-2">
              <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 shrink-0 mt-2"></span>
              <div className="text-[14px] text-slate-200 leading-relaxed flex-1">
                {formatInlineText(bulletText)}
              </div>
            </div>
          );
        }

        // Regular Paragraph
        return (
          <p key={`${index}-${i}`} className="mb-3 text-[14px] text-slate-200 leading-relaxed">
            {formatInlineText(line)}
          </p>
        );
      });
    });
  };

  return (
    <div className={`flex w-full mb-8 ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`relative max-w-[94%] md:max-w-[85%] p-6 transition-all shadow-xl ${
          isUser
            ? 'bg-gradient-to-br from-indigo-600 to-fuchsia-700 text-white rounded-3xl rounded-tr-sm shadow-[0_10px_30px_rgba(79,70,229,0.25)]'
            : 'bg-slate-900/90 border border-slate-800/90 text-slate-100 rounded-3xl rounded-tl-sm border-l-4 border-l-cyan-500'
        }`}
      >
        {/* Stream / Origin Header & Quick Actions */}
        <div className={`flex items-center justify-between mb-4 pb-2 border-b border-white/5`}>
          <div className="flex items-center gap-2 flex-wrap">
            <div className={`w-2 h-2 rounded-full ${isUser ? 'bg-fuchsia-400' : 'bg-cyan-400 animate-pulse'}`}></div>
            <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
              {isUser ? 'You (Petitioner)' : 'S2 Legal AI Assistant'}
            </span>

            {/* Trust Badges */}
            {!isUser && message.source === 'local_rag' && (
              <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-950/70 text-emerald-400 border border-emerald-500/40 shadow-sm">
                <svg className="w-3 h-3 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2" strokeWidth="2.5" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" strokeWidth="2.5" strokeLinecap="round" />
                </svg>
                <span>Local RAG (Verified Context)</span>
                {typeof message.confidenceScore === 'number' && (
                  <span className="ml-0.5 px-1.5 py-0.2 rounded bg-emerald-900/70 text-emerald-200 text-[10px] font-mono">
                    {(message.confidenceScore * 100).toFixed(0)}%
                  </span>
                )}
              </span>
            )}

            {!isUser && message.source === 'gemini_fallback' && (
              <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-blue-950/70 text-blue-400 border border-blue-500/40 shadow-sm">
                <svg className="w-3 h-3 text-blue-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <circle cx="12" cy="12" r="10" strokeWidth="2.2" />
                  <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" strokeWidth="2.2" />
                </svg>
                <span>Cloud Agent (Search Grounded)</span>
                {typeof message.confidenceScore === 'number' && (
                  <span className="ml-0.5 px-1.5 py-0.2 rounded bg-blue-900/70 text-blue-200 text-[10px] font-mono">
                    {(message.confidenceScore * 100).toFixed(0)}%
                  </span>
                )}
              </span>
            )}
          </div>

          {/* Copy Response Button */}
          {!isUser && (
            <button
              onClick={handleCopyMessage}
              className="flex items-center gap-1 px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-700/80 text-slate-300 hover:text-white text-[11px] font-medium transition-colors border border-slate-700/60"
              title="Copy message text"
            >
              {copied ? (
                <>
                  <svg className="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path d="M5 13l4 4L19 7" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                  <span className="text-emerald-400">Copied</span>
                </>
              ) : (
                <>
                  <svg className="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2" strokeWidth="2" />
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                  <span>Copy</span>
                </>
              )}
            </button>
          )}
        </div>

        {/* Message Legal Content */}
        <div className="legal-content">
          {isUser ? <p className="whitespace-pre-wrap leading-relaxed text-[15px]">{message.content}</p> : renderFormattedContent(message.content)}
        </div>

        {/* View Source Documents Collapsible Accordion */}
        {!isUser && message.citations && message.citations.length > 0 && (
          <div className="mt-5 pt-3 border-t border-slate-800/80">
            <button
              onClick={() => setShowCitations(!showCitations)}
              className="w-full flex items-center justify-between px-3.5 py-2 rounded-xl bg-slate-950/60 hover:bg-slate-950 border border-slate-800 transition-colors text-left group"
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
                <span className="text-xs font-semibold text-slate-300">
                  Verified Legal Sources & Context
                </span>
                <span className="px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 text-[10px] font-bold border border-cyan-500/30">
                  {message.citations.length}
                </span>
              </div>

              <div className="flex items-center gap-1.5 text-[11px] font-medium text-slate-400 group-hover:text-cyan-300">
                <span>{showCitations ? 'Hide Sources' : 'View Sources'}</span>
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
              <div className="mt-2.5 space-y-2 max-h-72 overflow-y-auto pr-1">
                {message.citations.map((citation, cIdx) => (
                  <pre
                    key={cIdx}
                    className="whitespace-pre-wrap bg-slate-950/90 border border-slate-800 text-slate-300 text-xs font-mono p-3 rounded-lg leading-relaxed overflow-x-auto"
                  >
                    {citation}
                  </pre>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Attachments Section */}
        {message.attachments && message.attachments.length > 0 && (
          <div className="mt-4 pt-3 border-t border-white/5 flex flex-wrap gap-2">
            {message.attachments.map((file, idx) => (
              <div
                key={idx}
                className="flex items-center gap-2 px-3 py-1.5 bg-slate-800/60 border border-slate-700/60 rounded-xl text-xs text-slate-300"
              >
                <svg className="w-3.5 h-3.5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
