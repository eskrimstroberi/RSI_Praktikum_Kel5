"use client";
import React, { useState } from "react";
import { X } from "lucide-react";
import { Event, EventCreateInput, EventUpdateInput } from "@/types/event";

interface EventFormProps {
  event?: Event;
  onSubmit: (data: EventCreateInput | EventUpdateInput) => void;
  onCancel: () => void;
  isLoading?: boolean;
}

function toLocalDate(dateStr: string) {
  const d = new Date(dateStr);
  const pad = (n: number) => n.toString().padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

function toLocalTime(dateStr: string) {
  const d = new Date(dateStr);
  const pad = (n: number) => n.toString().padStart(2, '0');
  return `${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

const HOURS = Array.from({ length: 24 }, (_, i) => i.toString().padStart(2, '0'));
const MINUTES = Array.from({ length: 60 }, (_, i) => i.toString().padStart(2, '0'));

export default function EventForm({ event, onSubmit, onCancel, isLoading }: EventFormProps) {
  const isEdit = !!event;

  const [formData, setFormData] = useState({
    name: event?.name || "",
    description: event?.description || "",
    quota: event?.quota?.toString() || "",
    startDate: event?.started_at ? toLocalDate(event.started_at) : "",
    startTime: event?.started_at ? toLocalTime(event.started_at) : "00:00",
    endDate: event?.ended_at ? toLocalDate(event.ended_at) : "",
    endTime: event?.ended_at ? toLocalTime(event.ended_at) : "00:00",
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    const started_at = formData.startDate
      ? `${formData.startDate}T${formData.startTime}:00`
      : null;
    const ended_at = formData.endDate
      ? `${formData.endDate}T${formData.endTime}:00`
      : null;
    const data: EventCreateInput | EventUpdateInput = {
      name: formData.name,
      description: formData.description || null,
      quota: formData.quota ? parseInt(formData.quota) : null,
      started_at,
      ended_at,
    };
    onSubmit(data);
  };

  const field =
    "w-full px-3 py-1.5 text-sm border border-[#C3C6D7] rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-[#434655] placeholder-gray-400  bg-[#F3F3FE]";
  return (
    /* Backdrop */
    <div className="fixed inset-0 bg-black/40 flex items-center justify-center p-4 z-50">
      <div className="bg-[#FAF8FF] rounded-2xl shadow-2xl w-full max-w-lg">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-[#C3C6D7]">
          <h2 className="text-xl font-semibold text-[#191B23]">
            {isEdit ? "Edit Event" : "Add New Event"}
          </h2>
          <button
            onClick={onCancel}
            className="p-1 text-[#434655] hover:text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <form onSubmit={handleSubmit} className="px-6 py-5 space-y-4">
          {/* Row 1: Event Name */}
          <div>
            <label className="block text-sm text-[#434655] mb-1.5">Event Name</label>
            <input
              type="text"
              required
              placeholder="e.g. Annual Tech Summit"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              className={field}
            />
          </div>

          {/* Row 2: Description */}
          <div>
            <label className="block text-sm text-[#434655]  mb-1.5">Description</label>
            <textarea
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              className={field}
              rows={3}
            />
          </div>

          {/* Row 3: Quota */}
          <div>
            <label className="block text-sm text-[#434655]  mb-1.5">Quota</label>
            <input
              type="number"
              placeholder="500"
              value={formData.quota}
              onChange={(e) => setFormData({ ...formData, quota: e.target.value })}
              className={field}
            />
          </div>

          {/* Row 4: Start Date */}
          <div className="grid grid-cols-2 gap-6">
            <div>
              <label className="block text-sm text-[#434655]  mb-1.5">Start Date</label>
              <input
                type="date"
                value={formData.startDate}
                onChange={(e) => setFormData({ ...formData, startDate: e.target.value })}
                className={field}
              />
            </div>
            <div>
              <label className="block text-sm text-[#434655]  mb-1.5">Start Time</label>
              <div className="flex gap-1">
                <select
                  value={formData.startTime.split(':')[0]}
                  onChange={(e) =>
                    setFormData({ ...formData, startTime: `${e.target.value}:${formData.startTime.split(':')[1]}` })
                  }
                  className={field}
                >
                  {HOURS.map((h) => (
                    <option key={h} value={h}>{h}</option>
                  ))}
                </select>
                <span className="self-center text-gray-400 text-sm">:</span>
                <select
                  value={formData.startTime.split(':')[1]}
                  onChange={(e) =>
                    setFormData({ ...formData, startTime: `${formData.startTime.split(':')[0]}:${e.target.value}` })
                  }
                  className={field}
                >
                  {MINUTES.map((m) => (
                    <option key={m} value={m}>{m}</option>
                  ))}
                </select>
              </div>
            </div>
          </div>

          {/* Row 5: End Date */}
          <div className="grid grid-cols-2 gap-6">
            <div>
              <label className="block text-sm text-[#434655]  mb-1.5">End Date</label>
              <input
                type="date"
                value={formData.endDate}
                onChange={(e) => setFormData({ ...formData, endDate: e.target.value })}
                className={field}
              />
            </div>
            <div>
              <label className="block text-sm text-[#434655]  mb-1.5">End Time</label>
              <div className="flex gap-1">
                <select
                  value={formData.endTime.split(':')[0]}
                  onChange={(e) =>
                    setFormData({ ...formData, endTime: `${e.target.value}:${formData.endTime.split(':')[1]}` })
                  }
                  className={field}
                >
                  {HOURS.map((h) => (
                    <option key={h} value={h}>{h}</option>
                  ))}
                </select>
                <span className="self-center text-gray-400 text-sm">:</span>
                <select
                  value={formData.endTime.split(':')[1]}
                  onChange={(e) =>
                    setFormData({ ...formData, endTime: `${formData.endTime.split(':')[0]}:${e.target.value}` })
                  }
                  className={field}
                >
                  {MINUTES.map((m) => (
                    <option key={m} value={m}>{m}</option>
                  ))}
                </select>
              </div>
            </div>
          </div>

          {/* Footer Buttons */}
          <div className="flex items-center justify-end gap-2 pt-2">
            <button
              type="button"
              onClick={onCancel}
              disabled={isLoading}
              className="px-4 py-3 text-sm text-[#434655]  font-medium border border-[#737686] rounded-lg hover:bg-gray-50 transition-colors disabled:opacity-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={isLoading}
              className="px-4 py-3 text-sm text-white font-semibold bg-[#004AC6] rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50"
            >
              {isLoading ? "Saving..." : isEdit ? "Update Event" : "Add Event"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
