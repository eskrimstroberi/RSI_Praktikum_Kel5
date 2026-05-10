"use client";

import { useState, useEffect } from "react";

const BASE_URL = "http://localhost:8082/api/v1";

interface Event {
    id: number;
    name: string;
    description: string | null;
    quota: number | null;
    started_at: string | null;
    ended_at: string | null;
}

type Status = "idle" | "loading" | "success" | "error";

function formatDate(dateStr: string | null) {
    if (!dateStr) return "-";
    return new Date(dateStr).toLocaleString("id-ID", {
        day: "2-digit",
        month: "long",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    });
}

export default function EventRegisterPage() {
    const [events, setEvents] = useState<Event[]>([]);
    const [eventsLoading, setEventsLoading] = useState(true);
    const [eventsError, setEventsError] = useState("");

    const [selectedEventId, setSelectedEventId] = useState<number | null>(null);
    const [userId, setUserId] = useState("");

    const [status, setStatus] = useState<Status>("idle");
    const [errorMsg, setErrorMsg] = useState("");
    const [successMsg, setSuccessMsg] = useState("");

    // Fetch all events on mount
    useEffect(() => {
        const fetchEvents = async () => {
            setEventsLoading(true);
            setEventsError("");
            try {
                const res = await fetch(`${BASE_URL}/event/`);
                if (!res.ok) {
                    const errData = await res.json().catch(() => ({}));
                    throw new Error(errData?.detail || "Gagal memuat daftar event.");
                }
                const data = await res.json();
                setEvents(data);
            } catch (err: unknown) {
                const errorMsg = err instanceof Error ? err.message : "Gagal memuat daftar event. Periksa koneksi ke backend.";
                setEventsError(errorMsg);
            } finally {
                setEventsLoading(false);
            }
        };
        fetchEvents();
    }, []);

    const selectedEvent = events.find((e) => e.id === selectedEventId) ?? null;

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setErrorMsg("");
        setSuccessMsg("");

        if (!selectedEventId) {
            setErrorMsg("Silakan pilih event terlebih dahulu.");
            return;
        }
        if (!userId.trim()) {
            setErrorMsg("User ID wajib diisi.");
            return;
        }
        if (isNaN(Number(userId)) || Number(userId) <= 0) {
            setErrorMsg("User ID harus berupa angka positif.");
            return;
        }

        setStatus("loading");
        try {
            const res = await fetch(`${BASE_URL}/registration/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    user_id: Number(userId),
                    event_id: selectedEventId,
                }),
            });
            if (!res.ok) {
                const errData = await res.json().catch(() => ({}));
                throw new Error(errData?.detail || "Pendaftaran gagal.");
            }
            setStatus("success");
            setSuccessMsg(
                `Berhasil mendaftar ke event "${selectedEvent?.name}"! Kami akan menghubungi Anda melalui WhatsApp.`
            );
            setUserId("");
            setSelectedEventId(null);
        } catch (err: unknown) {
            setStatus("error");
            const errorMessage = err instanceof Error ? err.message : "Pendaftaran gagal. Silakan coba lagi nanti.";
            setErrorMsg(errorMessage);
        }
    };

    return (
        <div className="min-h-screen bg-white flex items-center justify-center p-6">
            <div className="w-full max-w-6xl bg-white rounded-3xl shadow-2xl overflow-hidden grid grid-cols-1 md:grid-cols-2 min-h-[600px]">

                {/* LEFT SIDE: Form & Status */}
                <div className="p-10 text-gray-800 bg-white flex flex-col justify-center">

                    <h1 className="text-4xl font-bold text-[#004AC6] mb-2">
                        Event Registration
                    </h1>

                    <p className="text-gray-500 mb-6">
                        Register for your favorite event and secure your spot today.
                    </p>

                    {status === "success" && (
                        <div className="bg-green-100 text-green-700 p-3 rounded-lg mb-4">
                            {successMsg}
                        </div>
                    )}

                    {(errorMsg || status === "error") && (
                        <div className="bg-red-100 text-red-700 p-3 rounded-lg mb-4">
                            {errorMsg}
                        </div>
                    )}

                    <form onSubmit={handleSubmit} className="space-y-4">

                        <div>
                            <label className="block mb-1 font-medium text-gray-700">
                                User ID
                            </label>
                            <input
                                id="user-id-input"
                                type="number"
                                min="1"
                                value={userId}
                                onChange={(e) => {
                                    setUserId(e.target.value);
                                    setErrorMsg("");
                                    setStatus("idle");
                                }}
                                placeholder="Enter your User ID"
                                className="w-full border border-gray-300 rounded-xl p-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
                            />
                            <p className="text-xs text-gray-500 mt-1">
                                You receive this after account registration.
                            </p>
                        </div>

                        <div>
                            <label className="block mb-1 font-medium text-gray-700">
                                Selected Event
                            </label>
                            <div
                                className={`w-full border rounded-xl p-3 text-black ${selectedEvent
                                    ? "border-blue-400 bg-blue-50"
                                    : "border-gray-300 bg-gray-50 text-gray-400 italic"
                                    }`}
                            >
                                {selectedEvent
                                    ? `#${selectedEvent.id} — ${selectedEvent.name}`
                                    : "Please select an event from the right panel"}
                            </div>
                        </div>

                        <button
                            id="submit-register-btn"
                            type="submit"
                            disabled={status === "loading"}
                            className="w-full bg-[#004AC6] hover:bg-blue-700 text-white py-3 rounded-xl font-semibold transition duration-200 shadow-lg mt-4 flex justify-center items-center gap-2"
                        >
                            {status === "loading" ? "Processing..." : "Register Now"}
                        </button>

                    </form>

                    <p className="text-sm text-gray-500 text-center mt-6">
                        Don&apos;t have an account?{" "}
                        <a href="/register" className="text-[#004AC6] font-semibold cursor-pointer hover:underline">
                            Create one
                        </a>
                    </p>

                </div>

                {/* RIGHT SIDE: Event List */}
                <div className="bg-[#004AC6] p-10 text-white flex flex-col max-h-[700px]">

                    <div className="mb-6">
                        <h2 className="text-3xl font-bold mb-2">
                            Available Events
                        </h2>
                        <p className="text-blue-100 text-sm">
                            Select an event to register
                        </p>
                    </div>

                    {eventsLoading && (
                        <div className="flex flex-col gap-3">
                            {[1, 2, 3].map((i) => (
                                <div
                                    key={i}
                                    className="h-20 rounded-xl bg-white/20 animate-pulse"
                                ></div>
                            ))}
                        </div>
                    )}

                    {!eventsLoading && eventsError && (
                        <div className="bg-red-500/20 text-white rounded-xl p-4 text-sm">
                            ⚠️ {eventsError}
                        </div>
                    )}

                    {!eventsLoading && !eventsError && events.length === 0 && (
                        <div className="text-center py-12 text-blue-200">
                            <p>No events available at the moment.</p>
                        </div>
                    )}

                    {!eventsLoading && !eventsError && events.length > 0 && (
                        <div className="flex flex-col gap-3 overflow-y-auto pr-2">
                            {events.map((event) => {
                                const isSelected = selectedEventId === event.id;
                                return (
                                    <button
                                        key={event.id}
                                        type="button"
                                        onClick={() => setSelectedEventId(event.id)}
                                        className={`w-full text-left p-4 rounded-xl border transition-all duration-200 cursor-pointer ${isSelected
                                            ? "bg-white text-[#004AC6] border-white shadow-lg"
                                            : "bg-blue-700/50 border-blue-500 hover:bg-blue-600 hover:border-blue-400 text-white"
                                            }`}
                                    >
                                        <div className="flex items-start justify-between gap-2">
                                            <div className="flex-1 min-w-0">
                                                <p className="font-bold text-base truncate mb-1">
                                                    {event.name}
                                                </p>
                                                {event.description && (
                                                    <p className={`text-xs mt-0.5 line-clamp-2 ${isSelected ? "text-gray-600" : "text-blue-100"}`}>
                                                        {event.description}
                                                    </p>
                                                )}
                                                <div className="flex items-center gap-4 mt-3">
                                                    {event.started_at && (
                                                        <span className={`text-xs font-medium ${isSelected ? "text-gray-500" : "text-blue-200"}`}>
                                                            🗓 {formatDate(event.started_at)}
                                                        </span>
                                                    )}
                                                    {event.quota !== null && (
                                                        <span className={`text-xs font-medium ${isSelected ? "text-green-600" : "text-green-300"}`}>
                                                            👥 Quota: {event.quota}
                                                        </span>
                                                    )}
                                                </div>
                                            </div>
                                        </div>
                                    </button>
                                );
                            })}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
