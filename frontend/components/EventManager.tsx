"use client";
import { useState, useEffect } from "react";
import { ChevronDown, Download } from "lucide-react";
import { Event } from "@/types/event";
import { eventApi } from "@/lib/api";
import EventTable from "@/components/EventTable";
import EventForm from "@/components/EventForm";
import DeleteConfirmDialog from "@/components/DeleteConfirmDialog";

type ModalMode = "create" | "edit" | "delete" | null;
type TabFilter = "All Events" | "Upcoming" | "Ongoing" | "Finished";
type SortOption = "Newest" | "Oldest" | "Name A-Z" | "Name Z-A";

const TABS: TabFilter[] = ["All Events", "Upcoming", "Ongoing", "Finished"];
const SORT_OPTIONS: SortOption[] = ["Newest", "Oldest", "Name A-Z", "Name Z-A"];
const EVENTS_PER_PAGE = 10;

function getEventStatus(event: Event): string {
  const now = new Date();
  const start = event.started_at ? new Date(event.started_at) : null;
  const end = event.ended_at ? new Date(event.ended_at) : null;
  if (end && now > end) return "Finished";
  if (start && now >= start) return "Ongoing";
  return "Upcoming";
}

export default function EventManager() {
  const [events, setEvents] = useState<Event[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [modalMode, setModalMode] = useState<ModalMode>(null);
  const [selectedEvent, setSelectedEvent] = useState<Event | undefined>();
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<TabFilter>("All Events");
  const [sortBy, setSortBy] = useState<SortOption>("Newest");
  const [showSortDropdown, setShowSortDropdown] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    loadEvents();
  }, []);

  const loadEvents = async () => {
    try {
      setIsLoading(true);
      const data = await eventApi.getAll();
      setEvents(data);
      setError(null);
    } catch (err: any) {
      setError(err.message || "Failed to load events");
    } finally {
      setIsLoading(false);
    }
  };

  const filtered = events.filter((e) => {
    if (activeTab === "All Events") return true;
    return getEventStatus(e) === activeTab;
  });

  const sorted = [...filtered].sort((a, b) => {
    if (sortBy === "Newest") return new Date(b.created_at ?? b.started_at ?? 0).getTime() - new Date(a.created_at ?? a.started_at ?? 0).getTime();
    if (sortBy === "Oldest") return new Date(a.created_at ?? a.started_at ?? 0).getTime() - new Date(b.created_at ?? b.started_at ?? 0).getTime();
    if (sortBy === "Name A-Z") return a.name.localeCompare(b.name);
    if (sortBy === "Name Z-A") return b.name.localeCompare(a.name);
    return 0;
  });

  const totalFiltered = sorted.length;
  const paginated = sorted.slice((currentPage - 1) * EVENTS_PER_PAGE, currentPage * EVENTS_PER_PAGE);

  const handleTabChange = (tab: TabFilter) => {
    setActiveTab(tab);
    setCurrentPage(1);
  };

  const handleCreate = () => {
    setSelectedEvent(undefined);
    setModalMode("create");
  };

  const handleEdit = (event: Event) => {
    setSelectedEvent(event);
    setModalMode("edit");
  };

  const handleDelete = (event: Event) => {
    setSelectedEvent(event);
    setModalMode("delete");
  };

  const handleSubmit = async (data: any) => {
    try {
      setIsSubmitting(true);
      if (modalMode === "create") {
        await eventApi.create(data);
      } else if (modalMode === "edit" && selectedEvent) {
        await eventApi.update(selectedEvent.id, data);
      }
      setModalMode(null);
      loadEvents();
    } catch (err: any) {
      setError(err.message || "Failed to save event");
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleConfirmDelete = async () => {
    if (!selectedEvent) return;
    try {
      setIsSubmitting(true);
      await eventApi.delete(selectedEvent.id);
      setModalMode(null);
      loadEvents();
    } catch (err: any) {
      setError(err.message || "Failed to delete event");
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleExportExcel = () => {
    console.log("Exporting to Excel...");
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <main className="flex-1 px-8 py-8 mx-auto w-full">
        <div className="flex items-start justify-between mb-6 w-full">
          <div className="w-full justify-around">
            <h1 className="text-3xl font-semibold text-gray-900">Event Management</h1>
            <div className="flex gap-4 w-full justify-between">
              <p className="text-sm font-light text-[#434655] mt-1">
                Oversee and manage all active, upcoming, and historical events across the EventPro platform.
              </p>
              <div className="flex flex-row gap-2">
                <button
                  onClick={handleExportExcel}
                  className="flex items-center gap-1.5 px-3 py-2 text-sm font-medium text-[#191B23] border border-gray-300 rounded-lg hover:bg-gray-50 bg-white transition-colors"
                >
                  <Download className="w-4 h-4" />
                  Export Excel
                </button>
                <button
                  onClick={handleCreate}
                  className="flex items-center gap-1 px-4 py-2 text-sm font-semibold text-white bg-[#004AC6] rounded-lg hover:bg-blue-700 transition-colors shadow-sm"
                >
                  + Add Event
                </button>
              </div>
            </div>
          </div>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-50 text-red-700 border border-red-200 rounded-lg text-sm">
            {error}
          </div>
        )}

        <div className="flex items-center justify-between rounded-xl bg-[#FAF8FF] border-1 border-[#C3C6D7] px-2.5 py-2 mb-4">
          <div className="flex items-center bg-[#F3F3FE] border-1 border-[#C3C6D7] rounded-lg p-0.5 gap-0.5">
            {TABS.map((tab) => (
              <button
                key={tab}
                onClick={() => handleTabChange(tab)}
                className={`px-4 py-1 rounded-md text-xs font-medium transition-colors ${activeTab === tab
                  ? "bg-white text-[#004AC6]  shadow-sm"
                  : "text-[#434655] hover:text-[#191B23]"
                  }`}
              >
                {tab}
              </button>
            ))}
          </div>

          <div className="relative">
            <button
              onClick={() => setShowSortDropdown(!showSortDropdown)}
              className="flex items-center gap-2 px-3 py-1 text-sm text-[#191B23] border border-gray-300 rounded-lg bg-[#F3F3FE] hover:bg-gray-50 transition-colors"
            >
              <span>Sort by: <span className="font-medium">{sortBy}</span></span>
              <ChevronDown className="w-4 h-4 text-gray-400" />
            </button>
            {showSortDropdown && (
              <div className="absolute right-0 top-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg z-20 min-w-[140px]">
                {SORT_OPTIONS.map((opt) => (
                  <button
                    key={opt}
                    onClick={() => {
                      setSortBy(opt);
                      setShowSortDropdown(false);
                      setCurrentPage(1);
                    }}
                    className={`w-full text-left px-4 py-2 text-sm transition-colors hover:bg-gray-50 ${sortBy === opt ? "text-[#004AC6] font-medium" : "text-[#191B23]"
                      }`}
                  >
                    {opt}
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>

        <EventTable
          events={paginated}
          onEdit={handleEdit}
          onDelete={handleDelete}
          isLoading={isLoading}
          currentPage={currentPage}
          totalEvents={totalFiltered}
          eventsPerPage={EVENTS_PER_PAGE}
          onPageChange={setCurrentPage}
        />
      </main>

      <footer className="border-t border-gray-200 bg-white px-8 py-4">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <span className="text-sm text-[#434655]">
            <span className="font-semibold text-[#191B23]">EventPro</span> &nbsp;|&nbsp; © 2024 EventPro SaaS. All rights reserved.
          </span>
          <div className="flex items-center gap-4 text-sm text-[#434655]">
            <a href="#" className="hover:text-gray-800 transition-colors">Privacy Policy</a>
            <a href="#" className="hover:text-gray-800 transition-colors">Terms of Service</a>
            <a href="#" className="hover:text-gray-800 transition-colors">Contact Us</a>
          </div>
        </div>
      </footer>

      {(modalMode === "create" || modalMode === "edit") && (
        <EventForm
          event={selectedEvent}
          onSubmit={handleSubmit}
          onCancel={() => setModalMode(null)}
          isLoading={isSubmitting}
        />
      )}

      {modalMode === "delete" && selectedEvent && (
        <DeleteConfirmDialog
          event={{ id: selectedEvent.id, name: selectedEvent.name }}
          onConfirm={handleConfirmDelete}
          onCancel={() => setModalMode(null)}
          isLoading={isSubmitting}
        />
      )}
    </div>
  );
}
