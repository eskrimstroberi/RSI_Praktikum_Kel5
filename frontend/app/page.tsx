export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-zinc-50 dark:bg-black font-sans">
      <main className="flex flex-col items-center justify-center gap-6 text-center px-6">

        <h1 className="text-4xl font-bold text-black dark:text-white">
          Website Praktikum RSI Kelompok 5 🚀
        </h1>

        <p className="text-lg text-zinc-600 dark:text-zinc-400 max-w-xl">
          Ini adalah halaman homepage yang dibuat menggunakan Next.js sebagai bagian dari pengembangan frontend sistem praktikum Rekayasa Sistem Informasi.
        </p>

        <button className="px-6 py-3 rounded-full bg-black text-white hover:bg-zinc-800 dark:bg-white dark:text-black dark:hover:bg-zinc-300 transition">
          Mulai Sekarang
        </button>

      </main>
    </div>
  );
}