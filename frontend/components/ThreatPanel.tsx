"use client";

const threats = [
  "Unauthorized genomic export attempt detected",
  "Multiple failed access attempts from external node",
  "AI privacy risk score elevated for GTX-29301",
];

export default function ThreatPanel() {
  return (
    <div className="rounded-3xl border border-red-500/20 bg-red-500/5 p-6 backdrop-blur-xl">

      <h2 className="text-2xl font-bold text-white">
        Threat Intelligence
      </h2>

      <p className="mt-1 text-sm text-gray-400">
        Real-time genomic security monitoring
      </p>

      <div className="mt-6 flex flex-col gap-4">

        {threats.map((threat, index) => (
          <div
            key={index}
            className="rounded-2xl border border-red-500/10 bg-black/30 p-4"
          >
            <p className="text-sm leading-relaxed text-red-300">
              {threat}
            </p>
          </div>
        ))}

      </div>
    </div>
  );
}