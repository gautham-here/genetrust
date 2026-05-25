"use client";

import Sidebar from "@/components/Sidebar";
import Topbar from "@/components/Topbar";

import {
  ShieldAlert,
  Dna,
  ScanSearch,
  AlertTriangle,
  ShieldCheck,
} from "lucide-react";

import { motion } from "framer-motion";

export default function RiskAnalysisPage() {
  return (
    <main className="min-h-screen bg-black text-white">

      <Sidebar />

      <div className="ml-72">

        <Topbar />

        <div className="space-y-8 p-8">

          {/* Header */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            className="rounded-3xl border border-cyan-500/20 bg-cyan-500/5 p-8 backdrop-blur-xl"
          >

            <div className="flex items-center gap-4">

              <div className="rounded-2xl bg-cyan-500/10 p-4">
                <ShieldAlert
                  className="text-cyan-400"
                  size={32}
                />
              </div>

              <div>
                <h1 className="text-4xl font-bold">
                  AI Risk Intelligence Engine
                </h1>

                <p className="mt-2 text-gray-400">
                  AI-powered genomic privacy analysis and
                  exposure detection system
                </p>
              </div>

            </div>

          </motion.div>

          {/* Risk Overview */}
          <div className="grid gap-6 xl:grid-cols-4">

            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl"
            >

              <p className="text-sm text-gray-400">
                Privacy Risk Score
              </p>

              <h2 className="mt-4 text-5xl font-bold text-yellow-400">
                72%
              </h2>

              <p className="mt-3 text-sm text-gray-500">
                Elevated genomic identifiability
              </p>

            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1 }}
              className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl"
            >

              <p className="text-sm text-gray-400">
                Ancestry Exposure
              </p>

              <h2 className="mt-4 text-5xl font-bold text-red-400">
                HIGH
              </h2>

              <p className="mt-3 text-sm text-gray-500">
                Public genomic matching possible
              </p>

            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
              className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl"
            >

              <p className="text-sm text-gray-400">
                Encryption Status
              </p>

              <h2 className="mt-4 text-5xl font-bold text-green-400">
                SAFE
              </h2>

              <p className="mt-3 text-sm text-gray-500">
                AES-256 secure genomic vault
              </p>

            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 }}
              className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl"
            >

              <p className="text-sm text-gray-400">
                Threat Detection
              </p>

              <h2 className="mt-4 text-5xl font-bold text-cyan-400">
                ACTIVE
              </h2>

              <p className="mt-3 text-sm text-gray-500">
                Real-time genomic monitoring
              </p>

            </motion.div>

          </div>

          {/* Main Grid */}
          <div className="grid gap-8 xl:grid-cols-3">

            {/* AI Findings */}
            <div className="xl:col-span-2 rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">

              <div className="flex items-center gap-3">

                <div className="rounded-xl bg-cyan-500/10 p-3">
                  <ScanSearch className="text-cyan-400" />
                </div>

                <div>
                  <h2 className="text-3xl font-bold">
                    AI Genomic Findings
                  </h2>

                  <p className="mt-1 text-gray-400">
                    Automated privacy intelligence report
                  </p>
                </div>

              </div>

              <div className="mt-10 space-y-6">

                <div className="rounded-2xl border border-yellow-500/20 bg-yellow-500/5 p-6">

                  <div className="flex items-center gap-3">

                    <AlertTriangle
                      className="text-yellow-400"
                      size={24}
                    />

                    <h3 className="text-xl font-semibold text-yellow-300">
                      Elevated Re-Identification Risk
                    </h3>

                  </div>

                  <p className="mt-4 leading-relaxed text-gray-300">
                    AI analysis detected identifiable ancestry-linked
                    genomic markers with elevated public matching
                    probability across external genomic databases.
                  </p>

                </div>

                <div className="rounded-2xl border border-red-500/20 bg-red-500/5 p-6">

                  <div className="flex items-center gap-3">

                    <ShieldAlert
                      className="text-red-400"
                      size={24}
                    />

                    <h3 className="text-xl font-semibold text-red-300">
                      Potential Exposure Pathway
                    </h3>

                  </div>

                  <p className="mt-4 leading-relaxed text-gray-300">
                    Shared mutation segments may allow indirect
                    lineage tracing through third-party genomic
                    correlation systems.
                  </p>

                </div>

                <div className="rounded-2xl border border-green-500/20 bg-green-500/5 p-6">

                  <div className="flex items-center gap-3">

                    <ShieldCheck
                      className="text-green-400"
                      size={24}
                    />

                    <h3 className="text-xl font-semibold text-green-300">
                      Encryption Integrity Verified
                    </h3>

                  </div>

                  <p className="mt-4 leading-relaxed text-gray-300">
                    Genomic vault encryption protocols remain secure
                    with no detected compromise attempts within the
                    current monitoring cycle.
                  </p>

                </div>

              </div>

            </div>

            {/* DNA Visualization */}
            <div className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">

              <div className="flex items-center gap-3">

                <div className="rounded-xl bg-cyan-500/10 p-3">
                  <Dna className="text-cyan-400" />
                </div>

                <div>
                  <h2 className="text-2xl font-bold">
                    Genome Map
                  </h2>

                  <p className="mt-1 text-gray-400">
                    Exposure visualization
                  </p>
                </div>

              </div>

              {/* Fake DNA Graphic */}
              <div className="mt-10 flex flex-col gap-4">

                {[72, 40, 90, 55, 81, 33].map((width, index) => (
                  <motion.div
                    key={index}
                    initial={{ width: 0 }}
                    animate={{ width: `${width}%` }}
                    transition={{
                      duration: 1,
                      delay: index * 0.2,
                    }}
                    className="h-4 rounded-full bg-gradient-to-r from-cyan-400 to-blue-500"
                  />
                ))}

              </div>

              <div className="mt-10 space-y-5">

                <div className="flex items-center justify-between">

                  <p className="text-sm text-gray-400">
                    Protected Segments
                  </p>

                  <p className="text-cyan-400">
                    82%
                  </p>

                </div>

                <div className="flex items-center justify-between">

                  <p className="text-sm text-gray-400">
                    Exposed Markers
                  </p>

                  <p className="text-yellow-400">
                    11%
                  </p>

                </div>

                <div className="flex items-center justify-between">

                  <p className="text-sm text-gray-400">
                    Risk Criticality
                  </p>

                  <p className="text-red-400">
                    Moderate
                  </p>

                </div>

              </div>

            </div>

          </div>

          {/* AI Recommendations */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            className="rounded-3xl border border-cyan-500/20 bg-cyan-500/5 p-8 backdrop-blur-xl"
          >

            <h2 className="text-3xl font-bold">
              AI Security Recommendations
            </h2>

            <p className="mt-2 text-gray-400">
              Suggested actions based on genomic privacy analysis
            </p>

            <div className="mt-10 grid gap-6 md:grid-cols-3">

              <div className="rounded-2xl border border-white/10 bg-black/30 p-6">

                <h3 className="text-xl font-semibold text-white">
                  Restrict External Sharing
                </h3>

                <p className="mt-3 text-sm leading-relaxed text-gray-400">
                  Limit third-party genomic export access for
                  ancestry-sensitive genomic regions.
                </p>

              </div>

              <div className="rounded-2xl border border-white/10 bg-black/30 p-6">

                <h3 className="text-xl font-semibold text-white">
                  Enable Selective Masking
                </h3>

                <p className="mt-3 text-sm leading-relaxed text-gray-400">
                  Mask lineage-linked mutation segments before
                  research collaboration workflows.
                </p>

              </div>

              <div className="rounded-2xl border border-white/10 bg-black/30 p-6">

                <h3 className="text-xl font-semibold text-white">
                  Increase Monitoring
                </h3>

                <p className="mt-3 text-sm leading-relaxed text-gray-400">
                  Activate continuous anomaly detection for
                  privileged genomic access sessions.
                </p>

              </div>

            </div>

          </motion.div>

        </div>

      </div>

    </main>
  );
}