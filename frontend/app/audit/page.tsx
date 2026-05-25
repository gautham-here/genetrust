"use client";

import Sidebar from "@/components/Sidebar";
import Topbar from "@/components/Topbar";

import {
  ClipboardList,
  ShieldAlert,
  Eye,
  Lock,
  Database,
} from "lucide-react";

import { motion } from "framer-motion";

const logs = [
  {
    action: "Genome Access Approved",
    user: "Research Unit 7",
    genome: "GTX-29301",
    severity: "Low",
    time: "2 min ago",
  },
  {
    action: "Unauthorized Access Attempt",
    user: "External Node",
    genome: "GTX-88312",
    severity: "Critical",
    time: "12 min ago",
  },
  {
    action: "Genome Encryption Updated",
    user: "Admin Console",
    genome: "GTX-10293",
    severity: "Medium",
    time: "24 min ago",
  },
  {
    action: "AI Risk Scan Completed",
    user: "AI Security Engine",
    genome: "GTX-44882",
    severity: "Low",
    time: "41 min ago",
  },
];

export default function AuditPage() {
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
                <ClipboardList
                  className="text-cyan-400"
                  size={32}
                />
              </div>

              <div>
                <h1 className="text-4xl font-bold">
                  Audit & Compliance Logs
                </h1>

                <p className="mt-2 text-gray-400">
                  Real-time genomic infrastructure monitoring
                  and compliance visibility
                </p>
              </div>

            </div>

          </motion.div>

          {/* Metrics */}
          <div className="grid gap-6 xl:grid-cols-4">

            <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

              <p className="text-sm text-gray-400">
                Access Requests
              </p>

              <h2 className="mt-4 text-5xl font-bold text-cyan-400">
                482
              </h2>

              <p className="mt-3 text-sm text-gray-500">
                Active genomic interactions
              </p>

            </div>

            <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

              <p className="text-sm text-gray-400">
                Threat Escalations
              </p>

              <h2 className="mt-4 text-5xl font-bold text-red-400">
                19
              </h2>

              <p className="mt-3 text-sm text-gray-500">
                Security incidents detected
              </p>

            </div>

            <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

              <p className="text-sm text-gray-400">
                Encryption Integrity
              </p>

              <h2 className="mt-4 text-5xl font-bold text-green-400">
                SAFE
              </h2>

              <p className="mt-3 text-sm text-gray-500">
                Vault systems operational
              </p>

            </div>

            <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

              <p className="text-sm text-gray-400">
                Compliance Score
              </p>

              <h2 className="mt-4 text-5xl font-bold text-yellow-400">
                98%
              </h2>

              <p className="mt-3 text-sm text-gray-500">
                Infrastructure governance rating
              </p>

            </div>

          </div>

          {/* Main Grid */}
          <div className="grid gap-8 xl:grid-cols-3">

            {/* Logs Table */}
            <div className="xl:col-span-2 rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">

              <div className="flex items-center gap-3">

                <div className="rounded-xl bg-cyan-500/10 p-3">
                  <Database className="text-cyan-400" />
                </div>

                <div>
                  <h2 className="text-3xl font-bold">
                    Genomic Activity Logs
                  </h2>

                  <p className="mt-1 text-gray-400">
                    Monitored genomic infrastructure events
                  </p>
                </div>

              </div>

              <div className="mt-10 overflow-x-auto">

                <table className="w-full text-left">

                  <thead className="border-b border-white/10 text-sm text-gray-400">

                    <tr>
                      <th className="pb-4">Action</th>
                      <th className="pb-4">User</th>
                      <th className="pb-4">Genome ID</th>
                      <th className="pb-4">Severity</th>
                      <th className="pb-4">Time</th>
                    </tr>

                  </thead>

                  <tbody>

                    {logs.map((log, index) => (
                      <motion.tr
                        key={index}
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.1 }}
                        className="border-b border-white/5"
                      >

                        <td className="py-5 font-medium text-white">
                          {log.action}
                        </td>

                        <td className="py-5 text-gray-300">
                          {log.user}
                        </td>

                        <td className="py-5 text-cyan-400">
                          {log.genome}
                        </td>

                        <td className="py-5">

                          <span
                            className={`rounded-full px-3 py-1 text-sm ${
                              log.severity === "Critical"
                                ? "bg-red-500/10 text-red-400"
                                : log.severity === "Medium"
                                ? "bg-yellow-500/10 text-yellow-400"
                                : "bg-green-500/10 text-green-400"
                            }`}
                          >
                            {log.severity}
                          </span>

                        </td>

                        <td className="py-5 text-gray-500">
                          {log.time}
                        </td>

                      </motion.tr>
                    ))}

                  </tbody>

                </table>

              </div>

            </div>

            {/* Security Panel */}
            <div className="space-y-8">

              {/* Live Monitoring */}
              <div className="rounded-3xl border border-red-500/20 bg-red-500/5 p-6 backdrop-blur-xl">

                <div className="flex items-center gap-3">

                  <div className="rounded-xl bg-red-500/10 p-3">
                    <ShieldAlert className="text-red-400" />
                  </div>

                  <div>
                    <h2 className="text-2xl font-bold">
                      Threat Monitor
                    </h2>

                    <p className="mt-1 text-gray-400">
                      Active genomic security events
                    </p>
                  </div>

                </div>

                <div className="mt-8 space-y-4">

                  <div className="rounded-2xl border border-red-500/10 bg-black/30 p-4">

                    <p className="text-sm leading-relaxed text-red-300">
                      External genomic export attempt detected
                    </p>

                  </div>

                  <div className="rounded-2xl border border-red-500/10 bg-black/30 p-4">

                    <p className="text-sm leading-relaxed text-red-300">
                      Elevated lineage tracing probability identified
                    </p>

                  </div>

                </div>

              </div>

              {/* Access Integrity */}
              <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

                <div className="flex items-center gap-3">

                  <div className="rounded-xl bg-cyan-500/10 p-3">
                    <Lock className="text-cyan-400" />
                  </div>

                  <div>
                    <h2 className="text-2xl font-bold">
                      Access Integrity
                    </h2>

                    <p className="mt-1 text-gray-400">
                      Permission governance
                    </p>
                  </div>

                </div>

                <div className="mt-8 space-y-5">

                  <div className="flex items-center justify-between">

                    <p className="text-gray-400">
                      Secure Sessions
                    </p>

                    <p className="text-green-400">
                      94%
                    </p>

                  </div>

                  <div className="flex items-center justify-between">

                    <p className="text-gray-400">
                      Restricted Access
                    </p>

                    <p className="text-yellow-400">
                      Enabled
                    </p>

                  </div>

                  <div className="flex items-center justify-between">

                    <p className="text-gray-400">
                      Identity Verification
                    </p>

                    <p className="text-cyan-400">
                      Active
                    </p>

                  </div>

                </div>

              </div>

              {/* Surveillance */}
              <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

                <div className="flex items-center gap-3">

                  <div className="rounded-xl bg-cyan-500/10 p-3">
                    <Eye className="text-cyan-400" />
                  </div>

                  <div>
                    <h2 className="text-2xl font-bold">
                      Surveillance Layer
                    </h2>

                    <p className="mt-1 text-gray-400">
                      AI monitoring systems
                    </p>
                  </div>

                </div>

                <div className="mt-8 flex h-[140px] items-center justify-center">

                  <div className="text-center">

                    <div className="text-5xl font-bold text-cyan-400">
                      ACTIVE
                    </div>

                    <p className="mt-4 text-gray-400">
                      Continuous genomic threat analysis
                    </p>

                  </div>

                </div>

              </div>

            </div>

          </div>

        </div>

      </div>

    </main>
  );
}