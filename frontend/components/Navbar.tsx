"use client";
import { Bell, Settings, Search } from "lucide-react";

interface NavbarProps {
  account?: {
    user: {
      first_name: string | null;
      last_name: string | null;
    } | null;
  } | null;
}

export default function Navbar({ account }: NavbarProps) {
  return (
    <nav className="bg-white border-b border-gray-200 px-6 py-3 flex items-center justify-between sticky top-0 z-40">
      {/* Left: Logo + Nav Links */}
      <div className="flex items-center gap-8">
        <span className="text-[#004AC6] font-bold text-lg tracking-tight">EventPro</span>
        <div className="flex items-center gap-6">
          <a href="#" className="text-sm text-[#434655] hover:text-gray-800 transition-colors">Dashboard</a>
          <a href="#" className="text-sm text-[#004AC6] font-semibold border-b-2 border-blue-600 pb-0.5">Events</a>
          <a href="#" className="text-sm text-[#434655] hover:text-gray-800 transition-colors">Logs</a>
        </div>
      </div>

      {/* Right: Search + Icons + User */}
      <div className="flex items-center gap-3">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-4 h-4" />
          <input
            type="text"
            placeholder="Search events..."
            className="pl-9 pr-4 py-1.5 text-sm bg-gray-50 border border-gray-200 rounded-lg w-52 focus:outline-none focus:ring-2 focus:ring-blue-500 text-[#191B23] placeholder-gray-400"
          />
        </div>
        <button className="p-1.5 text-[#434655] hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-colors">
          <Bell className="w-5 h-5" />
        </button>
        <button className="p-1.5 text-[#434655] hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-colors">
          <Settings className="w-5 h-5" />
        </button>
        <div className="flex items-center gap-2 ml-1">
          <span className="text-sm text-[#191B23] font-medium">
            {account?.user?.first_name && account?.user?.last_name
              ? `${account.user.first_name} ${account.user.last_name}`
              : "Admin User"}
          </span>
          <div className="w-5 h-5 rounded-full bg-gray-800 flex items-center justify-center text-white text-xs font-bold">
            {account?.user?.first_name && account?.user?.last_name
              ? `${account.user.first_name[0]}${account.user.last_name[0]}`
              : "AU"}
          </div>
        </div>
      </div>
    </nav>
  );
}
