export interface Event {
  id: number;
  name: string;
  description: string | null;
  quota: number | null;
  started_at: string | null;
  ended_at: string | null;
  created_at: string;
  updated_at: string;
}

export interface EventCreateInput {
  name: string;
  description?: string | null;
  quota?: number | null;
  started_at?: string | null;
  ended_at?: string | null;
}

export interface EventUpdateInput {
  name?: string;
  description?: string | null;
  quota?: number | null;
  started_at?: string | null;
  ended_at?: string | null;
}

export interface EventCreateInput {
  name: string;
  description?: string | null;
  quota?: number | null;
  started_at?: string | null;
  ended_at?: string | null;
}

export interface EventUpdateInput {
  name?: string;
  description?: string | null;
  quota?: number | null;
  started_at?: string | null;
  ended_at?: string | null;
}
