"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export default function RegisterPage() {
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    whatsapp: "",
    email: "",
    username: "",
    password: "",
    confirmPassword: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const router = useRouter();

  const BASE_URL = "http://localhost:8082/api/v1";

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const validateForm = () => {
    const {
      first_name,
      last_name,
      whatsapp,
      email,
      username,
      password,
      confirmPassword,
    } = formData;

    if (
      !first_name ||
      !last_name ||
      !whatsapp ||
      !email ||
      !username ||
      !password ||
      !confirmPassword
    ) {
      return "Please fill in all required fields.";
    }

    const emailRegex = /^\S+@\S+\.\S+$/;

    if (!emailRegex.test(email)) {
      return "Enter a valid email format.";
    }

    if (password.length < 8) {
      return "Password must be at least 8 characters.";
    }

    if (!/[A-Z]/.test(password)) {
      return "Password must contain at least one uppercase letter.";
    }

    if (password !== confirmPassword) {
      return "Password and confirm password do not match.";
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

      // CREATE USER
      const userResponse = await fetch(`${BASE_URL}/user/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          first_name: formData.first_name,
          last_name: formData.last_name,
          whatsapp: formData.whatsapp,
        }),
      });

      if (!userResponse.ok) {
        throw new Error("Failed to create user.");
      }

      const userData = await userResponse.json();

      const userId = userData.id;

      // CREATE ACCOUNT
      const accountResponse = await fetch(`${BASE_URL}/account/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: userId,
          role_id: 3,
          email: formData.email,
          username: formData.username,
          password: formData.password,
        }),
      });

      if (!accountResponse.ok) {
          const errorData = await accountResponse.text();
          console.log(errorData);
          throw new Error(errorData);
        }

      setSuccess("Register successful!");

      setFormData({
        first_name: "",
        last_name: "",
        whatsapp: "",
        email: "",
        username: "",
        password: "",
        confirmPassword: "",
      });

    } catch (err: any) {
      console.error(err);
      setError(err.message || "Registration failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-white flex items-center justify-center p-6">
      <div className="w-full max-w-6xl bg-white rounded-3xl shadow-2xl overflow-hidden grid grid-cols-1 md:grid-cols-2">

        {/* LEFT SIDE */}
        <div className="p-10 text-gray-800 bg-white">

          <h1 className="text-4xl font-bold text-[#004AC6] mb-2">
            EventPro
          </h1>

          <p className="text-gray-500 mb-6">
            Create your account to start managing world-class events.
          </p>

          {error && (
            <div className="bg-red-100 text-red-700 p-3 rounded-lg mb-4">
              {error}
            </div>
          )}

          {success && (
            <div className="bg-green-100 text-green-700 p-3 rounded-lg mb-4">
              {success}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">

            <div className="grid grid-cols-2 gap-4">

              <div>
                <label className="block mb-1 font-medium text-gray-700">
                  First Name
                </label>

                <input
                  type="text"
                  name="first_name"
                  value={formData.first_name}
                  onChange={handleChange}
                  placeholder="John"
                  className="w-full border border-gray-300 rounded-xl p-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
                />
              </div>

              <div>
                <label className="block mb-1 font-medium text-gray-700">
                  Last Name
                </label>

                <input
                  type="text"
                  name="last_name"
                  value={formData.last_name}
                  onChange={handleChange}
                  placeholder="Doe"
                  className="w-full border border-gray-300 rounded-xl p-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
                />
              </div>

            </div>

            <div>
              <label className="block mb-1 font-medium text-gray-700">
                WhatsApp Number
              </label>

              <input
                type="text"
                name="whatsapp"
                value={formData.whatsapp}
                onChange={handleChange}
                placeholder="08123456789"
                className="w-full border border-gray-300 rounded-xl p-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
              />
            </div>

            <div>
              <label className="block mb-1 font-medium text-gray-700">
                Email Address
              </label>

              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="john@example.com"
                className="w-full border border-gray-300 rounded-xl p-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
              />
            </div>

            <div>
              <label className="block mb-1 font-medium text-gray-700">
                Username
              </label>

              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                placeholder="johndoe88"
                className="w-full border border-gray-300 rounded-xl p-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
                />
            </div>

            <div className="grid grid-cols-2 gap-4">

              <div>
                <label className="block mb-1 font-medium text-gray-700">
                  Password
                </label>

                <input
                  type="password"
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  placeholder="********"
                  className="w-full border border-gray-300 rounded-xl p-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
                />
              </div>

              <div>
                <label className="block mb-1 font-medium text-gray-700">
                  Confirm Password
                </label>

                <input
                  type="password"
                  name="confirmPassword"
                  value={formData.confirmPassword}
                  onChange={handleChange}
                  placeholder="********"
                  className="w-full border border-gray-300 rounded-xl p-3 text-black bg-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#004AC6]"
                />
              </div>

            </div>

            <div className="bg-gray-100 rounded-xl p-4 text-sm">
              <p className="font-semibold mb-2 text-gray-800">
                Password Requirements:
              </p>

              <ul className="space-y-1 text-gray-600">
                <li>• At least 8 characters</li>
                <li>• One uppercase letter required</li>
              </ul>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-[#004AC6] hover:bg-blue-700 text-white py-3 rounded-xl font-semibold transition duration-200 shadow-lg"
            >
              {loading ? "Loading..." : "Create Account"}
            </button>

          </form>

          <p className="text-sm text-gray-500 text-center mt-6">
            Already have an account?{" "}
            <span
              className="text-[#004AC6] font-semibold cursor-pointer hover:underline"
              onClick={() => router.push("/login")}
            >
              Login now
            </span>
          </p>

        </div>

        {/* RIGHT SIDE */}
        <div className="hidden md:flex bg-[#004AC6] items-center justify-center p-10 text-white">

          <div className="text-center max-w-md">

            <h2 className="text-5xl font-bold mb-6 leading-tight">
              Empowering Organizers
            </h2>

            <p className="text-lg text-blue-100 leading-relaxed">
              Join thousands of professional event planners managing
              registrations, logistics, and attendee engagement seamlessly.
            </p>

          </div>

        </div>

      </div>
    </div>
  );
}