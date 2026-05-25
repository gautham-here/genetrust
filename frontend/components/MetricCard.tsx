interface MetricCardProps {
  title: string;
  value: string;
  description: string;
}

export default function MetricCard({
  title,
  value,
  description,
}: MetricCardProps) {
  return (
    <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

      <p className="text-sm text-gray-400">
        {title}
      </p>

      <h2 className="mt-4 text-4xl font-bold text-cyan-400">
        {value}
      </h2>

      <p className="mt-3 text-sm text-gray-500">
        {description}
      </p>

    </div>
  );
}