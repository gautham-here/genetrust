"use client";

const activities = [
  {
    title: "Genome GTX-10293 uploaded",
    time: "2 min ago",
  },
  {
    title: "Access request approved for Research Unit 7",
    time: "14 min ago",
  },
  {
    title: "AI anomaly scan completed",
    time: "26 min ago",
  },
  {
    title: "Threat alert escalated",
    time: "1 hour ago",
  },
];

export default function ActivityTimeline() {
  return (
    <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

      <h2 className="text-2xl font-bold text-white">
        Activity Timeline
      </h2>

      <p className="mt-1 text-sm text-gray-400">
        Recent genomic infrastructure events
      </p>

      <div className="mt-8 flex flex-col gap-6">

        {activities.map((activity, index) => (
          <div
            key={index}
            className="flex items-start gap-4"
          >

            <div className="mt-2 h-3 w-3 rounded-full bg-cyan-400" />

            <div>
              <p className="text-white">
                {activity.title}
              </p>

              <p className="mt-1 text-sm text-gray-500">
                {activity.time}
              </p>
            </div>

          </div>
        ))}

      </div>
    </div>
  );
}