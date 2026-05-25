import Sidebar from "@/components/Sidebar";
import Topbar from "@/components/Topbar";
import MetricCard from "@/components/MetricCard";
import GenomeTable from "@/components/GenomeTable";
import ThreatPanel from "@/components/ThreatPanel";
import ActivityTimeline from "@/components/ActivityTimeline";

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-black text-white">

      <Sidebar />

      <div className="ml-72">

        <Topbar />

        <div className="space-y-8 p-8">

          {/* Metrics */}
          <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

            <MetricCard
              title="Stored Genomes"
              value="1,284"
              description="Encrypted genomic identities"
            />

            <MetricCard
              title="Threat Alerts"
              value="12"
              description="Potential exposure attempts"
            />

            <MetricCard
              title="Active Sessions"
              value="48"
              description="Current genomic interactions"
            />

            <MetricCard
              title="Compliance"
              value="98%"
              description="Infrastructure security rating"
            />

          </div>

          {/* Main Grid */}
          <div className="grid gap-8 xl:grid-cols-3">

            <div className="xl:col-span-2">
              <GenomeTable />
            </div>

            <ThreatPanel />

          </div>

          {/* Bottom Grid */}
          <div className="grid gap-8 xl:grid-cols-2">

            <ActivityTimeline />

            <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

              <h2 className="text-2xl font-bold text-white">
                AI Risk Distribution
              </h2>

              <p className="mt-1 text-sm text-gray-400">
                Genomic exposure classification
              </p>

              <div className="mt-10 flex h-[250px] items-center justify-center">

                <div className="flex flex-col items-center">

                  <div className="text-6xl font-bold text-cyan-400">
                    72%
                  </div>

                  <p className="mt-4 text-gray-400">
                    Low-Risk Genomic Profiles
                  </p>

                </div>

              </div>

            </div>

          </div>

        </div>

      </div>
    </main>
  );
}