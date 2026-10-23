export type UserRole = 'advocate' | 'client';

export interface FileAttachment {
  name: string;
  type: string;
  data: string; // base64
}

export interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  attachments?: FileAttachment[];
  source?: 'local_rag' | 'gemini_fallback' | 'error';
  confidenceScore?: number;
  citations?: string[];
}

export interface Hearing {
  id: string;
  caseId?: string;
  title: string;
  date: string;
  time: string;
  court: string;
  details: string;
}

export interface CaseRegistry {
  id: string;
  caseNumber: string;
  cnrNumber?: string;
  petitioner: string;
  respondent: string;
  courtName: string;
  status: 'active' | 'disposed' | 'pending';
  lastHearingDate?: string;
  nextHearingDate?: string;
}

export interface CaseSession {
  id: string;
  caseId?: string; // Link to a registry entry
  title: string;
  messages: Message[];
  createdAt: Date;
  role: UserRole;
}
