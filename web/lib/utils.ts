export function relativeTime(ts: number): string {
  const diff = (Date.now() - ts) / 1000;
  if (diff < 60) return "just now";
  if (diff < 60 * 60) return Math.floor(diff / 60) + "m ago";
  if (diff < 60 * 60 * 24) return Math.floor(diff / 3600) + "h ago";
  if (diff < 60 * 60 * 24 * 7) {
    const d = Math.floor(diff / 86400);
    return d === 1 ? "yesterday" : d + "d ago";
  }
  return new Date(ts).toLocaleDateString(undefined, {
    month: "short",
    day: "numeric",
  });
}
