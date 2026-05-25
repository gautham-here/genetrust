"use client";

import { useEffect, useState } from "react";

import {
  ShieldAlert,
  Dna,
} from "lucide-react";

interface Genome {
  id?: string;
  genome_code: string;
  filename: string;
  gc_content: number;
  genome_length: number;
  risk_level: string;
  risk_score: number;
  created_at?: string;
}

export default function GenomeTable() {

  const [genomes, setGenomes] = useState<Genome[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/genomes")
      .then((res) => res.json())
      .then((data) => {

        setGenomes(data);
        setLoading(false);

      })
      .catch((err) => {

        console.error(err);
        setLoading(false);

      });

  }, []);

  return (

    <div className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">

      {/* Header */}
      <div className="flex items-center gap-4">

        <div className="rounded-2xl bg-cyan-500/10 p-4">
          <Dna
            className="text-cyan-400"
            size={28}
          />
        </div>

        <div>
          <h2 className="text-3xl font-bold text-white">
            Genome Registry
          </h2>

          <p className="mt-1 text-gray-400">
            Secure genomic vault infrastructure
          </p>
        </div>

      </div>

      {/* Loading */}
      {loading && (

        <div className="mt-10 text-gray-400">
          Loading genomes...
        </div>

      )}

      {/* Empty State */}
      {!loading && genomes.length === 0 && (

        <div className="mt-10 rounded-2xl border border-white/10 bg-black/30 p-8 text-center">

          <p className="text-gray-400">
            No genomes uploaded yet.
          </p>

        </div>

      )}

      {/* Table */}
      {!loading && genomes.length > 0 && (

        <div className="mt-10 overflow-x-auto">

          <table className="w-full text-left">

            <thead className="border-b border-white/10 text-sm text-gray-400">

              <tr>

                <th className="pb-4">
                  Genome ID
                </th>

                <th className="pb-4">
                  File
                </th>

                <th className="pb-4">
                  GC Content
                </th>

                <th className="pb-4">
                  Length
                </th>

                <th className="pb-4">
                  Risk
                </th>

                <th className="pb-4">
                  Score
                </th>

              </tr>

            </thead>

            <tbody>

              {genomes.map((genome, index) => (

                <tr
                  key={index}
                  className="border-b border-white/5 transition hover:bg-white/5"
                >

                  {/* Genome ID */}
                  <td className="py-5">

                    <div className="font-semibold text-cyan-400">
                      {genome.genome_code}
                    </div>

                  </td>

                  {/* Filename */}
                  <td className="py-5 text-white">

                    {genome.filename}

                  </td>

                  {/* GC */}
                  <td className="py-5 text-green-400">

                    {genome.gc_content}%

                  </td>

                  {/* Length */}
                  <td className="py-5 text-gray-300">

                    {genome.genome_length}

                  </td>

                  {/* Risk */}
                  <td className="py-5">

                    <div
                      className={`inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-medium ${
                        genome.risk_level === "high"
                          ? "bg-red-500/10 text-red-400"
                          : genome.risk_level === "medium"
                          ? "bg-yellow-500/10 text-yellow-400"
                          : "bg-green-500/10 text-green-400"
                      }`}
                    >

                      <ShieldAlert size={16} />

                      {genome.risk_level.toUpperCase()}

                    </div>

                  </td>

                  {/* Score */}
                  <td className="py-5">

                    <span className="font-bold text-cyan-400">

                      {genome.risk_score}

                    </span>

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      )}

    </div>

  );
}