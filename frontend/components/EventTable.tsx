"use client";
import { Eye, Pencil, Trash2 } from "lucide-react";
import { Event } from "@/types/event";

interface EventTableProps {
  events: Event[];
  onView?: (event: Event) => void;
  onEdit: (event: Event) => void;
  onDelete: (event: Event) => void;
  isLoading?: boolean;
  currentPage?: number;
  totalEvents?: number;
  eventsPerPage?: number;
  onPageChange?: (page: number) => void;
}

const EVENT_ICONS: { emoji: string; bg: string }[] = [
  { emoji: "🚀", bg: "bg-blue-100" },
  { emoji: "🎨", bg: "bg-purple-100" },
  { emoji: "☕", bg: "bg-orange-100" },
  { emoji: "⚡", bg: "bg-yellow-100" },
  { emoji: "🌐", bg: "bg-green-100" },
];

function getEventIcon(id: number) {
  return EVENT_ICONS[id % EVENT_ICONS.length];
}

function getStatus(event: Event): "Upcoming" | "Ongoing" | "Finished" {
  const now = new Date();
  const start = event.started_at ? new Date(event.started_at) : null;
  const end = event.ended_at ? new Date(event.ended_at) : null;
  if (end && now > end) return "Finished";
  if (start && now >= start) return "Ongoing";
  return "Upcoming";
}

function StatusBadge({ status }: { status: string }) {
  const styles: Record<string, string> = {
    Upcoming: "bg-[#DCFCE7] text-[#15803D]",
    Ongoing: "bg-[#DBEAFE] text-[#1D4ED8]",
    Finished: "bg-[#E1E2ED] text-[#434655]",
  };
  return (
    <span className={`px-3 py-1 rounded-full text-xs font-semibold ${styles[status] || "bg-gray-100 text-[#434655]"}`}>
      {status}
    </span>
  );
}

function formatDuration(started_at: string | null, ended_at: string | null): string {
  if (!started_at) return "-";
  const fmt = (d: string) =>
    new Date(d).toLocaleDateString("en-US", { month: "short", day: "2-digit", year: "numeric" });
  if (!ended_at) return fmt(started_at);
  return `${fmt(started_at)} - ${fmt(ended_at)}`;
}

export default function EventTable({
  events,
  onView,
  onEdit,
  onDelete,
  isLoading,
  currentPage = 1,
  totalEvents = 0,
  eventsPerPage = 10,
  onPageChange,
}: EventTableProps) {
  const totalPages = Math.max(1, Math.ceil(totalEvents / eventsPerPage));
  const startItem = (currentPage - 1) * eventsPerPage + 1;
  const endItem = Math.min(currentPage * eventsPerPage, totalEvents);

  if (isLoading) {
    return (
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-12 text-center text-gray-400 text-sm">
        Loading events...
      </div>
    );
  }

  if (events.length === 0) {
    return (
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-12 text-center text-gray-400 text-sm">
        No events found.
      </div>
    );
  }

  const pages: (number | "...")[] = [];
  if (totalPages <= 5) {
    for (let i = 1; i <= totalPages; i++) pages.push(i);
  } else {
    pages.push(1, 2, 3);
    if (currentPage > 4) pages.push("...");
    if (currentPage > 3 && currentPage < totalPages - 1) pages.push(currentPage);
    if (currentPage < totalPages - 2) pages.push("...");
    pages.push(totalPages);
  }

  return (
    <div className="bg-white rounded-xl  border border-[#C3C6D7] overflow-hidden">
      <table className="w-full ">
        <thead>
          <tr className="border-b bg-[#F3F3FE] border-[#C3C6D7]">
            <th className="px-6 py-5 text-left text-sm font-extrabold text-[#434655] uppercase tracking-wider">Event Name</th>
            <th className="px-6 py-3 text-left text-sm font-extrabold text-[#434655] uppercase tracking-wider">Quota</th>
            <th className="px-6 py-3 text-left text-sm font-extrabold text-[#434655] uppercase tracking-wider">Duration</th>
            <th className="px-6 py-3 text-left text-sm font-extrabold text-[#434655] uppercase tracking-wider">Status</th>
            <th className="px-6 py-3 text-right text-sm font-extrabold text-[#434655] uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100">
          {events.map((event) => {
            const icon = getEventIcon(event.id);
            const status = getStatus(event);

            return (
              <tr key={event.id} className="hover:bg-gray-50 transition-colors">
                {/* Event Name */}
                <td className="px-5 py-5">
                  <div className="flex items-center gap-3">
                    <div className={`w-9 h-9 rounded-lg ${icon.bg} flex items-center justify-center text-lg flex-shrink-0`}>
                      {icon.emoji}
                    </div>
                    <div>
                      <div className="text-sm font-bold text-[#191B23]">{event.name}</div>
                      {event.description && (
                        <div className="text-xs text-[#434655] mt-0.5 max-w-xs truncate">{event.description}</div>
                      )}
                    </div>
                  </div>
                </td>

                {/* Quota */}
                <td className="px-6 py-4 text-sm text-[#191B23]">{event.quota ?? "-"}</td>

                {/* Duration */}
                <td className="px-6 py-4 text-sm text-[#191B23] whitespace-nowrap">
                  {formatDuration(event.started_at, event.ended_at)}
                </td>

                {/* Status */}
                <td className="px-6 py-4">
                  <StatusBadge status={status} />
                </td>

                {/* Actions */}
                <td className="px-6 py-4">
                  <div className="flex items-center justify-end gap-2">
                    <button
                      onClick={() => onView?.(event)}
                      className="p-1.5 text-[#434655] hover:text-[#434655] hover:bg-gray-100 rounded-lg transition-colors"
                      title="View"
                    >
                      <Eye className="w-4 h-4" />
                    </button>
                    <button
                      onClick={() => onEdit(event)}
                      className="p-1.5 text-[#004AC6] hover:text-[#004AC6] hover:bg-blue-50 rounded-lg transition-colors"
                      title="Edit"
                    >
                      <Pencil className="w-4 h-4" />
                    </button>
                    <button
                      onClick={() => onDelete(event)}
                      className="p-1.5 text-[#BA1A1A] hover:text-[#BA1A1A] hover:bg-red-50 rounded-lg transition-colors"
                      title="Delete"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>

      {/* Footer: Showing X-Y of Z + Pagination */}
      <div className="px-6 py-5 border-t border-[#C3C6D7] flex items-center justify-between">
        <span className="text-xs text-[#434655]">
          Showing {startItem} - {endItem} of {totalEvents} events
        </span>
        <div className="flex items-center gap-1">
          <button
            onClick={() => onPageChange?.(currentPage - 1)}
            disabled={currentPage === 1}
            className="w-4 h-6 flex items-center justify-center rounded-xl border text-[#434655] hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed text-xl"
          >
            ‹
          </button>
          {pages.map((p, i) =>
            p === "..." ? (
              <span key={`ellipsis-${i}`} className="w-7 h-7 flex items-center justify-center text-gray-400 text-sm">
                ...
              </span>
            ) : (
              <button
                key={p}
                onClick={() => onPageChange?.(p as number)}
                className={`w-7 h-7 flex items-center justify-center rounded-lg text-xs font-medium transition-colors ${currentPage === p
                  ? "bg-[#004AC6] text-white"
                  : "text-[#191B23] hover:bg-gray-100"
                  }`}
              >
                {p}
              </button>
            )
          )}
          <button
            onClick={() => onPageChange?.(currentPage + 1)}
            disabled={currentPage === totalPages}
            className="w-4 h-6 flex items-center justify-center rounded-xl border text-[#434655] hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed text-xl"
          >
            ›
          </button>
        </div>
      </div>
    </div>
  );
}
