"use client";

import { useState } from "react";

import Sidebar from "@/components/Sidebar";
import Topbar from "@/components/Topbar";

import {
  UploadCloud,
  ShieldCheck,
  Loader2,
  AlertTriangle,
} from "lucide-react";

import { Button } from "@/components/ui/button";

export default function UploadPage() {

  const [file, setFile] = useState<File | null>(null);

  const [uploading, setUploading] = useState(false);

  const [result, setResult] = useState<any>(null);

  const handleUpload = async () => {

    if (!file) return;

    setUploading(true);

    const formData = new FormData();

    formData.append("file", file);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/upload-genome",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      console.log(data);

      setResult(data);

    } catch (error) {

      console.error(error);

    } finally {

      setUploading(false);

    }
  };

  // ---------------------------------------------------
  // SAFE ACCESSORS
  // ---------------------------------------------------

  const analysis = result?.risk_analysis?.[0];

  const parsedGenome = result?.parsed_data?.[0];

  return (

    <main className="min-h-screen bg-black text-white">

      <Sidebar />

      <div className="ml-72">

        <Topbar />

        <div className="p-8">

          <div className="mx-auto max-w-5xl rounded-3xl border border-white/10 bg-white/5 p-10 backdrop-blur-xl">

            {/* Header */}
            <div className="flex items-center gap-4">

              <div className="rounded-2xl bg-cyan-500/10 p-4">

                <UploadCloud
                  className="text-cyan-400"
                  size={32}
                />

              </div>

              <div>

                <h1 className="text-4xl font-bold">
                  Upload Genomic Data
                </h1>

                <p className="mt-2 text-gray-400">
                  Secure genomic acquisition and AI-powered
                  privacy intelligence analysis
                </p>

              </div>

            </div>

            {/* Upload Area */}
            <div className="mt-10 rounded-3xl border-2 border-dashed border-cyan-500/20 bg-black/30 p-16 text-center">

              <div className="flex flex-col items-center">

                <div className="rounded-full bg-cyan-500/10 p-5">

                  <UploadCloud
                    className="text-cyan-400"
                    size={42}
                  />

                </div>

                <h2 className="mt-6 text-2xl font-semibold">
                  Upload FASTA Genomic File
                </h2>

                <p className="mt-3 max-w-xl text-sm leading-relaxed text-gray-400">
                  GeneTrust securely encrypts, analyzes,
                  and monitors genomic identity data using
                  AI-native security infrastructure.
                </p>

                {/* File Input */}
                <input
                  type="file"
                  accept=".fasta,.fa,.fastq,.fq"
                  onChange={(e) =>
                    setFile(e.target.files?.[0] || null)
                  }
                  className="mt-8 rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm text-gray-300"
                />

                {/* Upload Button */}
                <div className="mt-8">

                  {!uploading && (

                    <Button
                      onClick={handleUpload}
                      className="bg-cyan-500 px-6 py-6 text-black hover:bg-cyan-400"
                    >
                      Analyze Genome
                    </Button>

                  )}

                  {uploading && (

                    <Button
                      disabled
                      className="bg-cyan-500 px-6 py-6 text-black"
                    >

                      <Loader2 className="mr-2 animate-spin" />

                      Encrypting & Analyzing...

                    </Button>

                  )}

                </div>

              </div>

            </div>

            {/* Results */}
            {result && (

              <div className="mt-10 space-y-8">

                {/* Success */}
                <div className="flex items-center gap-3 rounded-2xl border border-green-500/20 bg-green-500/10 px-6 py-4 text-green-400">

                  <ShieldCheck />

                  Genome successfully secured and analyzed

                </div>

                {/* Metrics */}
                <div className="grid gap-6 md:grid-cols-3">

                  {/* Genome ID */}
                  <div className="rounded-3xl border border-white/10 bg-black/40 p-6">

                    <p className="text-sm text-gray-400">
                      Genome ID
                    </p>

                    <h2 className="mt-4 text-3xl font-bold text-cyan-400">

                      {result.genome_id}

                    </h2>

                  </div>

                  {/* Risk Level */}
                  <div className="rounded-3xl border border-white/10 bg-black/40 p-6">

                    <p className="text-sm text-gray-400">
                      Risk Level
                    </p>

                    <h2 className="mt-4 text-3xl font-bold text-yellow-400">

                      {analysis?.risk_level?.toUpperCase() || "UNKNOWN"}

                    </h2>

                  </div>

                  {/* Risk Score */}
                  <div className="rounded-3xl border border-white/10 bg-black/40 p-6">

                    <p className="text-sm text-gray-400">
                      Risk Score
                    </p>

                    <h2 className="mt-4 text-3xl font-bold text-red-400">

                      {analysis?.risk_score || 0}

                    </h2>

                  </div>

                </div>

                {/* Parsed Data */}
                <div className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">

                  <h2 className="text-3xl font-bold">
                    Genomic Analysis
                  </h2>

                  <div className="mt-8 grid gap-6 md:grid-cols-3">

                    {/* Genome Length */}
                    <div>

                      <p className="text-sm text-gray-400">
                        Genome Length
                      </p>

                      <h3 className="mt-2 text-2xl font-bold text-cyan-400">

                        {parsedGenome?.sequence_length || 0}

                      </h3>

                    </div>

                    {/* GC Content */}
                    <div>

                      <p className="text-sm text-gray-400">
                        GC Content
                      </p>

                      <h3 className="mt-2 text-2xl font-bold text-green-400">

                        {parsedGenome?.gc_content || 0}%

                      </h3>

                    </div>

                    {/* Preview */}
                    <div>

                      <p className="text-sm text-gray-400">
                        Genome Preview
                      </p>

                      <h3 className="mt-2 break-all text-sm text-gray-300">

                        {parsedGenome?.sequence_preview || "N/A"}

                      </h3>

                    </div>

                  </div>

                </div>

                {/* AI Findings */}
                <div className="grid gap-6 xl:grid-cols-2">

                  {/* Findings */}
                  <div className="rounded-3xl border border-yellow-500/20 bg-yellow-500/5 p-8">

                    <div className="flex items-center gap-3">

                      <AlertTriangle className="text-yellow-400" />

                      <h2 className="text-2xl font-bold">
                        AI Findings
                      </h2>

                    </div>

                    <div className="mt-6 space-y-4">

                      {analysis?.findings?.map(
                        (
                          finding: string,
                          index: number
                        ) => (

                          <div
                            key={index}
                            className="rounded-2xl border border-yellow-500/10 bg-black/30 p-4"
                          >

                            <p className="text-gray-300">
                              {finding}
                            </p>

                          </div>

                        )
                      )}

                    </div>

                  </div>

                  {/* Recommendations */}
                  <div className="rounded-3xl border border-cyan-500/20 bg-cyan-500/5 p-8">

                    <h2 className="text-2xl font-bold">
                      AI Recommendations
                    </h2>

                    <div className="mt-6 space-y-4">

                      {analysis?.recommendations?.map(
                        (
                          rec: string,
                          index: number
                        ) => (

                          <div
                            key={index}
                            className="rounded-2xl border border-cyan-500/10 bg-black/30 p-4"
                          >

                            <p className="text-gray-300">
                              {rec}
                            </p>

                          </div>

                        )
                      )}

                    </div>

                  </div>

                </div>

              </div>

            )}

          </div>

        </div>

      </div>

    </main>
  );
}