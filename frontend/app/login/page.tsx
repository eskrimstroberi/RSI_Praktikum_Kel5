"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const [formData, setFormData] = useState({
    identifier: "",
    password: "",
    rememberMe: false,
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const router = useRouter();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;

    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const validateForm = () => {
    const { identifier, password } = formData;

    if (!identifier || !password) {
      return "Please fill in all required fields.";
    }

    return null;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    setError("");
    setSuccess("");

    const validationError = validateForm();

    if (validationError) {
      setError(validationError);
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/account/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: formData.identifier,
          password: formData.password,
        }),
      });

      const data = await response.json().catch(() => null);

      if (!response.ok) {
        setError(
          data?.detail ||
          data?.message ||
          "Invalid username or password."
        );
        return;
      }

      setSuccess("Login successful! Redirecting...");

      if (data?.token) {
        if (formData.rememberMe) {
          localStorage.setItem("token", data.token);
        } else {
          sessionStorage.setItem("token", data.token);
        }
      }

      setTimeout(() => {
        router.push("/");
      }, 1000);
    } catch (err) {
      console.error(err);
      setError("Login failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-white flex items-center justify-center p-6">
      <div className="w-full max-w-6xl bg-white rounded-3xl shadow-2xl overflow-hidden grid grid-cols-1 md:grid-cols-2">

        {/* LEFT SIDE - FORM */}
        <div className="p-10 text-gray-800 bg-white flex flex-col justify-center">

          <h1 className="text-3xl font-bold text-[#004AC6] mb-1 md:hidden">
            EventPro
          </h1>

          <h2 className="text-3xl font-bold text-gray-800 mb-1">
            Welcome back
          </h2>

          <p className="text-gray-500 mb-8">
            Please enter your details to sign in.
          </p>

          {error && (
            <div className="bg-red-100 text-red-700 p-3 rounded-lg mb-4 text-sm">
              {error}
            </div>
          )}

          {success && (
            <div className="bg-green-100 text-green-700 p-3 rounded-lg mb-4 text-sm">
              {success}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-5">

            <div>
              <label className="block mb-1 font-medium text-gray-700">
                Email or Username
              </label>

              <input
                type="text"
                name="identifier"
                value={formData.identifier}
                onChange={handleChange}
                placeholder="name@company.com"
                className="w-full border border-gray-300 rounded-xl px-4 py-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
              />
            </div>

            <div>
              <label className="block mb-1 font-medium text-gray-700">
                Password
              </label>

              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  placeholder="••••••••"
                  className="w-full border border-gray-300 rounded-xl px-4 py-3 pr-12 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
                />

                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-500"
                >
                  {showPassword ? "Hide" : "Show"}
                </button>
              </div>
            </div>

            <div className="flex items-center">
              <label className="flex items-center gap-2 cursor-pointer">
                <input
                  type="checkbox"
                  name="rememberMe"
                  checked={formData.rememberMe}
                  onChange={handleChange}
                  className="w-4 h-4 accent-[#004AC6]"
                />

                <span className="text-sm text-gray-600">
                  Remember me
                </span>
              </label>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-[#004AC6] hover:bg-blue-700 text-white py-3 rounded-xl font-semibold transition"
            >
              {loading ? "Signing in..." : "Login"}
            </button>

          </form>

          <p className="text-sm text-gray-500 text-center mt-8">
            Don't have an account?{" "}
            <span
              className="text-[#004AC6] font-semibold cursor-pointer hover:underline"
              onClick={() => router.push("/register")}
            >
              Register now
            </span>
          </p>
        </div>

        {/* RIGHT SIDE - BLUE PANEL */}
        <div className="hidden md:flex bg-[#004AC6] flex-col justify-between p-10 text-white">

          <div>
            <h1 className="text-2xl font-bold mb-16">EventPro</h1>

            <h2 className="text-5xl font-bold leading-tight mb-6">
              Elevate your event experience.
            </h2>

            <p className="text-blue-100 text-lg leading-relaxed">
              The management suite designed for clarity,
              high-performance orchestration,
              and professional reliability.
            </p>
          </div>

          <div className="grid grid-cols-2 gap-4 mt-10">
            {[
              "Real-time Analytics",
              "Secure Registration",
              "Attendee Insights",
              "Global Deployment",
            ].map((feature) => (
              <div
                key={feature}
                className="flex items-center gap-2 text-sm text-blue-100"
              >
                <div className="w-5 h-5 rounded-full border border-blue-300 flex items-center justify-center">
                  ✓
                </div>

                {feature}
              </div>
            ))}
          </div>

        </div>
      </div>
    </div>
  );
}
