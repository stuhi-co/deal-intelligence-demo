/* ─────────────────────────────────────────────────────────────────────
 *  Hand-tuned line icons. Geometric, 1.5px stroke, no Lucide tropes.
 *  All icons sized 16 by default; pass size= to override.
 * ───────────────────────────────────────────────────────────────────── */

const Icon = ({ children, size = 16, ...rest }) => (
  <svg
    viewBox="0 0 24 24"
    width={size}
    height={size}
    fill="none"
    stroke="currentColor"
    strokeWidth="1.5"
    strokeLinecap="round"
    strokeLinejoin="round"
    {...rest}
  >
    {children}
  </svg>
);

const Icons = {
  Plus:   (p) => <Icon {...p}><line x1="12" y1="5" x2="12" y2="19" /><line x1="5" y1="12" x2="19" y2="12" /></Icon>,
  Search: (p) => <Icon {...p}><circle cx="11" cy="11" r="6" /><line x1="20" y1="20" x2="15.5" y2="15.5" /></Icon>,
  Sun:    (p) => <Icon {...p}><circle cx="12" cy="12" r="3.5" /><line x1="12" y1="3" x2="12" y2="5" /><line x1="12" y1="19" x2="12" y2="21" /><line x1="3" y1="12" x2="5" y2="12" /><line x1="19" y1="12" x2="21" y2="12" /><line x1="5.6" y1="5.6" x2="7" y2="7" /><line x1="17" y1="17" x2="18.4" y2="18.4" /><line x1="5.6" y1="18.4" x2="7" y2="17" /><line x1="17" y1="7" x2="18.4" y2="5.6" /></Icon>,
  Moon:   (p) => <Icon {...p}><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z" /></Icon>,
  Arrow:  (p) => <Icon {...p}><line x1="5" y1="12" x2="19" y2="12" /><polyline points="13,6 19,12 13,18" /></Icon>,
  ArrowUp:(p) => <Icon {...p}><line x1="12" y1="19" x2="12" y2="5" /><polyline points="6,11 12,5 18,11" /></Icon>,
  Close:  (p) => <Icon {...p}><line x1="6" y1="6" x2="18" y2="18" /><line x1="18" y1="6" x2="6" y2="18" /></Icon>,
};

window.Icon = Icon;
window.Icons = Icons;
