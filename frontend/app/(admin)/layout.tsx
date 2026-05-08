"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Navbar from "@/components/Navbar";

interface AccountResponse {
  id: number;
  username: string;
  email: string;
  role_id: number;
  user_id: number;
  role: {
    id: number;
    name: string;
  };
  user: {
    first_name: string | null;
    last_name: string | null;
  };
}

export default function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const router = useRouter();
  const [isLoading, setIsLoading] = useState(true);
  const [isAuthorized, setIsAuthorized] = useState(false);
  // const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [account, setAccount] = useState<AccountResponse | null>(null);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8082/api/v1";

        const response = await fetch(`${API_BASE_URL}/account/me`, {
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (response.status === 401) {
          const errorData = await response.json().catch(() => null);
          setErrorMessage(`Unauthorized: ${errorData?.detail || "Please login first"}`);
          setIsAuthorized(false);
          setIsLoading(false);
          return;
        }

        if (response.ok) {
          const account: AccountResponse = await response.json();
          const roleName = account.role?.name;
          if (roleName === "Admin" || roleName === "SuperAdmin") {
            setIsAuthorized(true);
            setAccount(account);
          } else {
            setErrorMessage(`Access Denied: Your role is "${roleName}", but admin access requires "Admin" or "SuperAdmin"`);
            setIsAuthorized(false);
          }
        } else {
          const errorData = await response.json().catch(() => null);
          setErrorMessage(`Server error: ${response.status} - ${errorData?.detail || "Unknown error"}`);
          setIsAuthorized(false);
        }
        setIsLoading(false);
      } catch (error: any) {
        console.error("Auth check failed:", error);
        setErrorMessage(`Network error: ${error.message}\nMake sure backend is running on port 8082`);
        setIsAuthorized(false);
        setIsLoading(false);
      }
    };

    checkAuth();
  }, [router]);

  if (isLoading) {
    return (
      <div>
      </div>
    );
  }

  if (!isAuthorized) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center max-w-md mx-auto p-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Access Denied</h2>
        </div>
      </div>
    );
  }

  return (
    <>
      <Navbar account={account} />
      {children}
    </>
  );
}
