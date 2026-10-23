import React, { useState } from 'react';
import { Message } from '../types';

interface ChatBubbleProps {
  message: Message;
}

/**
 * Parses inline Markdown tokens:
 * - ***bold italic***
 * - **bold** or __bold__
 * - *italic* or _italic_
 * - `code`
 * - [text](url)
 * Prevents raw asterisks (**) from rendering on the screen.
 */
const formatInlineText = (text: string): React.ReactNode => {
  if (!text) return text;
  if (!text.includes('*') && !text.includes('`') && !text.includes('_') && !text.includes('[')) {
    return text;
  }

  // Tokenize bold-italic (***), bold (**), italic (*), code (`), links ([...](...))
  const tokens = text.split(/(\*\*\*.*?\*\*\*|\*\*.*?\*\*|__.*?__|`.*?`|\*.*?\*|_.*?_|\[.*?\]\(.*?\))/g);

  return tokens.map((token, idx) => {
    if (!token) return null;

    // Bold + Italic: ***text***
    if (token.startsWith('***') && token.endsWith('***') && token.length > 6) {
      return (
        <strong key={idx} className="font-bold italic text-cyan-200 tracking-wide">
          {token.slice(3, -3)}
        </strong>
      );
    }

    // Bold: **text** or __text__
    if (
      (token.startsWith('**') && token.endsWith('**') && token.length > 4) ||
      (token.startsWith('__') && token.endsWith('__') && token.length > 4)
    ) {
      return (
        <strong key={idx} className="font-bold text-white tracking-wide">
          {token.slice(2, -2)}
        </strong>
      );
    }

    // Inline Code: `text`
    if (token.startsWith('`') && token.endsWith('`') && token.length > 2) {
      return (
        <code
          key={idx}
          className="px-1.5 py-0.5 mx-0.5 rounded-md bg-slate-800 text-cyan-300 font-mono text-xs border border-cyan-500/20"
        >
          {token.slice(1, -1)}
        </code>
      );
    }

    // Italic: *text* or _text_
    if (
      (token.startsWith('*') && token.endsWith('*') && token.length > 2) ||
      (token.startsWith('_') && token.endsWith('_') && token.length > 2)
    ) {
      return (
        <em key={idx} className="italic text-slate-200">
          {token.slice(1, -1)}
        </em>
      );
    }

    // Markdown Link: [text](url)
    const linkMatch = token.match(/^\[(.*?)\]\((.*?)\)$/);
    if (linkMatch) {
      return (
        <a
          key={idx}
          href={linkMatch[2]}
          target="_blank"
          rel="noopener noreferrer"
          className="text-cyan-400 hover:text-cyan-300 underline underline-offset-2 decoration-cyan-500/40"
        >
          {linkMatch[1]}
        </a>
      );
    }

    return token;
  });
};

interface TableData {
  headers: string[];
  rows: string[][];
}

interface Block {
  type:
    | 'code'
    | 'table'
    | 'h1'
    | 'h2'
    | 'h3'
    | 'blockquote'
    | 'hr'
    | 'ordered_list'
    | 'unordered_list'
    | 'paragraph';
  data: any;
}

/**
 * Robust Markdown block parser:
 * Groups contiguous table rows into a SINGLE table component.
 * Filters out separator rows (|---|---|---|).
 * Groups list items and code blocks.
 */
const parseMarkdownBlocks = (content: string): Block[] => {
  const blocks: Block[] = [];
  const lines = content.replace(/\r\n/g, '\n').split('\n');
  let i = 0;

  const isTableRow = (lineStr: string) => {
    const t = lineStr.trim();
    return t.startsWith('|') && (t.endsWith('|') || t.split('|').length >= 3);
  };

  const isSeparatorRow = (lineStr: string) => {
    const trimmed = lineStr.trim().replace(/^\|/, '').replace(/\|$/, '');
    const cells = trimmed.split('|').map((c) => c.trim());
    return cells.length > 0 && cells.every((c) => /^[\s\-:]+$/.test(c));
  };

  const extractCells = (lineStr: string): string[] => {
    const trimmed = lineStr.trim().replace(/^\|/, '').replace(/\|$/, '');
    return trimmed.split('|').map((c) => c.trim());
  };

  while (i < lines.length) {
    const line = lines[i];
    const trimmed = line.trim();

    // 1. Empty lines
    if (!trimmed) {
      i++;
      continue;
    }

    // 2. Code Block
    if (trimmed.startsWith('```')) {
      const lang = trimmed.slice(3).trim();
      const codeLines: string[] = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      if (i < lines.length) i++; // consume closing ```
      blocks.push({
        type: 'code',
        data: { code: codeLines.join('\n'), lang },
      });
      continue;
    }

    // 3. Complete Markdown Table (Collect all contiguous table rows together)
    if (isTableRow(trimmed)) {
      const tableLines: string[] = [];
      while (i < lines.length && isTableRow(lines[i])) {
        tableLines.push(lines[i]);
        i++;
      }

      let headerCells: string[] = [];
      const dataRows: string[][] = [];
      let separatorPassed = false;

      for (let tIdx = 0; tIdx < tableLines.length; tIdx++) {
        const tLine = tableLines[tIdx];
        if (isSeparatorRow(tLine)) {
          separatorPassed = true;
          continue; // completely drop the separator row
        }

        const cells = extractCells(tLine);
        if (!separatorPassed && headerCells.length === 0) {
          headerCells = cells;
        } else {
          dataRows.push(cells);
        }
      }

      // If no explicit separator was found but multiple rows exist, row 0 is header
      if (!separatorPassed && tableLines.length > 1 && headerCells.length === 0) {
        headerCells = extractCells(tableLines[0]);
        for (let r = 1; r < tableLines.length; r++) {
          dataRows.push(extractCells(tableLines[r]));
        }
      }

      blocks.push({
        type: 'table',
        data: { headers: headerCells, rows: dataRows } as TableData,
      });
      continue;
    }

    // 4. Horizontal Rules
    if (trimmed === '---' || trimmed === '***' || trimmed === '___') {
      blocks.push({ type: 'hr', data: null });
      i++;
      continue;
    }

    // 5. Headings
    if (trimmed.startsWith('### ')) {
      blocks.push({ type: 'h3', data: trimmed.slice(4).trim() });
      i++;
      continue;
    }
    if (trimmed.startsWith('## ')) {
      blocks.push({ type: 'h2', data: trimmed.slice(3).trim() });
      i++;
      continue;
    }
    if (trimmed.startsWith('# ')) {
      blocks.push({ type: 'h1', data: trimmed.slice(2).trim() });
      i++;
      continue;
    }

    // 6. Blockquotes / Disclaimers
    if (trimmed.startsWith('>') || trimmed.startsWith('DISCLAIMER:')) {
      const quoteLines: string[] = [];
      while (
        i < lines.length &&
        (lines[i].trim().startsWith('>') || lines[i].trim().startsWith('DISCLAIMER:'))
      ) {
        quoteLines.push(
          lines[i]
            .trim()
            .replace(/^>\s*/, '')
            .replace(/^DISCLAIMER:\s*/i, '')
        );
        i++;
      }
      blocks.push({
        type: 'blockquote',
        data: quoteLines.join(' '),
      });
      continue;
    }

    // 7. Ordered List Items (e.g. 1. text)
    const orderedMatch = trimmed.match(/^(\d+)\.\s+(.*)$/);
    if (orderedMatch) {
      const items: { num: string; text: string }[] = [];
      while (i < lines.length) {
        const m = lines[i].trim().match(/^(\d+)\.\s+(.*)$/);
        if (m) {
          items.push({ num: m[1], text: m[2] });
          i++;
        } else {
          break;
        }
      }
      blocks.push({ type: 'ordered_list', data: items });
      continue;
    }

    // 8. Unordered List Items (- text, * text, • text)
    if (trimmed.startsWith('- ') || trimmed.startsWith('* ') || trimmed.startsWith('• ')) {
      const items: string[] = [];
      while (i < lines.length) {
        const lTrim = lines[i].trim();
        if (lTrim.startsWith('- ') || lTrim.startsWith('* ') || lTrim.startsWith('• ')) {
          items.push(lTrim.replace(/^[-*•]\s*/, ''));
          i++;
        } else {
          break;
        }
      }
      blocks.push({ type: 'unordered_list', data: items });
      continue;
    }

    // 9. Regular Paragraph
    const paraLines: string[] = [trimmed];
    i++;
    while (
      i < lines.length &&
      lines[i].trim() !== '' &&
      !lines[i].trim().startsWith('```') &&
      !isTableRow(lines[i]) &&
      !lines[i].trim().startsWith('#') &&
      !lines[i].trim().startsWith('>') &&
      !lines[i].trim().startsWith('DISCLAIMER:') &&
      !lines[i].trim().match(/^(\d+)\.\s+/) &&
      !lines[i].trim().startsWith('- ') &&
      !lines[i].trim().startsWith('* ') &&
      !lines[i].trim().startsWith('• ') &&
      lines[i].trim() !== '---'
    ) {
      paraLines.push(lines[i].trim());
      i++;
    }
    blocks.push({
      type: 'paragraph',
      data: paraLines.join('\n'),
    });
  }

  return blocks;
};

export const ChatBubble: React.FC<ChatBubbleProps> = ({ message }) => {
  const isUser = message.role === 'user';
  const [showCitations, setShowCitations] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleCopyMessage = () => {
    if (navigator.clipboard?.writeText) {
      navigator.clipboard
        .writeText(message.content)
        .then(() => {
          setCopied(true);
          setTimeout(() => setCopied(false), 2000);
        })
        .catch(() => {});
    }
  };

  const renderFormattedContent = (content: string) => {
    const blocks = parseMarkdownBlocks(content);

    return blocks.map((block, idx) => {
      // 1. Code Block
      if (block.type === 'code') {
        const { code } = block.data;
        return (
          <div key={idx} className="relative group my-4">
            <pre className="whitespace-pre-wrap bg-slate-950/90 p-4 rounded-xl border border-white/10 text-xs font-mono text-cyan-200 overflow-x-auto shadow-inner">
              {code}
            </pre>
            <button
              onClick={() => {
                if (navigator.clipboard?.writeText) {
                  navigator.clipboard.writeText(code).catch(() => {});
                }
              }}
              className="absolute top-3 right-3 bg-cyan-500/20 hover:bg-cyan-500 text-cyan-300 hover:text-white text-[10px] font-black px-2.5 py-1 rounded-lg transition-all opacity-0 group-hover:opacity-100 uppercase tracking-widest border border-cyan-500/30 shadow-md"
            >
              Copy Code
            </button>
          </div>
        );
      }

      // 2. High-Precision Legal Table
      if (block.type === 'table') {
        const { headers, rows } = block.data as TableData;
        return (
          <div
            key={idx}
            className="overflow-x-auto my-5 rounded-2xl border border-slate-700/80 bg-slate-950/70 shadow-2xl backdrop-blur-sm"
          >
            <table className="w-full text-left border-collapse text-[13px]">
              {headers && headers.length > 0 && (
                <thead>
                  <tr className="bg-slate-800/90 border-b border-cyan-500/30">
                    {headers.map((h, hIdx) => (
                      <th
                        key={hIdx}
                        className="py-3 px-4 font-bold text-cyan-300 text-xs uppercase tracking-wider border-r border-slate-700/40 last:border-r-0"
                      >
                        {formatInlineText(h)}
                      </th>
                    ))}
                  </tr>
                </thead>
              )}
              <tbody className="divide-y divide-slate-800/70">
                {rows.map((row, rIdx) => (
                  <tr
                    key={rIdx}
                    className="hover:bg-cyan-950/25 transition-colors odd:bg-slate-900/50 even:bg-slate-900/20"
                  >
                    {row.map((cell, cIdx) => (
                      <td
                        key={cIdx}
                        className={`py-3 px-4 text-slate-200 leading-relaxed border-r border-slate-800/40 last:border-r-0 ${
                          cIdx === 0 ? 'font-semibold text-white' : ''
                        }`}
                      >
                        {formatInlineText(cell)}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        );
      }

      // 3. Headings
      if (block.type === 'h3') {
        return (
          <h3
            key={idx}
            className="text-[15px] font-bold text-white mt-6 mb-3 flex items-center gap-2 border-b border-white/10 pb-1.5"
          >
            <span className="w-1.5 h-4 bg-gradient-to-b from-cyan-400 to-blue-500 rounded-full inline-block shrink-0 shadow-[0_0_8px_rgba(34,211,238,0.6)]"></span>
            <span className="text-cyan-100">{formatInlineText(block.data)}</span>
          </h3>
        );
      }
      if (block.type === 'h2') {
        return (
          <h2
            key={idx}
            className="text-[16px] font-extrabold text-cyan-300 mt-6 mb-3 flex items-center gap-2 pb-1.5 border-b border-cyan-500/20"
          >
            <span>{formatInlineText(block.data)}</span>
          </h2>
        );
      }
      if (block.type === 'h1') {
        return (
          <h1 key={idx} className="text-[18px] font-black text-white mt-6 mb-3">
            {formatInlineText(block.data)}
          </h1>
        );
      }

      // 4. Blockquotes / Disclaimers
      if (block.type === 'blockquote') {
        return (
          <div
            key={idx}
            className="my-4 p-3.5 rounded-xl bg-gradient-to-r from-amber-950/30 to-slate-900/80 border-l-4 border-l-amber-400 border border-amber-500/20 text-xs text-amber-200/90 flex items-start gap-3 shadow-md"
          >
            <svg
              className="w-4 h-4 text-amber-400 shrink-0 mt-0.5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            <div className="leading-relaxed font-medium">{formatInlineText(block.data)}</div>
          </div>
        );
      }

      // 5. Ordered Lists
      if (block.type === 'ordered_list') {
        const items = block.data as { num: string; text: string }[];
        return (
          <div key={idx} className="my-3 space-y-2">
            {items.map((item, itemIdx) => (
              <div key={itemIdx} className="flex items-start gap-3 ml-1">
                <span className="shrink-0 w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 text-[11px] font-bold flex items-center justify-center mt-0.5 shadow-sm">
                  {item.num}
                </span>
                <div className="text-[14px] text-slate-200 leading-relaxed flex-1">
                  {formatInlineText(item.text)}
                </div>
              </div>
            ))}
          </div>
        );
      }

      // 6. Unordered Lists
      if (block.type === 'unordered_list') {
        const items = block.data as string[];
        return (
          <div key={idx} className="my-2.5 space-y-1.5">
            {items.map((item, itemIdx) => (
              <div key={itemIdx} className="flex items-start gap-2.5 ml-2">
                <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 shrink-0 mt-2 shadow-[0_0_6px_rgba(34,211,238,0.8)]"></span>
                <div className="text-[14px] text-slate-200 leading-relaxed flex-1">
                  {formatInlineText(item)}
                </div>
              </div>
            ))}
          </div>
        );
      }

      // 7. Horizontal Rule
      if (block.type === 'hr') {
        return <hr key={idx} className="my-5 border-t border-slate-700/50" />;
      }

      // 8. Paragraph
      return (
        <p key={idx} className="mb-3 text-[14px] text-slate-200 leading-relaxed">
          {formatInlineText(block.data)}
        </p>
      );
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
        <div className="flex items-center justify-between mb-4 pb-2 border-b border-white/5">
          <div className="flex items-center gap-2 flex-wrap">
            <div
              className={`w-2 h-2 rounded-full ${isUser ? 'bg-fuchsia-400' : 'bg-cyan-400 animate-pulse'}`}
            ></div>
            <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
              {isUser ? 'You (Petitioner)' : 'S2 Legal AI Assistant'}
            </span>

            {/* Trust Badges */}
            {!isUser && message.source === 'local_rag' && (
              <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-950/70 text-emerald-400 border border-emerald-500/40 shadow-sm">
                <svg
                  className="w-3 h-3 text-emerald-400 shrink-0"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
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
                <svg
                  className="w-3 h-3 text-blue-400 shrink-0"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <circle cx="12" cy="12" r="10" strokeWidth="2.2" />
                  <path
                    d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
                    strokeWidth="2.2"
                  />
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
                  <svg
                    className="w-3.5 h-3.5 text-emerald-400"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      d="M5 13l4 4L19 7"
                      strokeWidth="2.5"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                  <span className="text-emerald-400">Copied</span>
                </>
              ) : (
                <>
                  <svg
                    className="w-3.5 h-3.5 text-slate-400"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2" strokeWidth="2" />
                    <path
                      d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                  <span>Copy</span>
                </>
              )}
            </button>
          )}
        </div>

        {/* Message Legal Content */}
        <div className="legal-content">
          {isUser ? (
            <p className="whitespace-pre-wrap leading-relaxed text-[15px]">{message.content}</p>
          ) : (
            renderFormattedContent(message.content)
          )}
        </div>

        {/* View Source Documents Collapsible Accordion */}
        {!isUser && message.citations && message.citations.length > 0 && (
          <div className="mt-5 pt-3 border-t border-slate-800/80">
            <button
              onClick={() => setShowCitations(!showCitations)}
              className="w-full flex items-center justify-between px-3.5 py-2 rounded-xl bg-slate-950/60 hover:bg-slate-950 border border-slate-800 transition-colors text-left group"
            >
              <div className="flex items-center gap-2">
                <svg
                  className="w-4 h-4 text-cyan-400 shrink-0"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
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
                  className={`w-3.5 h-3.5 transition-transform duration-200 ${
                    showCitations ? 'rotate-180' : ''
                  }`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    d="M19 9l-7 7-7-7"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
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
                <svg
                  className="w-3.5 h-3.5 text-cyan-400"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"
                    strokeWidth="2.5"
                  />
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
