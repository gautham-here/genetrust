"use client";

import Link from "next/link";
import {
  LayoutDashboard,
  Upload,
  ShieldAlert,
  ClipboardList,
  Dna,
} from "lucide-react";

export default function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 z-50 flex h-screen w-72 flex-col border-r border-white/10 bg-black/70 backdrop-blur-xl">

      <div className="flex items-center gap-3 border-b border-white/10 px-6 py-6">
        <div className="rounded-xl bg-cyan-500/10 p-2">
          <Dna className="text-cyan-400" />
        </div>

        <div>
          <h1 className="text-xl font-bold text-white">
            GeneTrust
          </h1>

          <p className="text-xs text-gray-400">
            Genomic Security OS
          </p>
        </div>
      </div>

      <nav className="flex flex-col gap-2 px-4 py-6">

        <Link
          href="/dashboard"
          className="flex items-center gap-3 rounded-xl bg-cyan-500/10 px-4 py-3 text-cyan-300 transition hover:bg-cyan-500/20"
        >
          <LayoutDashboard size={18} />
          Dashboard
        </Link>

        <Link
          href="/upload"
          className="flex items-center gap-3 rounded-xl px-4 py-3 text-gray-300 transition hover:bg-white/10"
        >
          <Upload size={18} />
          Upload Genome
        </Link>

        <Link
          href="/risk-analysis"
          className="flex items-center gap-3 rounded-xl px-4 py-3 text-gray-300 transition hover:bg-white/10"
        >
          <ShieldAlert size={18} />
          Risk Analysis
        </Link>

        <Link
          href="/audit"
          className="flex items-center gap-3 rounded-xl px-4 py-3 text-gray-300 transition hover:bg-white/10"
        >
          <ClipboardList size={18} />
          Audit Logs
        </Link>

      </nav>
    </aside>
  );
}