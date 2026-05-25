export default function Topbar() {
  return (
    <div className="flex items-center justify-between border-b border-white/10 px-8 py-6">

      <div>
        <h1 className="text-3xl font-bold text-white">
          Security Dashboard
        </h1>

        <p className="mt-1 text-sm text-gray-400">
          Real-time genomic infrastructure monitoring
        </p>
      </div>

      <div className="flex items-center gap-3">

        <div className="rounded-full bg-green-500/20 px-4 py-2 text-sm text-green-400">
          System Secure
        </div>

      </div>

    </div>
  );
}