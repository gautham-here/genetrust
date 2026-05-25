"use client";

import Link from "next/link";
import {
  Shield,
  Dna,
  Lock,
  Activity,
  ChevronRight,
  Database,
  ScanSearch,
  Fingerprint,
} from "lucide-react";

import { motion } from "framer-motion";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function HomePage() {
  return (
    <main className="relative min-h-screen overflow-hidden bg-black text-white">

      {/* Background Effects */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,#0f172a,transparent_40%)] opacity-80" />
      <div className="absolute left-0 top-0 h-[500px] w-[500px] rounded-full bg-cyan-500/10 blur-3xl" />
      <div className="absolute bottom-0 right-0 h-[500px] w-[500px] rounded-full bg-blue-500/10 blur-3xl" />

      {/* Navbar */}
      <nav className="relative z-20 flex items-center justify-between border-b border-white/10 px-8 py-6 backdrop-blur-xl">
        <div className="flex items-center gap-3">
          <div className="rounded-xl bg-cyan-500/10 p-2">
            <Dna className="text-cyan-400" size={24} />
          </div>

          <h1 className="text-2xl font-bold tracking-tight">
            GeneTrust
          </h1>
        </div>

        <div className="flex items-center gap-4">
          <Link href="/dashboard">
            <Button
              variant="outline"
              className="border-white/10 bg-white/5 hover:bg-white/10"
            >
              Dashboard
            </Button>
          </Link>
        </div>
      </nav>

      {/* Hero */}
      <section className="relative z-10 flex flex-col items-center justify-center px-6 pb-32 pt-28 text-center">

        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="mb-6 flex items-center gap-2 rounded-full border border-cyan-500/20 bg-cyan-500/10 px-5 py-2 text-sm text-cyan-300 backdrop-blur-xl"
        >
          <Shield size={16} />
          AI-Native Genomic Security Infrastructure
        </motion.div>

        <motion.h1
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.9 }}
          className="max-w-6xl text-5xl font-bold leading-tight tracking-tight md:text-7xl"
        >
          Protecting the
          <span className="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
            {" "}Most Permanent{" "}
          </span>
          Form of Human Identity
        </motion.h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4 }}
          className="mt-8 max-w-3xl text-lg leading-relaxed text-gray-400"
        >
          GeneTrust is a secure genomic infrastructure platform for
          acquiring, storing, analyzing, and controlling access to
          genomic identity data.
          Built for the future of precision medicine,
          biotech collaboration, and AI-powered healthcare systems.
        </motion.p>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.7 }}
          className="mt-10 flex flex-wrap items-center justify-center gap-4"
        >
          <Link href="/upload">
            <Button className="rounded-xl bg-cyan-500 px-7 py-6 text-base font-semibold text-black hover:bg-cyan-400">
              Launch Vault
            </Button>
          </Link>

          <Link href="/risk-analysis">
            <Button
              variant="outline"
              className="rounded-xl border-white/10 bg-white/5 px-7 py-6 text-base hover:bg-white/10"
            >
              View Risk Engine
            </Button>
          </Link>
        </motion.div>
      </section>

      {/* Metrics */}
      <section className="relative z-10 px-8 pb-24">
        <div className="mx-auto grid max-w-6xl grid-cols-2 gap-6 md:grid-cols-4">

          {[
            ["256-bit", "AES Encryption"],
            ["24/7", "Threat Monitoring"],
            ["AI", "Risk Intelligence"],
            ["DNA", "Identity Protection"],
          ].map((item, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.1 }}
              viewport={{ once: true }}
              className="rounded-2xl border border-white/10 bg-white/5 p-6 text-center backdrop-blur-xl"
            >
              <h2 className="text-3xl font-bold text-cyan-400">
                {item[0]}
              </h2>

              <p className="mt-2 text-sm text-gray-400">
                {item[1]}
              </p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Problem Section */}
      <section className="relative z-10 px-8 py-24">
        <div className="mx-auto max-w-5xl text-center">

          <motion.h2
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-4xl font-bold leading-tight md:text-5xl"
          >
            Genomic Data Is the Most Sensitive
            <span className="text-cyan-400">
              {" "}Digital Identity Layer
            </span>
          </motion.h2>

          <motion.p
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ delay: 0.2 }}
            viewport={{ once: true }}
            className="mt-8 text-lg leading-relaxed text-gray-400"
          >
            Unlike passwords, genomic identity cannot be reset.
            DNA data contains inherited traits, ancestry markers,
            disease predispositions, and biological signatures
            that impact entire family lineages.
          </motion.p>

          <motion.p
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ delay: 0.4 }}
            viewport={{ once: true }}
            className="mt-6 text-lg leading-relaxed text-gray-400"
          >
            GeneTrust secures the full genomic lifecycle —
            from acquisition and encrypted storage to
            AI-powered privacy analysis and controlled access.
          </motion.p>
        </div>
      </section>

      {/* Features */}
      <section className="relative z-10 px-8 pb-24">
        <div className="mx-auto grid max-w-7xl gap-6 md:grid-cols-2 lg:grid-cols-4">

          {[
            {
              icon: <Lock className="text-cyan-400" />,
              title: "Secure Genomic Vault",
              desc: "Encrypted genomic storage with role-based access control and secure retrieval systems.",
            },
            {
              icon: <Dna className="text-cyan-400" />,
              title: "Genomic Intelligence",
              desc: "AI-powered genomic privacy analysis, identifiability scoring, and exposure insights.",
            },
            {
              icon: <Shield className="text-cyan-400" />,
              title: "Threat Monitoring",
              desc: "Detect suspicious access behavior and unauthorized genomic sharing attempts.",
            },
            {
              icon: <Activity className="text-cyan-400" />,
              title: "Audit & Compliance",
              desc: "Full genomic access visibility with audit trails and governance dashboards.",
            },
          ].map((feature, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.15 }}
              viewport={{ once: true }}
            >
              <Card className="border-white/10 bg-white/5 backdrop-blur-xl transition-all duration-300 hover:border-cyan-500/30 hover:bg-white/10">
                <CardContent className="p-6">

                  <div className="mb-4 w-fit rounded-xl bg-cyan-500/10 p-3">
                    {feature.icon}
                  </div>

                  <h3 className="text-xl font-semibold text-white">
                    {feature.title}
                  </h3>

                  <p className="mt-4 text-sm leading-relaxed text-gray-400">
                    {feature.desc}
                  </p>

                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Workflow */}
      <section className="relative z-10 px-8 py-24">
        <div className="mx-auto max-w-7xl">

          <div className="text-center">
            <h2 className="text-4xl font-bold">
              How GeneTrust Works
            </h2>

            <p className="mt-4 text-gray-400">
              End-to-end genomic identity infrastructure
            </p>
          </div>

          <div className="mt-16 grid gap-6 md:grid-cols-4">

            {[
              {
                number: "01",
                title: "Acquire",
                icon: <Database className="text-cyan-400" />,
                desc: "Upload genomic files and sequencing outputs securely.",
              },
              {
                number: "02",
                title: "Encrypt",
                icon: <Fingerprint className="text-cyan-400" />,
                desc: "Protect genomic identity using encrypted vault systems.",
              },
              {
                number: "03",
                title: "Analyze",
                icon: <ScanSearch className="text-cyan-400" />,
                desc: "AI evaluates genomic privacy exposure and anomalies.",
              },
              {
                number: "04",
                title: "Control",
                icon: <Shield className="text-cyan-400" />,
                desc: "Grant secure permission-based genomic access.",
              },
            ].map((step, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 40 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.12 }}
                viewport={{ once: true }}
                className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl"
              >
                <div className="flex items-center justify-between">
                  <div className="text-3xl font-bold text-cyan-400">
                    {step.number}
                  </div>

                  {step.icon}
                </div>

                <h3 className="mt-6 text-2xl font-semibold text-white">
                  {step.title}
                </h3>

                <p className="mt-4 text-sm leading-relaxed text-gray-400">
                  {step.desc}
                </p>

              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="relative z-10 px-8 py-28">
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          className="mx-auto max-w-5xl rounded-3xl border border-cyan-500/20 bg-cyan-500/10 p-12 text-center backdrop-blur-xl"
        >
          <h2 className="text-4xl font-bold md:text-5xl">
            The Future of Precision Medicine
            Requires Trust
          </h2>

          <p className="mt-6 text-lg leading-relaxed text-gray-300">
            GeneTrust secures genomic identity infrastructure
            for the next generation of AI-powered healthcare systems.
          </p>

          <div className="mt-10 flex flex-wrap justify-center gap-4">

            <Link href="/dashboard">
              <Button className="rounded-xl bg-cyan-500 px-7 py-6 text-black hover:bg-cyan-400">
                Open Dashboard
                <ChevronRight className="ml-2" size={18} />
              </Button>
            </Link>

            <Link href="/upload">
              <Button
                variant="outline"
                className="rounded-xl border-white/10 bg-white/5 px-7 py-6 hover:bg-white/10"
              >
                Upload Genome
              </Button>
            </Link>

          </div>
        </motion.div>
      </section>

      {/* Footer */}
      <footer className="relative z-10 border-t border-white/10 px-8 py-6 text-center text-sm text-gray-500">
        GeneTrust © 2026 — Secure Infrastructure for Genomic Identity
      </footer>
    </main>
  );
}